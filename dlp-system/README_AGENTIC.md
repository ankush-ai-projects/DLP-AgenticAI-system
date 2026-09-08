# SentinelDLP AI – Implementation Guide

This codebase contains a bounded multi-agent DLP workflow for MySQL, MSSQL, SQLite demo databases, and allowlisted Windows/Linux filesystem paths.

## Implemented

- FastAPI asset and agentic-scan APIs
- MySQL, MSSQL, and read-only SQLite connectors
- Schema discovery, column prioritization, batching, and masking
- Windows/Linux-compatible endpoint scanner CLI
- Regex + optional spaCy NER + Luhn validation
- Supervisor, Planner, Database, System, Critic, Risk/Policy, and Reporting agents
- Optional OpenAI-compatible planning with deterministic fallback
- LangGraph is the default orchestration runtime (not an optional wrapper)
- Durable SQLite/PostgreSQL checkpoints with one `thread_id` per scan
- Native `interrupt()` / `Command(resume=...)` human approval flow
- Conditional routing, bounded retries, re-planning, and terminal failure state
- Persistent scan state, findings, agent runs, reviews, and audit events
- Celery/Redis background execution
- Policy retrieval with citations
- Detection and agent unit tests
- Docker Compose and React Agentic Scan Console

## Quick start

```bash
cd dlp-system
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8001
```

Local mode writes LangGraph checkpoints to `./langgraph_checkpoints.sqlite`.
When `DATABASE_URL` is PostgreSQL, `LANGGRAPH_CHECKPOINTER=auto` selects the
PostgreSQL checkpointer. You can set `LANGGRAPH_POSTGRES_URL` explicitly when
the application and checkpoint databases differ.

The planner uses an OpenAI-compatible model only when `LLM_API_KEY` and
`LLM_MODEL` are configured. Without them, the graph remains fully active but
uses the validated deterministic planning fallback.

Frontend:

```bash
cd ../dlp-frontend-new
npm install
npm run dev
```

Open API documentation at `http://localhost:8001/docs` or the UI at the Vite URL.

## Configure a database credential

Asset records store only `secret_ref`. Configure its JSON value in the runtime environment:

```bash
export DLP_SECRET_PAYMENTS_MSSQL='{"username":"readonly_user","password":"replace-me"}'
```

Use a real secret manager in production. Never commit credentials.

## Run tests

```bash
pytest -q
python -m compileall -q app endpoint_agent tests
```

## Endpoint scan

```bash
python -m endpoint_agent.main scan \
  --path ./test_data \
  --allowed-root ./test_data \
  --output scan-result.json
```

The output contains masked findings only.

## Development order

1. Run and fix all tests.
2. Validate SQLite demo scanning.
3. Validate MySQL with a read-only test user.
4. Validate MSSQL with `ApplicationIntent=ReadOnly` and the Microsoft ODBC driver.
5. Validate Windows/Linux allowlisted scans.
6. Configure an LLM and compare its plan with the deterministic fallback.
7. Run human-review scenarios.
8. Record MLflow metrics and agent traces.
9. Run Docker Compose and the React demo.
10. Publish measured results only after independent evaluation.

See `Agentic_DLP_README.md` in the project package for the full interview-oriented roadmap.
