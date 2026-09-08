import { useCallback, useEffect, useRef, useState } from 'react';
import {
  useLocation,
  useNavigate,
  useSearchParams,
} from 'react-router-dom';
import { apiClient, formatApiError } from '../api/client';
import './ScanStatus.css';

const SCAN_HISTORY_KEY = 'dlp_scan_history';
const CONSUMED_LAUNCHES_KEY = 'dlp_consumed_scan_launches';
const MAX_HISTORY_ITEMS = 25;
const MAX_CONSUMED_LAUNCHES = 50;
const MAX_ESTIMATED_PROGRESS = 98;
const POLL_INTERVAL_MS = 1500;

const TERMINAL_STATUSES = new Set([
  'completed',
  'partially_completed',
  'awaiting_review',
  'failed',
  'cancelled',
]);

const STATUS_STAGE_PROGRESS = {
  created: 4,
  planning: 12,
  connecting: 22,
  discovering: 35,
  scanning: 55,
  verifying: 76,
  risk_analysis: 86,
  reporting: 95,
};

const STATUS_METADATA = {
  scanning: {
    icon: '⏳',
    label: 'Scanning',
    tone: 'amber',
  },
  completed: {
    icon: '✓',
    label: 'Completed',
    tone: 'green',
  },
  partially_completed: {
    icon: '◐',
    label: 'Partially completed',
    tone: 'blue',
  },
  awaiting_review: {
    icon: 'Ⅱ',
    label: 'Review required',
    tone: 'purple',
  },
  failed: {
    icon: '×',
    label: 'Failed',
    tone: 'red',
  },
  cancelled: {
    icon: '×',
    label: 'Cancelled',
    tone: 'red',
  },
};

function normalizeStoredScan(scan) {
  if (scan.status === 'scanning' && !scan.scanId) {
    return {
      ...scan,
      status: 'failed',
      progress: 100,
      error: 'Scan start was interrupted before the server returned a scan ID.',
    };
  }

  return scan;
}

function readScanHistory() {
  try {
    const storedValue = JSON.parse(
      localStorage.getItem(SCAN_HISTORY_KEY) || '[]',
    );

    return Array.isArray(storedValue)
      ? storedValue.map(normalizeStoredScan)
      : [];
  } catch {
    localStorage.removeItem(SCAN_HISTORY_KEY);
    return [];
  }
}

function consumeLaunch(launchId) {
  if (!launchId) {
    return false;
  }

  try {
    const consumedLaunches = JSON.parse(
      sessionStorage.getItem(CONSUMED_LAUNCHES_KEY) || '[]',
    );
    const launchIds = Array.isArray(consumedLaunches) ? consumedLaunches : [];

    if (launchIds.includes(launchId)) {
      return false;
    }

    sessionStorage.setItem(
      CONSUMED_LAUNCHES_KEY,
      JSON.stringify([launchId, ...launchIds].slice(0, MAX_CONSUMED_LAUNCHES)),
    );
    return true;
  } catch {
    return true;
  }
}

function persistScanHistory(history) {
  localStorage.setItem(
    SCAN_HISTORY_KEY,
    JSON.stringify(history.slice(0, MAX_HISTORY_ITEMS)),
  );
}

function countFindings(summary) {
  const entityCounts =
    summary?.entity_counts ||
    summary?.by_entity ||
    summary?.by_entity_type ||
    summary?.risk?.by_entity ||
    {};

  return Object.values(entityCounts).reduce(
    (total, count) => total + Number(count || 0),
    0,
  );
}

function countResultFindings(result) {
  const workflowState = result.workflow_state || {};
  const verifiedFindings = workflowState.verified_findings;
  const detectedFindings = workflowState.findings;
  const reportFindings = workflowState.report?.findings;

  if (Array.isArray(verifiedFindings) && verifiedFindings.length > 0) {
    return verifiedFindings.length;
  }

  if (Array.isArray(detectedFindings) && detectedFindings.length > 0) {
    return detectedFindings.length;
  }

  if (Array.isArray(reportFindings) && reportFindings.length > 0) {
    return reportFindings.length;
  }

  const numericTotals = [
    workflowState.risk_summary?.total_findings,
    workflowState.scan_stats?.findings_detected,
    result.summary?.total_findings,
    result.summary?.risk?.total_findings,
    result.summary?.total,
  ];

  const knownTotal = numericTotals.find(
    (value) => value !== undefined && value !== null,
  );

  if (knownTotal !== undefined) {
    return Number(knownTotal) || 0;
  }

  return Math.max(
    countFindings(workflowState.risk_summary),
    countFindings(result.summary),
  );
}

