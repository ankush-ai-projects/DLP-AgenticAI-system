import { useEffect, useMemo, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import {
  Cell,
  Line,
  LineChart,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

import { apiClient } from '../api/client';
import './NeonDashboard.css';

const DASHBOARD_TYPES = {
  system: {
    label: 'System Dashboard',
    subtitle: 'Windows and Linux filesystem scan analytics',
    icon: '🖥️',
  },
  database: {
    label: 'DB Dashboard',
    subtitle: 'MySQL, MSSQL and SQLite scan analytics',
    icon: '🗄️',
  },
};

const RISK_COLORS = {
  Critical: '#ff3366',
  High: '#ff9933',
  Medium: '#ffcc00',
  Low: '#00ffff',
};

const ENTITY_COLORS = [
  '#00ffff',
  '#ff00ff',
  '#ffcc00',
  '#00ff88',
  '#ff3366',
  '#8a7dff',
];

const EMPTY_DASHBOARD = {
  generated_at: null,
  metrics: {
    total_findings: 0,
    incidents: 0,
    total_scans: 0,
    completed_scans: 0,
    partial_scans: 0,
    failed_scans: 0,
    active_scans: 0,
    monitored_assets: 0,
  },
  risk_counts: {
    critical: 0,
    high: 0,
    medium: 0,
    low: 0,
  },
  entity_counts: [],
  status_counts: {},
  findings_trend: [],
  recent_scans: [],
};

function formatEntityName(value) {
  return String(value || 'Unknown')
    .toLowerCase()
    .split('_')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function formatStatus(value) {
  return String(value || 'unknown')
    .replaceAll('_', ' ')
    .replace(/\b\w/g, (character) => character.toUpperCase());
}

function formatDate(value) {
  if (!value) return 'Not available';

  return new Intl.DateTimeFormat('en-IN', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(new Date(value));
}

export default function NeonDashboard() {
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const requestedDashboardType = searchParams.get('type');
  const [dashboardType, setDashboardType] = useState(
    requestedDashboardType === 'database' ? 'database' : 'system',
  );
  const [dashboard, setDashboard] = useState(EMPTY_DASHBOARD);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const nextDashboardType =
      requestedDashboardType === 'database' ? 'database' : 'system';

    setDashboardType(nextDashboardType);
  }, [requestedDashboardType]);

  useEffect(() => {
    let isCancelled = false;

    const fetchDashboard = async ({ showLoader = false } = {}) => {
      if (showLoader) setLoading(true);

      try {
        const response = await apiClient.get('/api/v1/dashboard/summary', {
          params: {
            asset_type: dashboardType,
          },
        });

        if (!isCancelled) {
          setDashboard(response.data);
          setError('');
        }
      } catch (requestError) {
        // 401s are handled globally by apiClient's response interceptor.
        if (!isCancelled && requestError.response?.status !== 401) {
          setError(
            requestError.response?.data?.detail ||
              'Dashboard data load nahi ho saka.',
          );
        }
      } finally {
        if (!isCancelled) setLoading(false);
      }
    };

    fetchDashboard({ showLoader: true });
    const refreshTimer = window.setInterval(fetchDashboard, 5000);

    return () => {
      isCancelled = true;
      window.clearInterval(refreshTimer);
    };
  }, [dashboardType]);

  const severityData = useMemo(
    () =>
      [
        ['Critical', dashboard.risk_counts.critical],
        ['High', dashboard.risk_counts.high],
        ['Medium', dashboard.risk_counts.medium],
        ['Low', dashboard.risk_counts.low],
      ].map(([name, value]) => ({
        name,
        value,
        color: RISK_COLORS[name],
      })),
    [dashboard.risk_counts],
  );

  const statusData = useMemo(
    () =>
      Object.entries(dashboard.status_counts).map(([name, value], index) => ({
        name: formatStatus(name),
        value,
        color: ENTITY_COLORS[index % ENTITY_COLORS.length],
      })),
    [dashboard.status_counts],
  );

  const threatScore = Math.min(
    100,
    dashboard.risk_counts.critical * 10 +
      dashboard.risk_counts.high * 5 +
      dashboard.risk_counts.medium * 2,
  );

  const riskLabel =
    threatScore >= 70
      ? 'Critical Risk'
      : threatScore >= 40
        ? 'High Risk'
        : threatScore >= 15
          ? 'Medium Risk'
          : 'Low Risk';

  const dateRange = dashboard.findings_trend.length
    ? `${dashboard.findings_trend[0].label} - ${
        dashboard.findings_trend.at(-1).label
      }`
    : 'Last 7 days';

  const handleDashboardTypeChange = (type) => {
    setDashboardType(type);
    setSearchParams({ type });
  };

  return (
    <div className="neon-dashboard">
      <main className="neon-content">
        <section className="dashboard-hero">
          <div className="dashboard-hero__copy">
            <span className="dashboard-eyebrow">LIVE SECURITY OVERVIEW</span>
            <h1>{DASHBOARD_TYPES[dashboardType].label}</h1>
            <p>{DASHBOARD_TYPES[dashboardType].subtitle}</p>
          </div>

          <div className="dashboard-hero__controls">
            <div className="dashboard-type-tabs" aria-label="Dashboard type">
              {Object.entries(DASHBOARD_TYPES).map(([type, details]) => (
                <button
                  type="button"
                  key={type}
                  className={dashboardType === type ? 'selected' : ''}
                  onClick={() => handleDashboardTypeChange(type)}
                >
                  <span aria-hidden="true">{details.icon}</span>
                  {details.label}
                </button>
              ))}
            </div>

            <div className="dashboard-range">
              <span>{dateRange}</span>
              <small>Auto refresh · 5 seconds</small>
            </div>

            <div className="dashboard-risk-chip">
              <span>{threatScore}</span>
              <div>
                <small>Threat score</small>
                <strong>{riskLabel}</strong>
              </div>
            </div>
          </div>
        </section>

        {error && <div className="dashboard-error">{error}</div>}

        <div className="dashboard-toolbar">
          <span>
            Last synchronized {formatDate(dashboard.generated_at)}
          </span>
        </div>

        {loading ? (
          <div className="dashboard-loading">LOADING LIVE SCAN DATA...</div>
        ) : (
          <DashboardContent
            dashboard={dashboard}
            severityData={severityData}
            statusData={statusData}
            navigate={navigate}
          />
        )}
      </main>
    </div>
  );
}

function DashboardContent({ dashboard, severityData, statusData, navigate }) {
  const metrics = dashboard.metrics;

  return (
    <>
      <section className="stats-row">
        <StatCard
          label="TOTAL DATA FOUND"
          value={metrics.total_findings}
          tone="cyan"
          caption="Verified sensitive findings"
        />
        <StatCard
          label="HIGH-RISK INCIDENTS"
          value={metrics.incidents}
          tone="purple"
          caption="Critical and high findings"
        />
        <StatCard
          label="COMPLETED SCANS"
          value={metrics.completed_scans}
          tone="yellow"
          caption={`${metrics.partial_scans} partial · ${metrics.failed_scans} failed`}
        />
        <StatCard
          label="MONITORED ASSETS"
          value={metrics.monitored_assets}
          tone="green"
          caption={`${metrics.total_scans} total scans · ${metrics.active_scans} active`}
        />
      </section>

      <section className="charts-row">
        <div className="chart-card large">
          <div className="card-header">
            <h3>FINDINGS OVER TIME</h3>
            <span>Last 7 days</span>
          </div>

          <ResponsiveContainer width="100%" height={280}>
            <LineChart data={dashboard.findings_trend}>
              <XAxis dataKey="label" stroke="#72d9f7" />
              <YAxis allowDecimals={false} stroke="#72d9f7" />
              <Tooltip
                contentStyle={{
                  background: '#071426',
                  border: '1px solid #00d9ff',
                  borderRadius: 8,
                }}
              />
              <Line
                type="monotone"
                dataKey="value"
                name="Data found"
                stroke="#00ffff"
                strokeWidth={3}
                dot={{ fill: '#00ffff', r: 5 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <DonutCard
          title="FINDINGS BY SEVERITY"
          data={severityData}
          total={metrics.total_findings}
        />
      </section>

      <section className="bottom-row">
        <EntityTypesCard entities={dashboard.entity_counts} />
        <DonutCard
          title="SCAN STATUS"
          data={statusData}
          total={metrics.total_scans}
        />
        <RecentScansCard scans={dashboard.recent_scans} navigate={navigate} />
      </section>
    </>
  );
}

function StatCard({ label, value, tone, caption }) {
  return (
    <article className={`stat-card ${tone}`}>
      <div className="stat-header">{label}</div>
      <div className="stat-value">{Number(value || 0).toLocaleString()}</div>
      <div className="stat-caption">{caption}</div>
    </article>
  );
}

function DonutCard({ title, data, total }) {
  const visibleData = data.filter((item) => item.value > 0);

  return (
    <article className="chart-card">
      <div className="card-header">
        <h3>{title}</h3>
      </div>

      {visibleData.length ? (
        <>
          <div className="donut-chart">
            <ResponsiveContainer width="100%" height={210}>
              <PieChart>
                <Pie
                  data={visibleData}
                  cx="50%"
                  cy="50%"
                  innerRadius={62}
                  outerRadius={84}
                  paddingAngle={4}
                  dataKey="value"
                >
                  {visibleData.map((entry) => (
                    <Cell key={entry.name} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    background: '#071426',
                    border: '1px solid #00d9ff',
                    borderRadius: 8,
                  }}
                />
              </PieChart>
            </ResponsiveContainer>

            <div className="donut-center">
              <div className="donut-value">{total}</div>
              <div className="donut-label">TOTAL</div>
            </div>
          </div>

          <div className="legend">
            {visibleData.map((item) => (
              <div key={item.name} className="legend-item">
                <span
                  className="legend-dot"
                  style={{ background: item.color }}
                />
                <span className="legend-label">{item.name}</span>
                <span className="legend-value">{item.value}</span>
              </div>
            ))}
          </div>
        </>
      ) : (
        <EmptyData message="No scan data available" />
      )}
    </article>
  );
}

function EntityTypesCard({ entities }) {
  const visibleEntities = entities.slice(0, 6);
  const maximum = Math.max(...visibleEntities.map((item) => item.count), 1);

  return (
    <article className="chart-card">
      <div className="card-header">
        <h3>TOP DATA TYPES DETECTED</h3>
      </div>

      {visibleEntities.length ? (
        <div className="data-types-list">
          {visibleEntities.map((item, index) => (
            <div key={item.entity_type} className="data-type-item">
              <div className="data-type-label">
                {formatEntityName(item.entity_type)}
              </div>
              <div className="data-type-bar">
                <div
                  className="data-type-fill"
                  style={{
                    width: `${(item.count / maximum) * 100}%`,
                    background: ENTITY_COLORS[index % ENTITY_COLORS.length],
                  }}
                />
              </div>
              <div className="data-type-count">{item.count}</div>
            </div>
          ))}
        </div>
      ) : (
        <EmptyData message="No sensitive data detected yet" />
      )}
    </article>
  );
}

function RecentScansCard({ scans, navigate }) {
  return (
    <article className="chart-card recent-scans-card">
      <div className="card-header">
        <h3>RECENT SCANS</h3>
      </div>

      {scans.length ? (
        <div className="recent-scan-list">
          {scans.map((scan) => (
            <button
              type="button"
              key={scan.scan_id}
              className="recent-scan-item"
              onClick={() => navigate(`/scan-results/${scan.scan_id}`)}
            >
              <span className={`scan-risk ${scan.risk_level}`} />
              <span className="recent-scan-content">
                <strong>{scan.asset_name}</strong>
                <small>
                  {scan.platform} · {formatStatus(scan.status)}
                </small>
              </span>
              <span className="recent-scan-count">{scan.data_found}</span>
            </button>
          ))}
        </div>
      ) : (
        <EmptyData message="No scans available for this dashboard" />
      )}
    </article>
  );
}

function EmptyData({ message }) {
  return <div className="empty-dashboard-data">{message}</div>;
} 
