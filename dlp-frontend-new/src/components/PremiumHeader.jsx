import { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';

import './PremiumHeader.css';

const NAVIGATION_GROUPS = [
  {
    id: 'dashboards',
    label: 'Dashboards',
    icon: 'dashboard',
    items: [
      {
        label: 'System Dashboard',
        description: 'Filesystem scan analytics and risk overview',
        icon: 'monitor',
        to: '/dashboard?type=system',
      },
      {
        label: 'DB Dashboard',
        description: 'Database scan analytics and findings',
        icon: 'database',
        to: '/dashboard?type=database',
      },
    ],
  },
  {
    id: 'scanners',
    label: 'Scanners',
    icon: 'radar',
    items: [
      {
        label: 'System Scanner',
        description: 'Scan allowlisted Windows and Linux paths',
        icon: 'monitor',
        to: '/agentic?type=system',
      },
      {
        label: 'DB Scanner',
        description: 'Scan MySQL, MSSQL and SQLite assets',
        icon: 'database',
        to: '/agentic?type=database',
      },
    ],
  },
  {
    id: 'scan-data',
    label: 'Scan Data',
    icon: 'scan',
    items: [
      {
        label: 'New Scan',
        description: 'Register an asset and start a protected scan',
        icon: 'plus',
        to: '/agentic',
      },
      {
        label: 'Scan Status',
        description: 'Track progress and live findings',
        icon: 'activity',
        to: '/scan-status',
      },
      {
        label: 'Recent Scan Results',
        description: 'Open completed and partial scan results',
        icon: 'results',
        to: '/scan-status#recent-scans',
      },
    ],
  },
  {
    id: 'reports',
    label: 'Reports',
    icon: 'report',
    items: [
      {
        label: 'System Reports',
        description: 'View and download system scan reports',
        icon: 'file',
        to: '/scan-status?reports=system#recent-scans',
      },
      {
        label: 'DB Reports',
        description: 'View and download database scan reports',
        icon: 'table',
        to: '/scan-status?reports=database#recent-scans',
      },
    ],
  },
];

const SEARCH_ITEMS = NAVIGATION_GROUPS.flatMap((group) =>
  group.items.map((item) => ({ ...item, group: group.label })),
);

function getInitials(username) {
  const normalizedName = String(username || 'User').trim();

  return normalizedName.slice(0, 2).toUpperCase();
}

function isItemCurrent(item, location) {
  const target = new URL(item.to, window.location.origin);

  if (target.pathname !== location.pathname) {
    return false;
  }

  const currentSearch = new URLSearchParams(location.search);
  const targetEntries = [...target.searchParams.entries()];

  if (targetEntries.length > 0) {
    return targetEntries.every(
      ([key, value]) => currentSearch.get(key) === value,
    );
  }

  if (target.pathname === '/agentic') {
    return !currentSearch.has('type');
  }

  if (target.pathname === '/scan-status') {
    return !currentSearch.has('reports');
  }

  return true;
}

function isGroupCurrent(groupId, location) {
  const currentSearch = new URLSearchParams(location.search);

  if (groupId === 'dashboards') {
    return location.pathname === '/dashboard';
  }

  if (groupId === 'scanners') {
    return location.pathname === '/agentic' && currentSearch.has('type');
  }

  if (groupId === 'scan-data') {
    return (
      (location.pathname === '/agentic' && !currentSearch.has('type')) ||
      (location.pathname === '/scan-status' && !currentSearch.has('reports')) ||
      location.pathname.startsWith('/scan-results/')
    );
  }

  if (groupId === 'reports') {
    return location.pathname === '/scan-status' && currentSearch.has('reports');
  }

  return false;
}

export default function PremiumHeader({ user, onLogout }) {
  const location = useLocation();
  const navigate = useNavigate();
  const headerRef = useRef(null);
  const searchInputRef = useRef(null);
  const [openPanel, setOpenPanel] = useState(null);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  const filteredSearchItems = useMemo(() => {
    const query = searchQuery.trim().toLowerCase();

    if (!query) return SEARCH_ITEMS;

    return SEARCH_ITEMS.filter((item) =>
      `${item.group} ${item.label} ${item.description}`
        .toLowerCase()
        .includes(query),
    );
  }, [searchQuery]);

  useEffect(() => {
    setOpenPanel(null);
    setMobileMenuOpen(false);
    setSearchQuery('');
  }, [location.pathname, location.search, location.hash]);

  useEffect(() => {
    const closeOnOutsideClick = (event) => {
      if (headerRef.current && !headerRef.current.contains(event.target)) {
        setOpenPanel(null);
        setMobileMenuOpen(false);
      }
    };

    const closeOnEscape = (event) => {
      if (event.key === 'Escape') {
        setOpenPanel(null);
        setMobileMenuOpen(false);
      }
    };

    document.addEventListener('pointerdown', closeOnOutsideClick);
    document.addEventListener('keydown', closeOnEscape);

    return () => {
      document.removeEventListener('pointerdown', closeOnOutsideClick);
      document.removeEventListener('keydown', closeOnEscape);
    };
  }, []);

  useEffect(() => {
    if (openPanel === 'search') {
      window.requestAnimationFrame(() => searchInputRef.current?.focus());
    }
  }, [openPanel]);

  const togglePanel = (panelName) => {
    setOpenPanel((currentPanel) =>
      currentPanel === panelName ? null : panelName,
    );
  };

  const handleSearchItemClick = (destination) => {
    setOpenPanel(null);
    navigate(destination);
  };

  const handleLogout = () => {
    setOpenPanel(null);
    onLogout();
    navigate('/login', { replace: true });
  };

  return (
    <header className="premium-header" ref={headerRef}>
      <div className="premium-header__bar">
        <Link className="premium-brand" to="/dashboard?type=system">
          <span className="premium-brand__mark" aria-hidden="true">
            <Icon name="shield" />
          </span>
          <span className="premium-brand__copy">
            <strong>SentinelDLP</strong>
            <small>DATA PROTECTION</small>
          </span>
        </Link>

        <button
          type="button"
          className="premium-mobile-toggle"
          aria-label="Toggle navigation"
          aria-expanded={mobileMenuOpen}
          onClick={() => setMobileMenuOpen((isOpen) => !isOpen)}
        >
          <Icon name={mobileMenuOpen ? 'close' : 'menu'} />
        </button>

        <nav
          className={`premium-navigation ${mobileMenuOpen ? 'is-open' : ''}`}
          aria-label="Primary navigation"
        >
          {NAVIGATION_GROUPS.map((group) => {
            const isOpen = openPanel === group.id;
            const isCurrent = isGroupCurrent(group.id, location);

            return (
              <div className="premium-nav-group" key={group.id}>
                <button
                  type="button"
                  className={`premium-nav-trigger ${
                    isOpen ? 'is-active' : ''
                  } ${isCurrent ? 'is-current' : ''}`}
                  aria-expanded={isOpen}
                  onClick={() => togglePanel(group.id)}
                >
                  <Icon name={group.icon} />
                  <span>{group.label}</span>
                  <Icon name="chevron" className="premium-chevron" />
                </button>

                {isOpen && (
                  <div className="premium-dropdown">
                    <div className="premium-dropdown__heading">
                      <span>{group.label}</span>
                      <small>Select a workspace</small>
                    </div>

                    <div className="premium-dropdown__items">
                      {group.items.map((item) => (
                        <Link
                          className={`premium-dropdown__item ${
                            isItemCurrent(item, location) ? 'is-current' : ''
                          }`}
                          key={item.label}
                          to={item.to}
                        >
                          <span className="premium-dropdown__icon">
                            <Icon name={item.icon} />
                          </span>
                          <span>
                            <strong>{item.label}</strong>
                            <small>{item.description}</small>
                          </span>
                          <Icon name="arrow" />
                        </Link>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </nav>

        <div className="premium-actions">
          <ActionButton
            label="Home"
            icon="home"
            active={location.pathname === '/dashboard'}
            onClick={() => navigate('/dashboard?type=system')}
          />
          <ActionButton
            label="Search"
            icon="search"
            active={openPanel === 'search'}
            onClick={() => togglePanel('search')}
          />
          <ActionButton
            label="Help"
            icon="help"
            active={openPanel === 'help'}
            onClick={() => togglePanel('help')}
          />
          <ActionButton
            label="Settings"
            icon="settings"
            active={openPanel === 'settings'}
            onClick={() => togglePanel('settings')}
          />

          <button
            type="button"
            className={`premium-profile ${openPanel === 'profile' ? 'is-active' : ''}`}
            aria-expanded={openPanel === 'profile'}
            onClick={() => togglePanel('profile')}
          >
            <span className="premium-avatar">{getInitials(user?.username)}</span>
            <span className="premium-profile__name">
              <small>Signed in as</small>
              <strong>{user?.username || 'User'}</strong>
            </span>
            <Icon name="chevron" />
          </button>

          <ActionButton label="Logout" icon="logout" onClick={handleLogout} />
        </div>

        {openPanel === 'search' && (
          <SearchPanel
            inputRef={searchInputRef}
            items={filteredSearchItems}
            query={searchQuery}
            onChange={setSearchQuery}
            onSelect={handleSearchItemClick}
          />
        )}

        {openPanel === 'help' && (
          <InfoPanel
            title="Help Center"
            icon="help"
            description="Quick access to the main DLP workflows."
            items={[
              'Start a scan from Scanners or Scan Data.',
              'Track live progress from Scan Status.',
              'Download Excel reports after scan processing.',
            ]}
          />
        )}

        {openPanel === 'settings' && (
          <InfoPanel
            title="Settings"
            icon="settings"
            description="Security and scanner configuration will be connected in the next update."
            items={[
              'Scanner preferences',
              'Notifications',
              'Security and access',
            ]}
          />
        )}

        {openPanel === 'profile' && (
          <ProfilePanel user={user} onLogout={handleLogout} />
        )}
      </div>
    </header>
  );
}

function ActionButton({ active = false, icon, label, onClick }) {
  return (
    <button
      type="button"
      className={`premium-action ${active ? 'is-active' : ''}`}
      aria-label={label}
      title={label}
      onClick={onClick}
    >
      <Icon name={icon} />
      <span>{label}</span>
    </button>
  );
}

function SearchPanel({ inputRef, items, onChange, onSelect, query }) {
  return (
    <div className="premium-flyout premium-search-panel">
      <div className="premium-search-box">
        <Icon name="search" />
        <input
          ref={inputRef}
          type="search"
          value={query}
          placeholder="Search dashboards, scanners and reports..."
          onChange={(event) => onChange(event.target.value)}
        />
        <kbd>ESC</kbd>
      </div>

      <div className="premium-search-results">
        {items.length ? (
          items.map((item) => (
            <button
              type="button"
              key={`${item.group}-${item.label}`}
              onClick={() => onSelect(item.to)}
            >
              <span className="premium-dropdown__icon">
                <Icon name={item.icon} />
              </span>
              <span>
                <small>{item.group}</small>
                <strong>{item.label}</strong>
              </span>
              <Icon name="arrow" />
            </button>
          ))
        ) : (
          <div className="premium-search-empty">No matching module found.</div>
        )}
      </div>
    </div>
  );
}

function InfoPanel({ description, icon, items, title }) {
  return (
    <div className="premium-flyout premium-info-panel">
      <div className="premium-info-panel__title">
        <span><Icon name={icon} /></span>
        <div>
          <strong>{title}</strong>
          <small>{description}</small>
        </div>
      </div>

      <ul>
        {items.map((item) => (
          <li key={item}>
            <Icon name="check" />
            <span>{item}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

function ProfilePanel({ onLogout, user }) {
  return (
    <div className="premium-flyout premium-profile-panel">
      <div className="premium-profile-panel__identity">
        <span className="premium-avatar large">
          {getInitials(user?.username)}
        </span>
        <div>
          <strong>{user?.username || 'User'}</strong>
          <small>{user?.email || 'Authenticated DLP user'}</small>
        </div>
      </div>

      <div className="premium-profile-panel__status">
        <span /> Active session
      </div>

      <button type="button" onClick={onLogout}>
        <Icon name="logout" />
        Sign out securely
      </button>
    </div>
  );
}

function Icon({ className = '', name }) {
  const paths = {
    activity: <path d="M3 12h4l2.2-6 4.2 12 2.2-6H21" />,
    arrow: <><path d="M5 12h14" /><path d="m13 6 6 6-6 6" /></>,
    check: <path d="m5 12 4 4L19 6" />,
    chevron: <path d="m7 10 5 5 5-5" />,
    close: <><path d="m6 6 12 12" /><path d="m18 6-12 12" /></>,
    dashboard: <><rect x="3" y="3" width="7" height="7" rx="1" /><rect x="14" y="3" width="7" height="7" rx="1" /><rect x="3" y="14" width="7" height="7" rx="1" /><rect x="14" y="14" width="7" height="7" rx="1" /></>,
    database: <><ellipse cx="12" cy="5" rx="8" ry="3" /><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5" /><path d="M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6" /></>,
    file: <><path d="M6 2h8l4 4v16H6z" /><path d="M14 2v5h5" /><path d="M9 13h6M9 17h6" /></>,
    help: <><circle cx="12" cy="12" r="9" /><path d="M9.8 9a2.4 2.4 0 1 1 3.6 2.1c-.9.5-1.4 1.1-1.4 2.4" /><path d="M12 17h.01" /></>,
    home: <><path d="m3 11 9-8 9 8" /><path d="M5 10v10h14V10" /><path d="M9 20v-6h6v6" /></>,
    logout: <><path d="M10 5H5v14h5" /><path d="M14 8l4 4-4 4" /><path d="M9 12h9" /></>,
    menu: <><path d="M4 7h16M4 12h16M4 17h16" /></>,
    monitor: <><rect x="3" y="4" width="18" height="13" rx="2" /><path d="M8 21h8M12 17v4" /></>,
    plus: <><circle cx="12" cy="12" r="9" /><path d="M12 8v8M8 12h8" /></>,
    radar: <><circle cx="12" cy="12" r="9" /><circle cx="12" cy="12" r="5" /><path d="m12 12 6-6" /><circle cx="12" cy="12" r="1" /></>,
    report: <><path d="M5 3h14v18H5z" /><path d="M9 17v-4M12 17V8M15 17v-7" /></>,
    results: <><path d="M5 4h14v16H5z" /><path d="m8 13 2 2 5-6M8 8h3" /></>,
    scan: <><path d="M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4" /><path d="M7 12h10" /></>,
    search: <><circle cx="11" cy="11" r="7" /><path d="m20 20-4-4" /></>,
    settings: <><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1-2.8 2.8-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.6v.2h-4V21a1.7 1.7 0 0 0-1-1.6 1.7 1.7 0 0 0-1.9.3l-.1.1L4.2 17l.1-.1a1.7 1.7 0 0 0 .3-1.9A1.7 1.7 0 0 0 3 14H2.8v-4H3a1.7 1.7 0 0 0 1.6-1 1.7 1.7 0 0 0-.3-1.9L4.2 7 7 4.2l.1.1A1.7 1.7 0 0 0 9 4.6a1.7 1.7 0 0 0 1-1.6v-.2h4V3a1.7 1.7 0 0 0 1 1.6 1.7 1.7 0 0 0 1.9-.3l.1-.1L19.8 7l-.1.1a1.7 1.7 0 0 0-.3 1.9 1.7 1.7 0 0 0 1.6 1h.2v4H21a1.7 1.7 0 0 0-1.6 1Z" /></>,
    shield: <><path d="M12 2 4.5 5v6c0 5 3.2 8.4 7.5 11 4.3-2.6 7.5-6 7.5-11V5z" /><path d="m8.5 12 2.2 2.2 4.8-5" /></>,
    table: <><rect x="3" y="4" width="18" height="16" rx="2" /><path d="M3 10h18M9 10v10M15 10v10" /></>,
  };

  return (
    <svg
      aria-hidden="true"
      className={className}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      {paths[name] || paths.dashboard}
    </svg>
  );
} 