function firstMetricValue(...values) {
  const value = values.find((candidate) => {
    if (candidate === undefined || candidate === null || candidate === '') {
      return false;
    }

    return Number.isFinite(Number(candidate));
  });

  return value === undefined ? null : Math.max(0, Number(value));
}

function getResultFindings(result) {
  const workflowState = result.workflow_state || {};

  return [
    workflowState.verified_findings,
    workflowState.findings,
    workflowState.report?.findings,
    result.findings,
  ].find(Array.isArray) || [];
}

function getUniqueLocationMetrics(findings) {
  const files = new Map();
  const tables = new Set();

  findings.forEach((finding) => {
    const location = finding?.location || {};
    const filePath =
      location.path ||
      location.file_path ||
      finding.file_path ||
      finding.path;
    const tableName =
      location.table ||
      location.table_name ||
      finding.table ||
      finding.table_name;

    if (filePath) {
      const fileSize = firstMetricValue(
        location.size_bytes,
        location.file_size_bytes,
        finding.size_bytes,
        finding.file_size_bytes,
      );

      if (!files.has(filePath) || files.get(filePath) === null) {
        files.set(filePath, fileSize);
      }
    }

    if (tableName) {
      tables.add(tableName);
    }
  });

  const knownFileSizes = [...files.values()].filter(
    (size) => size !== null,
  );

  return {
    filesScanned: files.size || null,
    bytesScanned:
      knownFileSizes.length === files.size && files.size > 0
        ? knownFileSizes.reduce((total, size) => total + size, 0)
        : null,
    tablesScanned: tables.size || null,
  };
}

function extractScanActivity(result, assetType, previousActivity = {}) {
  const workflowState = result.workflow_state || {};
  const scanStats = workflowState.scan_stats || result.scan_stats || {};
  const summary = result.summary || workflowState.summary || {};
  const discoveredFiles =
    workflowState.discovered_files || result.discovered_files;
  const discoveredTables =
    workflowState.discovered_tables || result.discovered_tables;
  const locationMetrics = getUniqueLocationMetrics(getResultFindings(result));

  const filesScanned = firstMetricValue(
    scanStats.files_scanned,
    scanStats.files_processed,
    scanStats.processed_files,
    summary.files_scanned,
    Array.isArray(discoveredFiles) ? discoveredFiles.length : null,
    locationMetrics.filesScanned,
    previousActivity.filesScanned,
  );
  const totalFiles = firstMetricValue(
    scanStats.total_files,
    scanStats.files_total,
    summary.total_files,
    previousActivity.totalFiles,
  );
  const bytesScanned = firstMetricValue(
    scanStats.bytes_scanned,
    scanStats.bytes_processed,
    scanStats.processed_bytes,
    scanStats.data_scanned_bytes,
    summary.bytes_scanned,
    summary.data_scanned_bytes,
    locationMetrics.bytesScanned,
    previousActivity.bytesScanned,
  );
  const totalBytes = firstMetricValue(
    scanStats.total_bytes,
    scanStats.bytes_total,
    summary.total_bytes,
    previousActivity.totalBytes,
  );
  const tablesScanned = firstMetricValue(
    scanStats.tables_scanned,
    scanStats.tables_processed,
    summary.tables_scanned,
    Array.isArray(discoveredTables) ? discoveredTables.length : null,
    locationMetrics.tablesScanned,
    previousActivity.tablesScanned,
  );
  const totalTables = firstMetricValue(
    scanStats.total_tables,
    scanStats.tables_total,
    summary.total_tables,
    previousActivity.totalTables,
  );
  const rowsScanned = firstMetricValue(
    scanStats.rows_scanned,
    scanStats.rows_processed,
    scanStats.processed_rows,
    summary.rows_scanned,
    previousActivity.rowsScanned,
  );

  return {
    type: assetType,
    filesScanned,
    totalFiles,
    bytesScanned,
    totalBytes,
    tablesScanned,
    totalTables,
    rowsScanned,
  };
}

function formatCount(processed, total) {
  if (processed === null || processed === undefined) {
    return '—';
  }

  const processedLabel = Number(processed).toLocaleString();

  return total !== null && total !== undefined && total >= processed
    ? `${processedLabel} / ${Number(total).toLocaleString()}`
    : processedLabel;
}

