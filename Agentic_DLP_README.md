# SentinelDLP AI Project Workflow

This repository follows a bounded, production-oriented Agentic AI design for database and Windows/Linux system scanning.

## Runtime workflow

```text
User goal
-> LangGraph planner node
-> Database or System specialist node
-> Hybrid Detection
-> Critic verification node
-> Deterministic Risk and Policy node
-> LangGraph interrupt when critical
-> Command(resume=decision) on the same checkpoint
-> Grounded report node
-> Audit, metrics, and persistent state
```

## Build checklist

| Milestone | Code status | Required validation |
| --- | --- | --- |
| Clean models, configuration, RBAC foundation | Implemented | API and tenant-isolation tests |
| MySQL/MSSQL/SQLite connectors | Implemented | Test against read-only databases |
| Windows/Linux allowlisted scanning | Implemented | Test endpoint CLI on both operating systems |
| Hybrid PII/PCI detection | Implemented | Independent precision/recall/F1 evaluation |
| Celery/Redis distributed execution | Implemented | Worker failure and retry test |
| Multi-agent runtime | Implemented | Goal-routing and bounded-loop tests |
| LangGraph durable runtime | Default API/worker runtime | Checkpoint and interrupt integration test |
| Human review and audit | Implemented | Approval/rejection API test |
| Policy retrieval and cited reports | Implemented locally | Retrieval evaluation; pgvector production adapter |
| MLOps and observability hooks | Implemented | MLflow/Prometheus deployment validation |
| React scan console and Docker | Implemented | Clean-machine end-to-end test |

## Development rule

Do not claim a milestone is production-ready until its validation passes. Work in small vertical slices:

```text
Choose one acceptance criterion
-> implement or configure
-> add automated test
-> run security checks
-> record measured result
-> update documentation
```

## Next required action

Install dependencies and run the complete test suite. Then execute one SQLite demo, one MySQL scan, one MSSQL scan, one Windows path scan, and one Linux path scan. Record failures and measured performance before adding more features.
