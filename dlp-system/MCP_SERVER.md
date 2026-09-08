# SentinelDLP MCP Server

Exposes read-only DLP scanning to any MCP client (Claude Desktop, Claude
Code, etc.) as tools. See the safety-boundary comment at the top of
`mcp_server.py` before adding any new tool here.

## Tools exposed

| Tool | What it does |
|---|---|
| `list_assets` | List registered scan targets (no credentials/data) |
| `discover_schema` | List tables/columns for a database asset (structure only) |
| `scan_database` | Scan a registered DATABASE asset (MySQL/MSSQL/SQLite); returns a masked risk summary |
| `scan_system` | Scan a registered filesystem asset (Windows/Linux); returns a masked risk summary |
| `get_scan_status` | Poll a scan's status and masked risk summary |

**Not exposed, on purpose:** anything from the remediation API (mask,
redact, encrypt, delete). Those stay behind the web app's human-approval
flow. See the module docstring in `mcp_server.py` for why.

Every finding-returning tool strips raw PII values -- only entity-type
counts and risk levels cross the MCP boundary, same as this project's
existing `ScanMemoryStore` summaries.

## Run it standalone (sanity check)

```bash
cd dlp-system
pip install -r requirements.txt
python mcp_server.py
```

It should sit and wait on stdio -- that's correct, it's waiting for an
MCP client to connect. Ctrl+C to stop.

## Connect Claude Desktop

Add this to Claude Desktop's MCP config file (Settings -> Developer ->
Edit Config, or the `claude_desktop_config.json` file directly):

```json
{
  "mcpServers": {
    "sentineldlp": {
      "command": "python",
      "args": ["/absolute/path/to/dlp-system/mcp_server.py"]
    }
  }
}
```

Use the absolute path to `mcp_server.py` on your machine, and make sure
the `python` on your PATH (or give a full interpreter path instead) has
this project's dependencies installed. Restart Claude Desktop after
saving.

Then in a new conversation: "what scan targets do we have registered?"
or "scan asset 1 for PII" should trigger these tools.

## Notes

- Runs with `SKIP_AUTH=true` semantics (see `.env.example`) -- every call
  uses the same shared dev user the rest of the app uses in that mode.
  Don't point this at a production database until real auth/authorization
  is wired back in for this entrypoint too.
- Creates its own DB tables on first run if they don't exist yet (same
  models as the FastAPI app, same DATABASE_URL).