function formatBytes(bytes, totalBytes) {
  const formatSingleValue = (value) => {
    if (value === null || value === undefined) {
      return '—';
    }

    if (value === 0) {
      return '0 B';
    }

    const units = ['B', 'KB', 'MB', 'GB', 'TB'];
    const unitIndex = Math.min(
      Math.floor(Math.log(value) / Math.log(1024)),
      units.length - 1,
    );
    const amount = value / 1024 ** unitIndex;

    return `${amount.toFixed(amount >= 10 || unitIndex === 0 ? 0 : 2)} ${units[unitIndex]}`;
  };

  const processedLabel = formatSingleValue(bytes);

  return totalBytes !== null && totalBytes !== undefined && totalBytes >= bytes
    ? `${processedLabel} / ${formatSingleValue(totalBytes)}`
    : processedLabel;
}


function getBackendProgress(result) {
  const scanProgress = Number(
    result.workflow_state?.scan_stats?.progress_percent,
  );

  if (!Number.isFinite(scanProgress)) {
    return 0;
  }

  // File/table scanning occupies the middle portion of the full workflow.
  return Math.min(75, 35 + Math.round(scanProgress * 0.4));
}

function calculateEstimatedProgress(elapsedSeconds) {
  return Math.min(
    MAX_ESTIMATED_PROGRESS,
    8 + Math.floor(elapsedSeconds * 2.2),
  );
}

function calculateStatusCounts(history) {
  return history.reduce(
    (counts, scan) => {
      counts.all += 1;

      if (scan.status === 'scanning') counts.scanning += 1;
      if (scan.status === 'completed') counts.completed += 1;
      if (scan.status === 'partially_completed') counts.partial += 1;
      if (scan.status === 'awaiting_review') counts.review += 1;
      if (scan.status === 'failed' || scan.status === 'cancelled') {
        counts.failed += 1;
      }

      return counts;
    },
    {
      all: 0,
      scanning: 0,
      completed: 0,
      partial: 0,
      review: 0,
      failed: 0,
    },
  );
}

function getScanAssetType(scan) {
  if (scan.assetType === 'system' || scan.assetType === 'database') {
    return scan.assetType;
  }

  return ['windows', 'linux'].includes(
    String(scan.platform || '').toLowerCase(),
  )
    ? 'system'
    : 'database';
}

