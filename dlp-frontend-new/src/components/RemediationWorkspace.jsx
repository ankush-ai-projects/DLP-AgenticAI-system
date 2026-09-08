import { useCallback, useEffect, useMemo, useState } from 'react';

import { apiClient, formatApiError } from '../api/client';
import './RemediationWorkspace.css';

// The backend (app/schemas/remediation.py: RemediationActionValue) only
// supports these four -- no separate "unmask"/"decrypt" reverse actions,
// since recovery happens via the encrypted backup + admin approval flow,
// not a button. Only real, backend-supported actions are listed here.
const ACTIONS = [
  {
    action: 'mask',
    icon: '◐',
    title: 'Mask Data',
    description: 'Hide sensitive values while preserving format.',
  },
  {
    action: 'redact',
    icon: '▰',
    title: 'Redact Data',
    description: 'Permanently remove sensitive text.',
  },
  {
    action: 'encrypt',
    icon: '◇',
    title: 'Encrypt Data',
    description: 'Move sensitive content into an encrypted container.',
  },
  {
    action: 'delete',
    icon: '×',
    title: 'Delete Data',
    description: 'Admin-only removal, with an encrypted recovery copy.',
    danger: true,
  },
];

function groupFileFindings(findings) {
  const groups = new Map();

  findings.forEach((finding, index) => {
    const path = finding.location?.path;

    if (!path) {
      return;
    }

    const current = groups.get(path) || {
      path,
      findings: [],
      findingIndexes: [],
    };
    current.findings.push(finding);
    current.findingIndexes.push(index);
    groups.set(path, current);
  });

  return [...groups.values()];
}

export default function RemediationWorkspace({
  scanId,
  findings,
  preselectedIndexes = [],
  onClose,
}) {
  const fileGroups = useMemo(() => groupFileFindings(findings), [findings]);

  // The drawer opens already scoped to whatever the person checked in the
  // table -- if nothing valid was selected, fall back to the first file
  // so the drawer is never empty.
  const initialGroup = useMemo(() => {
    const selectedPaths = new Set(
      preselectedIndexes.map((i) => findings[i]?.location?.path).filter(Boolean),
    );
    if (selectedPaths.size > 0) {
      return fileGroups.find((group) => selectedPaths.has(group.path)) || fileGroups[0];
    }
    return fileGroups[0];
  }, [fileGroups, findings, preselectedIndexes]);

  const [selectedPath] = useState(initialGroup?.path || '');
  const [step, setStep] = useState('select-action'); // 'select-action' | 'parameters' | 'preview'
  const [selectedAction, setSelectedAction] = useState(null);
  const [reason, setReason] = useState('Protect verified sensitive data');
  const [decisionNote, setDecisionNote] = useState(
    'Reviewed remediation preview and safety controls',
  );
  const [activeJob, setActiveJob] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [isWorking, setIsWorking] = useState(false);
  const [remediationError, setRemediationError] = useState('');

  // Lock the page underneath while the drawer is open -- otherwise the
  // outer page's own scroll position can drift out of sync with the
  // fixed-position overlay, which is what was pushing the drawer's own
  // header text up and out of view in earlier testing.
  useEffect(() => {
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = previousOverflow;
    };
  }, []);

  const selectedGroup = fileGroups.find((group) => group.path === selectedPath);

  const loadJobs = useCallback(async () => {
    const response = await apiClient.get(
      `/api/v1/remediations?scan_id=${scanId}`,
    );
    setJobs(response.data);
  }, [scanId]);

  useEffect(() => {
    loadJobs().catch(() => {
      // Scan results still remain usable when no remediation history exists.
    });
  }, [loadJobs]);

  const chooseAction = (action) => {
    setSelectedAction(action);
    setStep('parameters');
  };

  const createPlan = async () => {
    if (!selectedGroup || !selectedAction) {
      return;
    }

    setIsWorking(true);
    setRemediationError('');

    try {
      const response = await apiClient.post('/api/v1/remediations/plan', {
        scan_id: scanId,
        file_path: selectedGroup.path,
        requested_action: selectedAction,
        finding_indexes: selectedGroup.findingIndexes,
        reason,
      });
      setActiveJob(response.data);
      setStep('preview');
      await loadJobs();
    } catch (requestError) {
      setRemediationError(formatApiError(requestError));
    } finally {
      setIsWorking(false);
    }
  };

  const decidePlan = async (approved) => {
    if (!activeJob) {
      return;
    }

    setIsWorking(true);
    setRemediationError('');

    try {
      const response = await apiClient.post(
        `/api/v1/remediations/${activeJob.id}/decision`,
        { approved, note: decisionNote },
      );
      setActiveJob(response.data);
      await loadJobs();
    } catch (requestError) {
      setRemediationError(formatApiError(requestError));
    } finally {
      setIsWorking(false);
    }
  };

  if (!selectedGroup) {
    return null;
  }

  return (
    <div className="remediation-drawer-overlay" onClick={onClose}>
      <aside
        className="remediation-drawer"
        onClick={(event) => event.stopPropagation()}
      >
        <header className="remediation-drawer__header">
          <div>
            <span className="eyebrow">🛡 Remediation Actions</span>
            <h2>{selectedGroup.path}</h2>
            <p>{selectedGroup.findings.length} selected finding(s)</p>
          </div>
          <button
            type="button"
            className="drawer-close"
            onClick={onClose}
            aria-label="Close remediation panel"
          >
            ×
          </button>
        </header>

        <div className="remediation-drawer__body">
          {remediationError && (
            <div className="remediation-error" role="alert">
              {remediationError}
            </div>
          )}

          {step === 'select-action' && (
            <ActionGrid onSelect={chooseAction} />
          )}

          {step === 'parameters' && selectedAction && (
            <ActionParameters
              action={ACTIONS.find((item) => item.action === selectedAction)}
              reason={reason}
              onReason={setReason}
              isWorking={isWorking}
              onBack={() => setStep('select-action')}
              onSubmit={createPlan}
            />
          )}

          {step === 'preview' && (
            <RemediationPreview
              job={activeJob}
              decisionNote={decisionNote}
              disabled={isWorking}
              onDecisionNote={setDecisionNote}
              onDecision={decidePlan}
              onStartOver={() => {
                setActiveJob(null);
                setSelectedAction(null);
                setStep('select-action');
              }}
            />
          )}

          <RemediationHistory jobs={jobs} onOpen={(job) => {
            setActiveJob(job);
            setStep('preview');
          }} />
        </div>
      </aside>
    </div>
  );
}

