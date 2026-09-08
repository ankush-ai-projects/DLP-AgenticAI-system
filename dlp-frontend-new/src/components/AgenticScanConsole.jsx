import { useCallback, useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';

import { apiClient, formatApiError } from '../api/client';
import './AgenticScanConsole.css';

const DEFAULT_GOAL =
  'Scan this asset for PCI and PII using read-only operations.';

const REQUESTED_ENTITIES = [
  'CREDIT_CARD',
  'AADHAAR',
  'PAN',
  'EMAIL',
  'PHONE',
];

const ENTITY_LABELS = {
  CREDIT_CARD: 'Credit Card (PCI)',
  AADHAAR: 'Aadhaar (PII)',
  PAN: 'PAN (PII)',
  EMAIL: 'Email (PII)',
  PHONE: 'Phone (PII)',
};

// Kept in sync with SUPPORTED_EXTENSIONS in
// dlp-system/app/tools/filesystem_tools.py -- anything not in that set
// is silently ignored server-side, so this list should only ever be a
// subset of it.
const FILE_EXTENSIONS = ['.txt', '.csv', '.json', '.xml', '.log', '.pdf', '.docx', '.xlsx'];

function normalizeScannerType(value) {
  return value === 'system' ? 'system' : 'database';
}

function createEmptyAsset(assetType = 'database') {
  const normalizedType = normalizeScannerType(assetType);
  return {
    name: '',
    asset_type: normalizedType,
    platform: normalizedType === 'system' ? 'windows' : 'mysql',
    host: '',
    port: normalizedType === 'system' ? null : 3306,
    database_name: '',
    root_path: '',
    secret_ref: '',
    config: {},
  };
}

function createEmptyCredentials() {
  return {
    username: '',
    password: '',
    driver: 'ODBC Driver 18 for SQL Server',
    encrypt: true,
    trust_server_certificate: false,
  };
}

function createLaunchId() {
  if (typeof globalThis.crypto?.randomUUID === 'function') {
    return globalThis.crypto.randomUUID();
  }
  return `scan-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

export default function AgenticScanConsole() {
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const scannerType = normalizeScannerType(searchParams.get('type'));

  const [assets, setAssets] = useState([]);
  const [asset, setAsset] = useState(() => createEmptyAsset(scannerType));
  const [selectedAssetId, setSelectedAssetId] = useState('');
  const [goal, setGoal] = useState(DEFAULT_GOAL);
  const [selectedEntities, setSelectedEntities] = useState(REQUESTED_ENTITIES);
  const [selectedExtensions, setSelectedExtensions] = useState(FILE_EXTENSIONS);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isDiscovering, setIsDiscovering] = useState(false);
  const [credentials, setCredentials] = useState(createEmptyCredentials);
  const [availableDatabases, setAvailableDatabases] = useState([]);
  const [selectedDatabases, setSelectedDatabases] = useState([]);

  const loadAssets = useCallback(async () => {
    const response = await apiClient.get('/api/v1/assets');
    const availableAssets = response.data;
    const matchingAssets = availableAssets.filter(
      (item) => item.asset_type === scannerType,
    );
    setAssets(availableAssets);
    setSelectedAssetId((currentId) => {
      const valid = matchingAssets.some(
        (item) => String(item.id) === String(currentId),
      );
      if (valid) return currentId;
      return matchingAssets.length ? String(matchingAssets[0].id) : '';
    });
  }, [scannerType]);

  useEffect(() => {
    setAsset(createEmptyAsset(scannerType));
    setCredentials(createEmptyCredentials());
    setAvailableDatabases([]);
    setSelectedDatabases([]);
    setSelectedAssetId('');
    setError('');
    setSuccess('');
  }, [scannerType]);

  useEffect(() => {
    let mounted = true;
    loadAssets().catch((requestError) => {
      if (mounted && requestError.response?.status !== 401) {
        setError(formatApiError(requestError));
      }
    });
    return () => {
      mounted = false;
    };
  }, [loadAssets]);

  const updateAsset = (field, value) => {
    setAsset((current) => ({ ...current, [field]: value }));
  };

  const clearDiscovery = () => {
    setAvailableDatabases([]);
    setSelectedDatabases([]);
    setSuccess('');
  };

  const updateConnection = (field, value) => {
    if (field === 'host' || field === 'port') {
      updateAsset(field, value);
    } else {
      setCredentials((current) => ({ ...current, [field]: value }));
    }
    clearDiscovery();
  };

  const changeAssetType = (value) => {
    const type = normalizeScannerType(value);
    setAsset(createEmptyAsset(type));
    setCredentials(createEmptyCredentials());
    clearDiscovery();
    setSelectedAssetId('');
    setSearchParams({ type });
  };

  const changePlatform = (platform) => {
    setAsset((current) => ({
      ...current,
      platform,
      port: platform === 'mssql' ? 1433 : platform === 'mysql' ? 3306 : null,
      database_name: '',
      secret_ref: '',
    }));
    setCredentials(createEmptyCredentials());
    clearDiscovery();
  };

  const buildConnectionPayload = () => ({
    platform: asset.platform,
    host: asset.host.trim(),
    port: Number(asset.port),
    username: credentials.username,
    password: credentials.password,
    driver: credentials.driver,
    encrypt: credentials.encrypt,
    trust_server_certificate: credentials.trust_server_certificate,
    include_system_databases: false,
  });

  const discoverDatabases = async () => {
    if (!asset.host.trim() || !asset.port || !credentials.username || !credentials.password) {
      setError('Enter host, port, username, and password before connecting.');
      return;
    }
    setIsDiscovering(true);
    setError('');
    setSuccess('');
    try {
      const response = await apiClient.post(
        '/api/v1/assets/discover-databases',
        buildConnectionPayload(),
      );
      const databases = response.data.databases || [];
      setAvailableDatabases(databases);
      setSelectedDatabases([]);
      setSuccess(
        databases.length
          ? `${databases.length} accessible database(s) found.`
          : 'Connection succeeded, but no user databases are accessible.',
      );
    } catch (requestError) {
      if (requestError.response?.status !== 401) {
        setError(formatApiError(requestError));
      }
      setAvailableDatabases([]);
      setSelectedDatabases([]);
    } finally {
      setIsDiscovering(false);
    }
  };

  const registerAsset = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    setError('');
    setSuccess('');
    try {
      if (asset.asset_type === 'database' && asset.platform !== 'sqlite') {
        if (!availableDatabases.length) {
          throw new Error('Connect and fetch databases before registering.');
        }
        if (!selectedDatabases.length) {
          throw new Error('Select at least one database to register.');
        }
        const response = await apiClient.post(
          '/api/v1/assets/register-databases',
          {
            ...buildConnectionPayload(),
            asset_name: asset.name,
            database_names: selectedDatabases,
          },
        );
        const registered = response.data.registered?.length || 0;
        const skipped = response.data.skipped_databases?.length || 0;
        setSuccess(
          `${registered} database asset(s) registered${
            skipped ? `; ${skipped} duplicate(s) skipped` : ''
          }.`,
        );
      } else {
        const payload = { ...asset };
        if (payload.asset_type === 'system') {
          payload.host = null;
          payload.port = null;
          payload.database_name = null;
          payload.secret_ref = null;
        } else {
          payload.root_path = null;
        }
        await apiClient.post('/api/v1/assets', payload);
        setSuccess('Asset registered successfully.');
      }
      setAsset(createEmptyAsset(scannerType));
      setCredentials(createEmptyCredentials());
      setAvailableDatabases([]);
      setSelectedDatabases([]);
      await loadAssets();
    } catch (requestError) {
      if (requestError.response?.status !== 401) {
        setError(requestError.response ? formatApiError(requestError) : requestError.message);
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  const startScan = (event) => {
    event.preventDefault();
    if (selectedEntities.length === 0) {
      setError('Select at least one data type to scan for.');
      return;
    }
    if (scannerType === 'system' && selectedExtensions.length === 0) {
      setError('Select at least one file extension to scan.');
      return;
    }
    const selectedAsset = assets.find(
      (item) => String(item.id) === String(selectedAssetId),
    );
    navigate('/scan-status', {
      state: {
        startScan: true,
        launchId: createLaunchId(),
        asset: selectedAsset,
        request: {
          asset_id: Number(selectedAssetId),
          goal,
          dry_run: true,
          execute_async: true,
          entities: selectedEntities,
          ...(scannerType === 'system'
            ? { file_extensions: selectedExtensions }
            : {}),
        },
      },
    });
  };

  const databaseAsset = asset.asset_type === 'database';
  const sqliteAsset = asset.platform === 'sqlite';
  const visibleAssets = assets.filter((item) => item.asset_type === scannerType);

  return (
    <main className="agentic-console">
      <header className="agentic-console__header">
        <button type="button" onClick={() => navigate('/dashboard')}>← Dashboard</button>
        <h1>{scannerType === 'system' ? 'System Scanner' : 'DB Scanner'}</h1>
      </header>

      {error && <div className="console-error" role="alert">{error}</div>}
      {success && <div className="console-success" role="status">{success}</div>}

      <section className="console-grid">
        <form className="console-card" onSubmit={registerAsset}>
          <h2>1. Register asset</h2>
          <label>
            Asset type
            <select value={asset.asset_type} onChange={(event) => changeAssetType(event.target.value)}>
              <option value="database">Database</option>
              <option value="system">System</option>
            </select>
          </label>
          <label>
            Asset name
            <input
              required
              value={asset.name}
              placeholder="Production payments database"
              onChange={(event) => updateAsset('name', event.target.value)}
            />
          </label>
          <label>
            Platform
            <select value={asset.platform} onChange={(event) => changePlatform(event.target.value)}>
              {databaseAsset ? (
                <>
                  <option value="mysql">MySQL</option>
                  <option value="mssql">MSSQL</option>
                  <option value="sqlite">SQLite demo</option>
                </>
              ) : (
                <>
                  <option value="windows">Windows</option>
                  <option value="linux">Linux</option>
                </>
              )}
            </select>
          </label>

          {databaseAsset ? (
            <DatabaseFields
              asset={asset}
              available={availableDatabases}
              credentials={credentials}
              discovering={isDiscovering}
              sqlite={sqliteAsset}
              onAssetChange={updateAsset}
              onConnectionChange={updateConnection}
              onDiscover={discoverDatabases}
              selected={selectedDatabases}
              setSelected={setSelectedDatabases}
            />
          ) : (
            <ScanPathsInput
              value={asset.root_path}
              onChange={(value) => updateAsset('root_path', value)}
            />
          )}
          <button type="submit" disabled={isSubmitting || isDiscovering}>
            {isSubmitting ? 'Registering…' : 'Register'}
          </button>
        </form>

        <form className="console-card" onSubmit={startScan}>
          <h2>2. Run bounded agent workflow</h2>
          <label>
            Asset
            <select required value={selectedAssetId} onChange={(event) => setSelectedAssetId(event.target.value)}>
              <option value="">Select asset</option>
              {visibleAssets.map((item) => (
                <option key={item.id} value={item.id}>{item.name} · {item.platform}</option>
              ))}
            </select>
          </label>
          <label>
            Scan Type
            <div className="scan-type-pill">Full Scan (bounded, read-only)</div>
          </label>
          <label>
            Data Types
            <div className="entity-chip-group">
              {REQUESTED_ENTITIES.map((entity) => {
                const isSelected = selectedEntities.includes(entity);
                return (
                  <button
                    type="button"
                    key={entity}
                    className={`entity-chip ${isSelected ? 'selected' : ''}`}
                    aria-pressed={isSelected}
                    onClick={() =>
                      setSelectedEntities((current) =>
                        isSelected
                          ? current.filter((item) => item !== entity)
                          : [...current, entity],
                      )
                    }
                  >
                    {ENTITY_LABELS[entity] || entity}
                  </button>
                );
              })}
            </div>
          </label>
          {scannerType === 'system' && (
            <label>
              File Extensions to Scan
              <div className="entity-chip-group">
                {FILE_EXTENSIONS.map((extension) => {
                  const isSelected = selectedExtensions.includes(extension);
                  return (
                    <button
                      type="button"
                      key={extension}
                      className={`entity-chip ${isSelected ? 'selected' : ''}`}
                      aria-pressed={isSelected}
                      onClick={() =>
                        setSelectedExtensions((current) =>
                          isSelected
                            ? current.filter((item) => item !== extension)
                            : [...current, extension],
                        )
                      }
                    >
                      {extension}
                    </button>
                  );
                })}
              </div>
              <small className="field-hint">
                Only these file types are scanned. Leave all selected to
                scan everything supported.
              </small>
            </label>
          )}
          <label>
            Scan goal
            <textarea rows="7" value={goal} onChange={(event) => setGoal(event.target.value)} />
          </label>
          <button
            type="submit"
            disabled={
              !selectedAssetId ||
              selectedEntities.length === 0 ||
              (scannerType === 'system' && selectedExtensions.length === 0)
            }
          >
            Plan and scan
          </button>
        </form>
      </section>

      <button type="button" className="history-link" onClick={() => navigate('/scan-status')}>
        View scan status and results
      </button>
    </main>
  );
}

function DatabaseFields({
  asset,
  available,
  credentials,
  discovering,
  sqlite,
  onAssetChange,
  onConnectionChange,
  onDiscover,
  selected,
  setSelected,
}) {
  if (sqlite) {
    return (
      <label>
        Absolute database path
        <input
          required
          value={asset.database_name}
          placeholder="D:/data/demo.db"
          onChange={(event) => onAssetChange('database_name', event.target.value)}
        />
      </label>
    );
  }

  return (
    <>
      <div className="field-row">
        <label>
          Host
          <input required value={asset.host} placeholder="10.10.10.20" onChange={(event) => onConnectionChange('host', event.target.value)} />
        </label>
        <label>
          Port
          <input required type="number" min="1" max="65535" value={asset.port || ''} onChange={(event) => onConnectionChange('port', Number(event.target.value))} />
        </label>
      </div>
      <div className="field-row field-row--credentials">
        <label>
          Database username
          <input required autoComplete="username" value={credentials.username} placeholder="Read-only database user" onChange={(event) => onConnectionChange('username', event.target.value)} />
        </label>
        <label>
          Database password
          <input required autoComplete="new-password" type="password" value={credentials.password} placeholder="Database password" onChange={(event) => onConnectionChange('password', event.target.value)} />
        </label>
      </div>

      {asset.platform === 'mssql' && (
        <div className="mssql-options">
          <label>
            ODBC driver
            <input required value={credentials.driver} onChange={(event) => onConnectionChange('driver', event.target.value)} />
          </label>
          <label className="checkbox-label">
            <input type="checkbox" checked={credentials.trust_server_certificate} onChange={(event) => onConnectionChange('trust_server_certificate', event.target.checked)} />
            Trust server certificate (local/test only)
          </label>
        </div>
      )}

      <button type="button" className="discover-button" disabled={discovering} onClick={onDiscover}>
        {discovering ? 'Connecting…' : 'Connect & Fetch Databases'}
      </button>

      {available.length > 0 && (
        <div className="database-picker">
          <div className="database-picker__header">
            <span>Available databases</span>
            <div>
              <button type="button" onClick={() => setSelected([...available])}>Select all</button>
              <button type="button" onClick={() => setSelected([])}>Clear</button>
            </div>
          </div>
          <select
            required
            multiple
            size={Math.min(Math.max(available.length, 3), 8)}
            value={selected}
            onChange={(event) =>
              setSelected(Array.from(event.target.selectedOptions, (option) => option.value))
            }
          >
            {available.map((database) => (
              <option key={database} value={database}>{database}</option>
            ))}
          </select>
          <small>Select one or more databases. Use Ctrl/Command for multiple selection.</small>
        </div>
      )}
    </>
  );
}

function ScanPathsInput({ value, onChange }) {
  const [draft, setDraft] = useState('');
  const paths = value ? value.split(',').map((item) => item.trim()).filter(Boolean) : [];

  const addPath = () => {
    const trimmed = draft.trim();
    if (!trimmed || paths.includes(trimmed)) {
      setDraft('');
      return;
    }
    onChange([...paths, trimmed].join(', '));
    setDraft('');
  };

  const removePath = (target) => {
    onChange(paths.filter((item) => item !== target).join(', '));
  };

  return (
    <label>
      Scan Paths
      <div className="scan-paths-input">
        {paths.map((path) => (
          <span key={path} className="scan-path-chip">
            {path}
            <button
              type="button"
              onClick={() => removePath(path)}
              aria-label={`Remove ${path}`}
            >
              ×
            </button>
          </span>
        ))}
        <input
          value={draft}
          placeholder={paths.length === 0 ? 'D:/piiTest' : 'Add another path…'}
          onChange={(event) => setDraft(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === 'Enter') {
              event.preventDefault();
              addPath();
            }
          }}
          onBlur={addPath}
        />
      </div>
      <small className="field-hint">
        Type a directory path and press Enter to add it. Multiple paths are
        all scanned together in one run.
      </small>
      {/* Keeps the underlying form's required-field semantics working
          even though the visible control is the chip input above. */}
      <input type="hidden" required value={value} readOnly />
    </label>
  );
} 