export default function ScanStatus() {
  const navigate = useNavigate();
  const location = useLocation();
  const [searchParams] = useSearchParams();
  const requestedReportType = searchParams.get('reports');
  const reportType = ['system', 'database'].includes(requestedReportType)
    ? requestedReportType
    : null;
  const hasStartedScan = useRef(false);
  const scanHistoryRef = useRef([]);
  const refreshedTerminalScanIds = useRef(new Set());

  const [scanHistory, setScanHistory] = useState(readScanHistory);
  const [error, setError] = useState('');
  const [downloadingScanId, setDownloadingScanId] = useState(null);

  const updateScan = useCallback((localId, changes) => {
    setScanHistory((currentHistory) => {
      const updatedHistory = currentHistory.map((scan) =>
        scan.localId === localId ? { ...scan, ...changes } : scan,
      );

      persistScanHistory(updatedHistory);
      return updatedHistory;
    });
  }, []);

  useEffect(() => {
    scanHistoryRef.current = scanHistory;
  }, [scanHistory]);

  useEffect(() => {
    const scanState = location.state;
    const launchId = scanState?.launchId || location.key;

    if (
      !scanState?.startScan ||
      hasStartedScan.current ||
      !consumeLaunch(launchId)
    ) {
      return undefined;
    }

    hasStartedScan.current = true;

    const localId = `launch-${launchId}`;
    const startedAt = Date.now();
    const asset = scanState.asset || {};

    const pendingScan = {
      localId,
      scanId: null,
      assetName: asset.name || `Asset ${scanState.request.asset_id}`,
      assetType: asset.asset_type || getScanAssetType(asset),
      platform: asset.platform || 'system',
      status: 'scanning',
      progress: 4,
      startedAt: new Date(startedAt).toISOString(),
      durationSeconds: 0,
      goal: scanState.request.goal,
      dataFound: 0,
      activity: {
        type: asset.asset_type || getScanAssetType(asset),
        filesScanned: null,
        totalFiles: null,
        bytesScanned: null,
        totalBytes: null,
        tablesScanned: null,
        totalTables: null,
        rowsScanned: null,
      },
      error: null,
      approvalRequired: false,
    };

    setScanHistory((currentHistory) => {
      const updatedHistory = [pendingScan, ...currentHistory];
      persistScanHistory(updatedHistory);
      return updatedHistory;
    });

    let isCancelled = false;

    const startScan = async () => {
      try {
        const startResponse = await apiClient.post(
          '/api/v1/agentic-scans',
          scanState.request,
          {
            headers: {
              'X-Scan-Launch-Id': launchId,
            },
          },
        );
        const result = startResponse.data;

        if (isCancelled) {
          return;
        }

        updateScan(localId, {
          scanId: result.scan_id,
          status: TERMINAL_STATUSES.has(result.status)
            ? result.status
            : 'scanning',
          progress: TERMINAL_STATUSES.has(result.status) ? 100 : 4,
          dataFound: TERMINAL_STATUSES.has(result.status)
            ? countResultFindings(result)
            : 0,
          activity: extractScanActivity(
            result,
            pendingScan.assetType,
            pendingScan.activity,
          ),
          error: result.error || null,
          approvalRequired: result.approval_required,
        });
      } catch (requestError) {
        if (requestError.response?.status === 401) {
          // Handled globally by apiClient's response interceptor.
          return;
        }

        const message = formatApiError(requestError);

        updateScan(localId, {
          status: 'failed',
          progress: 100,
          durationSeconds: Math.max(
            1,
            Math.floor((Date.now() - startedAt) / 1000),
          ),
          error: message,
        });

        setError(message);
      }
    };

    startScan();

    return () => {
      isCancelled = true;
    };
  }, [location.key, location.state, updateScan]);

  useEffect(() => {
    const progressTimer = window.setInterval(() => {
      setScanHistory((currentHistory) => {
        let hasActiveScan = false;

        const updatedHistory = currentHistory.map((scan) => {
          if (scan.status !== 'scanning') {
            return scan;
          }

          hasActiveScan = true;
          const startedAt = new Date(scan.startedAt).getTime();
          const elapsedSeconds = Number.isFinite(startedAt)
            ? Math.max(0, Math.floor((Date.now() - startedAt) / 1000))
            : scan.durationSeconds || 0;

          return {
            ...scan,
            progress: Math.max(
              scan.progress || 0,
              calculateEstimatedProgress(elapsedSeconds),
            ),
            durationSeconds: elapsedSeconds,
          };
        });

        if (!hasActiveScan) {
          return currentHistory;
        }

        persistScanHistory(updatedHistory);
        return updatedHistory;
      });
    }, 1000);

    return () => {
      window.clearInterval(progressTimer);
    };
  }, []);

  useEffect(() => {
    let isCancelled = false;
    let isPolling = false;

    const pollActiveScans = async () => {
      if (isPolling || isCancelled) {
        return;
      }

      const activeScans = scanHistoryRef.current.filter((scan) => {
        if (!scan.scanId) {
          return false;
        }

        if (scan.status === 'scanning') {
          return true;
        }

        const needsTerminalRefresh =
          TERMINAL_STATUSES.has(scan.status) &&
          Number(scan.dataFound || 0) === 0 &&
          !refreshedTerminalScanIds.current.has(scan.scanId);

        if (needsTerminalRefresh) {
          refreshedTerminalScanIds.current.add(scan.scanId);
        }

        return needsTerminalRefresh;
      });

      if (activeScans.length === 0) {
        return;
      }

      isPolling = true;

      await Promise.allSettled(
        activeScans.map(async (scan) => {
          try {
            const response = await apiClient.get(
              `/api/v1/agentic-scans/${scan.scanId}`,
            );
            const result = response.data;

            if (!isCancelled) {
              const isTerminal = TERMINAL_STATUSES.has(result.status);

              updateScan(scan.localId, {
                status: isTerminal ? result.status : 'scanning',
                progress: isTerminal
                  ? 100
                  : Math.max(
                      scan.progress || 0,
                      STATUS_STAGE_PROGRESS[result.status] || 4,
                      getBackendProgress(result),
                    ),
                dataFound: countResultFindings(result),
                activity: extractScanActivity(
                  result,
                  getScanAssetType(scan),
                  scan.activity,
                ),
                error: result.error || null,
                approvalRequired: result.approval_required,
              });
            }
          } catch (requestError) {
            if (requestError.response?.status === 401) {
              // Handled globally by apiClient's response interceptor.
              isCancelled = true;
              return;
            }

            if (requestError.response?.status === 404) {
              updateScan(scan.localId, {
                status: 'failed',
                progress: 100,
                error: 'Scan record was not found on the server.',
              });
            }
          }
        }),
      );

      isPolling = false;
    };

    pollActiveScans();
    const pollTimer = window.setInterval(pollActiveScans, POLL_INTERVAL_MS);

    return () => {
      isCancelled = true;
      window.clearInterval(pollTimer);
    };
  }, [updateScan]);

  const downloadReport = async (scan) => {
    setDownloadingScanId(scan.scanId);
    setError('');

    try {
      const response = await apiClient.get(
        `/api/v1/agentic-scans/${scan.scanId}/export`,
        {
          responseType: 'blob',
        },
      );
      const disposition = response.headers['content-disposition'] || '';
      const filenameMatch = disposition.match(/filename="?([^";]+)"?/i);
      const filename = filenameMatch?.[1] || `dlp-scan-${scan.scanId}.xlsx`;
      const downloadUrl = URL.createObjectURL(response.data);
      const downloadLink = document.createElement('a');

      downloadLink.href = downloadUrl;
      downloadLink.download = filename;
      document.body.appendChild(downloadLink);
      downloadLink.click();
      downloadLink.remove();
      URL.revokeObjectURL(downloadUrl);
    } catch (requestError) {
      if (requestError.response?.status === 401) {
        // Handled globally by apiClient's response interceptor.
        return;
      }

      setError(formatApiError(requestError));
    } finally {
      setDownloadingScanId(null);
    }
  };

  const visibleHistory = reportType
    ? scanHistory.filter((scan) => getScanAssetType(scan) === reportType)
    : scanHistory;
  const statusCounts = calculateStatusCounts(visibleHistory);
  const tableTitle = reportType
    ? `${reportType === 'system' ? 'System' : 'DB'} scan reports`
    : 'Recent scans';

  const clearHistory = () => {
    setScanHistory([]);
    persistScanHistory([]);
    setError('');
  };

  return (
    <main className="scan-status-page">
      <header className="status-header">
        <div className="status-header__title">
          <button type="button" onClick={() => navigate('/agentic')}>
            ← Scan Console
          </button>
          <h1>
            ▤ {reportType ? `${tableTitle}` : 'Scan Status'}
          </h1>
        </div>

        <div className="status-header__actions">
          <button
            type="button"
            className="clear-history"
            onClick={clearHistory}
          >
            Clear history
          </button>

          <button
            type="button"
            className="new-scan"
            onClick={() =>
              navigate(reportType ? `/agentic?type=${reportType}` : '/agentic')
            }
          >
            ＋ New scan
          </button>
        </div>
      </header>

      {error && (
        <div className="status-error" role="alert">
          {error}
        </div>
      )}

      <StatusMetrics counts={statusCounts} />

      <section className="status-table-card" id="recent-scans">
        <div className="table-title">
          <h2>{tableTitle}</h2>
          <span>{visibleHistory.length} records</span>
        </div>

        {visibleHistory.length === 0 ? (
          <div className="empty-state">
            {reportType
              ? `No ${reportType} scan reports are available yet.`
              : 'No scans yet. Start one from the Agentic Scan Console.'}
          </div>
        ) : (
          <ScanTable
            history={visibleHistory}
            downloadingScanId={downloadingScanId}
            onDownload={downloadReport}
            onNavigate={navigate}
          />
        )}
      </section>
    </main>
  );
}

