"""Human-approved file remediation API."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.models.remediation import RemediationJob
from app.models.user import User
from app.schemas.remediation import (
    RemediationDecisionRequest,
    RemediationJobResponse,
    RemediationPlanRequest,
)
from app.services.remediation_service import RemediationService


router = APIRouter(prefix="/remediations", tags=["remediations"])


def build_response(job: RemediationJob) -> RemediationJobResponse:
    return RemediationJobResponse(
        id=job.id,
        scan_id=job.scan_id,
        file_path=job.file_path,
        action=job.action.value if hasattr(job.action, "value") else str(job.action),
        status=job.status.value if hasattr(job.status, "value") else str(job.status),
        entity_types=list(job.entity_types or []),
        planner_output=dict(job.planner_output or {}),
        preview=dict(job.preview or {}),
        approval_required=job.approval_required,
        admin_required=job.admin_required,
        output_path=job.output_path,
        result=dict(job.result or {}),
        error=job.error_message,
        created_at=job.created_at.isoformat() if job.created_at else None,
        updated_at=job.updated_at.isoformat() if job.updated_at else None,
    )


@router.post("/plan", response_model=RemediationJobResponse, status_code=201)
def plan_remediation(
    payload: RemediationPlanRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a masked-metadata AI plan and wait for human approval."""
    try:
        return build_response(RemediationService(db).plan(current_user, payload))
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=str(error)) from error
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@router.get("", response_model=list[RemediationJobResponse])
def list_remediations(
    scan_id: int | None = Query(default=None, gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return [
        build_response(job)
        for job in RemediationService(db).list(current_user.id, scan_id)
    ]


@router.get("/{job_id}", response_model=RemediationJobResponse)
def get_remediation(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    job = RemediationService(db).get(job_id, current_user.id)

    if job is None:
        raise HTTPException(status_code=404, detail="Remediation job not found")

    return build_response(job)


@router.post("/{job_id}/decision", response_model=RemediationJobResponse)
def decide_remediation(
    job_id: int,
    payload: RemediationDecisionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Approve/reject a plan; an approval executes the bounded tool."""
    try:
        return build_response(
            RemediationService(db).decide(
                job_id,
                current_user,
                approved=payload.approved,
                note=payload.note,
            )
        )
    except PermissionError as error:
        raise HTTPException(status_code=403, detail=str(error)) from error
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
