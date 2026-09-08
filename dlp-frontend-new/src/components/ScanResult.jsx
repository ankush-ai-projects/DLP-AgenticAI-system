import { useCallback, useEffect, useMemo, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

import { apiClient, formatApiError } from '../api/client';
import RemediationWorkspace from './RemediationWorkspace';
import './ScanResult.css';

function groupFindingsByEntity(findings) {
  return findings.reduce((counts, finding) => {
    const entityType = finding.entity_type || 'UNKNOWN';
    counts[entityType] = (counts[entityType] || 0) + 1;
    return counts;
  }, {});
}

export default function ScanResult() {
  const { scanId } = useParams();
  const navigate = useNavigate();

  const [scan, setScan] = useState(null);
  const [error, setError] = useState('');
  const [isReviewing, setIsReviewing] = useState(false);
  const [selectedIndexes, setSelectedIndexes] = useState(() => new Set());
  const [isRemediationOpen, setIsRemediationOpen] = useState(false);

  const loadScan = useCallback(async () => {
    const response = await apiClient.get(`/api/v1/agentic-scans/${scanId}`);
    setScan(response.data);
  }, [scanId]);

  useEffect(() => {
    let isMounted = true;

    loadScan().catch((requestError) => {
      if (isMounted) {
        setError(formatApiError(requestError));
      }
    });

    return () => {
      isMounted = false;
    };
  }, [loadScan]);

  const handleReview = async (approved) => {
    setIsReviewing(true);
    setError('');

    try {
      await apiClient.post(`/api/v1/agentic-scans/${scanId}/review`, {
        approved,
        note: approved
          ? 'Approved from the scan result page'
          : 'Rejected from the scan result page',
      });

      await loadScan();
    } catch (requestError) {
      setError(formatApiError(requestError));
    } finally {
      setIsReviewing(false);
    }
  };

  if (!scan && !error) {
    return (
      <main className="scan-result-page">
        <div className="result-loading">Loading scan report…</div>
      </main>
    );
  }

  const workflowState = scan?.workflow_state || {};
  const findings =
    workflowState.verified_findings || workflowState.findings || [];
  const entityCounts = groupFindingsByEntity(findings);

  return (
    <main className="scan-result-page">
      <header className="result-header">
        <div className="result-header__title">
          <button type="button" onClick={() => navigate('/scan-status')}>
            ← Scan Status
          </button>

          <div>
            <h1>Scan Result</h1>
            <p>Scan ID {scanId} · LangGraph Agentic workflow</p>
          </div>
        </div>

        {scan && (
          <span className={`result-status ${scan.status}`}>
            {scan.status.replaceAll('_', ' ')}
          </span>
        )}
      </header>

      {error && (
        <div className="result-error" role="alert">
          {error}
        </div>
      )}

      {scan && (
        <>
          <ResultMetrics
            findings={findings}
            scanStats={workflowState.scan_stats}
            riskSummary={workflowState.risk_summary}
          />

          {scan.approval_required && (
            <ApprovalBanner
              disabled={isReviewing}
              onDecision={handleReview}
            />
          )}

          <section className="result-layout">
            <FindingSummary entityCounts={entityCounts} />
          </section>

          <FindingsTable
            findings={findings}
            host={workflowState.asset?.host || workflowState.asset?.name || 'Unknown'}
            selectedIndexes={selectedIndexes}
            onToggleRow={(index, path) => {
              setSelectedIndexes((current) => {
                const next = new Set(current);
                if (next.has(index)) {
                  next.delete(index);
                  return next;
                }
                // Remediation runs against one file at a time (the
                // backend job is created per file_path), so selecting a
                // row from a different file than what's already picked
                // starts a fresh selection instead of mixing files.
                const selectedPaths = new Set(
                  [...current].map((i) => findings[i]?.location?.path),
                );
                if (selectedPaths.size > 0 && !selectedPaths.has(path)) {
                  return new Set([index]);
                }
                next.add(index);
                return next;
              });
            }}
            onOpenRemediation={() => setIsRemediationOpen(true)}
          />

          {isRemediationOpen && (
            <RemediationWorkspace
              scanId={Number(scanId)}
              findings={findings}
              preselectedIndexes={[...selectedIndexes]}
              onClose={() => {
                setIsRemediationOpen(false);
                setSelectedIndexes(new Set());
              }}
            />
          )}

          {workflowState.errors?.length > 0 && (
            <section className="result-panel">
              <h2>Failed or skipped items</h2>
              <pre>{JSON.stringify(workflowState.errors, null, 2)}</pre>
            </section>
          )}
        </>
      )}
    </main>
  );
}

function ResultMetrics({ findings, scanStats = {}, riskSummary = {} }) {
  const scannedItems =
    scanStats.files_scanned ?? scanStats.tables_scanned ?? 0;

  return (
    <section className="result-metrics" aria-label="Scan result summary">
      <Metric label="Total findings" value={findings.length} />
      <Metric label="Scanned files / tables" value={scannedItems} />
      <Metric
        label="Scanned content"
        value={formatBytes(scanStats.bytes_scanned ?? 0)}
      />
      <Metric label="Failed items" value={scanStats.files_failed ?? 0} />
      <Metric label="Risk level" value={riskSummary.risk_level || '—'} />
    </section>
  );
}

function formatBytes(value) {
  const bytes = Number(value || 0);

  if (!Number.isFinite(bytes) || bytes <= 0) {
    return '0 B';
  }

  const units = ['B', 'KB', 'MB', 'GB', 'TB'];
  const unitIndex = Math.min(
    Math.floor(Math.log(bytes) / Math.log(1024)),
    units.length - 1,
  );
  const size = bytes / 1024 ** unitIndex;

  return `${size >= 10 || unitIndex === 0 ? size.toFixed(0) : size.toFixed(1)} ${
    units[unitIndex]
  }`;
}

function Metric({ label, value }) {
  return (
    <div>
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function ApprovalBanner({ disabled, onDecision }) {
  return (
    <section className="approval-banner">
      <div>
        <strong>Analyst review required</strong>
        <p>
          Critical findings need a human decision before the workflow can
          finish.
        </p>
      </div>

      <div className="approval-actions">
        <button
          type="button"
          disabled={disabled}
          onClick={() => onDecision(true)}
        >
          Approve
        </button>
        <button
          type="button"
          className="reject"
          disabled={disabled}
          onClick={() => onDecision(false)}
        >
          Reject
        </button>
      </div>
    </section>
  );
}

function FindingSummary({ entityCounts }) {
  const entries = Object.entries(entityCounts);

  return (
    <section className="result-panel">
      <h2>Finding summary</h2>

      {entries.length === 0 ? (
        <p className="muted">No verified findings.</p>
      ) : (
        <div className="entity-list">
          {entries.map(([entityType, count]) => (
            <div key={entityType}>
              <span>{entityType.replaceAll('_', ' ')}</span>
              <strong>{count}</strong>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

function AgentPlan({ plan = {} }) {
  return (
    <section className="result-panel">
      <h2>Agent plan</h2>

      <div className="tool-flow">
        {(plan.tools || []).map((tool, index) => (
          <span key={tool}>
            {index + 1}. {tool.replaceAll('_', ' ')}
          </span>
        ))}
      </div>

      <p className="planner-source">
        Planner: {plan.planner_source || 'unknown'}
      </p>
    </section>
  );
}

function FindingsTable({
  findings,
  host,
  selectedIndexes,
  onToggleRow,
  onOpenRemediation,
}) {
  const selectedCount = selectedIndexes.size;
  const visibleFindings = findings.slice(0, 250);
  const allVisibleSelected =
    visibleFindings.length > 0 &&
    visibleFindings.every((_, index) => selectedIndexes.has(index));

  const toggleSelectAllVisible = () => {
    if (allVisibleSelected) {
      visibleFindings.forEach((_, index) => {
        if (selectedIndexes.has(index)) onToggleRow(index, visibleFindings[index]?.location?.path);
      });
      return;
    }
    // Selecting "all" only makes sense within a single file (see the
    // one-file-at-a-time note in ScanResult) -- so this only selects the
    // rows that belong to the first visible file.
    const firstPath = visibleFindings[0]?.location?.path;
    visibleFindings.forEach((finding, index) => {
      if (finding.location?.path === firstPath && !selectedIndexes.has(index)) {
        onToggleRow(index, firstPath);
      }
    });
  };

  return (
    <section className="result-panel findings-panel">
      <div className="findings-toolbar">
        <h2>Detected data</h2>
        <button
          type="button"
          className="remediation-trigger"
          disabled={selectedCount === 0}
          onClick={onOpenRemediation}
        >
          🛡 Remediation{selectedCount > 0 ? ` (${selectedCount})` : ''}
        </button>
      </div>

      {findings.length === 0 ? (
        <p className="muted">No sensitive data was detected.</p>
      ) : (
        <div className="findings-table">
          <table>
            <thead>
              <tr>
                <th className="select-col">
                  <input
                    type="checkbox"
                    checked={allVisibleSelected}
                    onChange={toggleSelectAllVisible}
                    aria-label="Select all rows for the first file"
                  />
                </th>
                <th>S.No</th>
                <th>Host</th>
                <th>Data Type</th>
                <th>Detected Data</th>
                <th>Data Location</th>
              </tr>
            </thead>

            <tbody>
              {visibleFindings.map((finding, index) => (
                <FindingRow
                  key={`${finding.entity_type}-${index}`}
                  index={index}
                  serial={index + 1}
                  host={host}
                  finding={finding}
                  selected={selectedIndexes.has(index)}
                  onToggle={onToggleRow}
                />
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}

const ENTITY_CATEGORY = {
  CREDIT_CARD: 'PCI',
  AADHAAR: 'PII',
  PAN: 'PII',
  EMAIL: 'PII',
  PHONE: 'PII',
  PERSON: 'PII',
  ADDRESS: 'PII',
};

function FindingRow({ index, serial, host, finding, selected, onToggle }) {
  const source =
    finding.location?.path || finding.location?.table || 'Unavailable';
  const category = ENTITY_CATEGORY[finding.entity_type] || 'PII';

  return (
    <tr className={selected ? 'row-selected' : ''}>
      <td className="select-col">
        <input
          type="checkbox"
          checked={selected}
          onChange={() => onToggle(index, finding.location?.path)}
          aria-label={`Select finding ${serial}`}
        />
      </td>
      <td>{serial}</td>
      <td>{host}</td>
      <td>
        <span className={`data-type-badge ${category.toLowerCase()}`}>
          {category}
        </span>
        <span className="risk-mini" title={`Risk: ${finding.risk_level || 'unknown'}`}>
          {finding.entity_type?.replaceAll('_', ' ')}
        </span>
      </td>
      <td>
        <code>{finding.masked_value}</code>
      </td>
      <td>{source}</td>
    </tr>
  );
} 