function StatusMetrics({ counts }) {
  return (
    <section className="metric-grid" aria-label="Scan status summary">
      <Metric icon="☷" label="All scans" value={counts.all} tone="blue" />
      <Metric
        icon="⌛"
        label="Scanning"
        value={counts.scanning}
        tone="amber"
      />
      <Metric
        icon="✓"
        label="Completed"
        value={counts.completed}
        tone="green"
      />
      <Metric icon="◐" label="Partial" value={counts.partial} tone="blue" />
      <Metric
        icon="Ⅱ"
        label="Review"
        value={counts.review}
        tone="purple"
      />
      <Metric icon="×" label="Error" value={counts.failed} tone="red" />
    </section>
  );
}

function Metric({ icon, label, value, tone }) {
  return (
    <div className={`metric-card ${tone}`}>
      <span className="metric-icon" aria-hidden="true">
        {icon}
      </span>
      <div>
        <strong>{value}</strong>
        <small>{label}</small>
      </div>
    </div>
  );
}

function ScanTable({
  history,
  downloadingScanId,
  onDownload,
  onNavigate,
}) {
  return (
    <div className="table-scroll">
      <table>
        <thead>
          <tr>
            <th>S.No</th>
            <th>Asset</th>
            <th>Scan details</th>
            <th>Status</th>
            <th>Progress</th>
            <th>Scan activity</th>
            <th>Sensitive data</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {history.map((scan, index) => (
            <ScanRow
              key={scan.localId}
              scan={scan}
              rowNumber={index + 1}
              isDownloading={downloadingScanId === scan.scanId}
              onDownload={onDownload}
              onNavigate={onNavigate}
            />
          ))}
        </tbody>
      </table>
    </div>
  );
}