function ActionGrid({ onSelect }) {
  return (
    <div className="action-grid-wrap">
      <div className="action-grid-heading">
        <span>✂ Select Remediation Action</span>
        <p>Choose one action below to apply to the selected finding(s).</p>
      </div>

      <div className="action-grid">
        {ACTIONS.map((item) => (
          <div
            key={item.action}
            className={`action-card ${item.danger ? 'danger' : ''}`}
          >
            <i aria-hidden="true">{item.icon}</i>
            <h3>{item.title}</h3>
            <p>{item.description}</p>
            <button type="button" onClick={() => onSelect(item.action)}>
              Select Action
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

function ActionParameters({ action, reason, onReason, isWorking, onBack, onSubmit }) {
  return (
    <div className="action-parameters">
      <button type="button" className="drawer-back" onClick={onBack}>
        ← Change action
      </button>

      <div className="action-parameters__selected">
        <i aria-hidden="true">{action.icon}</i>
        <div>
          <strong>{action.title}</strong>
          <small>{action.description}</small>
        </div>
      </div>

      <span className="field-label">⚙ Action Parameters</span>
      <p className="muted">Sent to the backend along with the selected action.</p>

      <label htmlFor="remediation-reason">Business reason</label>
      <textarea
        id="remediation-reason"
        rows="3"
        value={reason}
        maxLength="1000"
        onChange={(event) => onReason(event.target.value)}
      />

      <button
        type="button"
        className="plan-remediation"
        disabled={isWorking}
        onClick={onSubmit}
      >
        {isWorking ? 'Preparing…' : 'Generate AI plan'}
      </button>
    </div>
  );
}

function RemediationPreview({
  job,
  decisionNote,
  disabled,
  onDecisionNote,
  onDecision,
  onStartOver,
}) {
  if (!job) {
    return (
      <div className="remediation-preview empty">
        <span>AI plan preview</span>
        <strong>Generating…</strong>
      </div>
    );
  }

  const awaitingApproval = job.status === 'awaiting_approval';

  return (
    <div className="remediation-preview">
      <button type="button" className="drawer-back" onClick={onStartOver}>
        ← Choose a different action
      </button>

      <div className="preview-status-row">
        <span>Plan #{job.id}</span>
        <strong className={`job-status ${job.status}`}>{job.status}</strong>
      </div>

      <h3>{job.action.toUpperCase()} recommendation</h3>
      <p>{job.planner_output?.reason}</p>

      <div className="preview-facts">
        <div>
          <span>Confidence</span>
          <strong>
            {Math.round(Number(job.planner_output?.confidence || 0) * 100)}%
          </strong>
        </div>
        <div>
          <span>Affected findings</span>
          <strong>{job.preview?.affected_findings || 0}</strong>
        </div>
        <div>
          <span>Planner</span>
          <strong>{job.planner_output?.planner_source || 'bounded'}</strong>
        </div>
      </div>

      <ul className="safety-list">
        {(job.planner_output?.safety_controls || []).map((control) => (
          <li key={control}>✓ {control.replaceAll('_', ' ')}</li>
        ))}
      </ul>

      {job.error && <div className="remediation-error">{job.error}</div>}

      {awaitingApproval && (
        <>
          <span className="field-label">📝 Notes</span>
          <label htmlFor="decision-note">Approval note</label>
          <textarea
            id="decision-note"
            rows="3"
            value={decisionNote}
            onChange={(event) => onDecisionNote(event.target.value)}
          />

          {job.admin_required && (
            <p className="admin-warning">Delete requires an administrator.</p>
          )}

          <div className="decision-actions">
            <button
              type="button"
              disabled={disabled || decisionNote.trim().length < 3}
              onClick={() => onDecision(true)}
            >
              Approve and execute
            </button>
            <button
              type="button"
              className="reject"
              disabled={disabled || decisionNote.trim().length < 3}
              onClick={() => onDecision(false)}
            >
              Reject
            </button>
          </div>
        </>
      )}

      {job.status === 'completed' && (
        <div className="verification-success">
          ✓ Completed and verified
          {job.result?.replacements > 0
            ? ` · ${job.result.replacements} values changed`
            : ''}
        </div>
      )}
    </div>
  );
}

function RemediationHistory({ jobs, onOpen }) {
  if (jobs.length === 0) {
    return null;
  }

  return (
    <div className="remediation-history">
      <h3>Remediation history</h3>
      <div>
        {jobs.map((job) => (
          <button key={job.id} type="button" onClick={() => onOpen(job)}>
            <span>
              <strong>#{job.id} · {job.action}</strong>
              <small>{job.preview?.file_name || job.file_path}</small>
            </span>
            <i className={`job-status ${job.status}`}>{job.status}</i>
          </button>
        ))}
      </div>
    </div>
  );
} 