function ScanRow({
  scan,
  rowNumber,
  isDownloading,
  onDownload,
  onNavigate,
}) {
  const metadata = STATUS_METADATA[scan.status] || STATUS_METADATA.failed;
  const isScanning = scan.status === 'scanning';

  return (
    <tr>
      <td>{rowNumber}</td>

      <td>
        <strong>{scan.assetName}</strong>
        <small>
          {scan.platform}
          {scan.scanId ? ` · Scan ID ${scan.scanId}` : ''}
        </small>
      </td>

      <td>
        <span className="goal-text" title={scan.goal}>
          {scan.goal}
        </span>
        <small>Duration: {scan.durationSeconds}s</small>
      </td>

      <td>
        <span className={`status-pill ${metadata.tone}`}>
          <i aria-hidden="true">{metadata.icon}</i>
          {metadata.label}
        </span>
        {scan.error && <small className="row-error">{scan.error}</small>}
      </td>

      <td>
        <div className="progress-wrap">
          <div className="progress-label">
            <span>
              {scan.status === 'scanning' ? 'Scanning files…' : 'Processed'}
            </span>
            <strong>{scan.progress}%</strong>
          </div>
          <div
            className="progress-track"
            role="progressbar"
            aria-valuemin="0"
            aria-valuemax="100"
            aria-valuenow={scan.progress}
          >
            <span style={{ width: `${scan.progress}%` }} />
          </div>
        </div>
      </td>

      <td>
        <ScanActivity scan={scan} />
      </td>

      <td>
        <strong className="found-count">{scan.dataFound || 0}</strong>
        <small>Findings found</small>
      </td>

      <td>
        <div className="action-buttons">
          <button
            type="button"
            aria-label={`View result for scan ${scan.scanId || ''}`}
            title="View scan result"
            disabled={!scan.scanId}
            onClick={() => onNavigate(`/scan-results/${scan.scanId}`)}
          >
            ▣
          </button>
          <button
            type="button"
            aria-label={`Download Excel report for scan ${scan.scanId || ''}`}
            title="Download Excel report"
            disabled={!scan.scanId || isScanning || isDownloading}
            onClick={() => onDownload(scan)}
          >
            {isDownloading ? '…' : '⇩'}
          </button>
          <button
            type="button"
            aria-label="Start another scan"
            title="Start another scan"
            onClick={() => onNavigate('/agentic')}
          >
            ↻
          </button>
        </div>
      </td>
    </tr>
  );
}

function ScanActivity({ scan }) {
  const activity = scan.activity || {};
  const assetType = activity.type || getScanAssetType(scan);

  if (assetType === 'database') {
    return (
      <dl className="scan-activity">
        <div>
          <dt>Tables scanned</dt>
          <dd>{formatCount(activity.tablesScanned, activity.totalTables)}</dd>
        </div>
        <div>
          <dt>Rows scanned</dt>
          <dd>{formatCount(activity.rowsScanned, null)}</dd>
        </div>
        <div>
          <dt>Data scanned</dt>
          <dd>{formatBytes(activity.bytesScanned, activity.totalBytes)}</dd>
        </div>
      </dl>
    );
  }

  return (
    <dl className="scan-activity">
      <div>
        <dt>Files scanned</dt>
        <dd>{formatCount(activity.filesScanned, activity.totalFiles)}</dd>
      </div>
      <div>
        <dt>Data scanned</dt>
        <dd>{formatBytes(activity.bytesScanned, activity.totalBytes)}</dd>
      </div>
    </dl>
  );
}
