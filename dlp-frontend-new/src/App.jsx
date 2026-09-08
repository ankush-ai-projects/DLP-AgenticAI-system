import { useEffect, useState } from 'react';
import {
  BrowserRouter,
  Navigate,
  Outlet,
  Route,
  Routes,
} from 'react-router-dom';

import './App.css';
import AgenticScanConsole from './components/AgenticScanConsole';
import Home from './components/Home';
import Login from './components/Login';
import NeonDashboard from './components/NeonDashboard';
import PremiumHeader from './components/PremiumHeader';
import Register from './components/Register';
import ScanResult from './components/ScanResult';
import ScanStatus from './components/ScanStatus';

// TEMPORARY: login is being skipped so the app opens straight on the
// dashboard while auth is wired up properly later. Flip this back to
// `false` to restore the normal login-required flow -- Login/Register
// and the token-based guards below are untouched, just not enforced.
//
// NOTE: the backend still requires a valid JWT on every protected
// endpoint (assets, dashboard, agentic-scans). With no token, those API
// calls will fail with 401 and the dashboard/console will show empty or
// error states -- skipping the login *screen* doesn't skip backend auth.
const SKIP_LOGIN = true;

const TOKEN_STORAGE_KEY = 'token';
const USER_STORAGE_KEY = 'user';

function readStoredUser() {
  try {
    return JSON.parse(localStorage.getItem(USER_STORAGE_KEY) || 'null');
  } catch {
    localStorage.removeItem(USER_STORAGE_KEY);
    return null;
  }
}

function PublicOnlyRoute({ token, children }) {
  return token ? <Navigate to="/dashboard" replace /> : children;
}

function ProtectedLayout({ token, user, onLogout }) {
  if (!token && !SKIP_LOGIN) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div className="protected-app-shell">
      <PremiumHeader user={user} onLogout={onLogout} />
      <div className="protected-app-content">
        <Outlet />
      </div>
    </div>
  );
}

export default function App() {
  const [token, setToken] = useState(
    localStorage.getItem(TOKEN_STORAGE_KEY),
  );
  const [user, setUser] = useState(readStoredUser);

  useEffect(() => {
    if (token) {
      localStorage.setItem(TOKEN_STORAGE_KEY, token);
      return;
    }

    localStorage.removeItem(TOKEN_STORAGE_KEY);
  }, [token]);

  useEffect(() => {
    if (user) {
      localStorage.setItem(USER_STORAGE_KEY, JSON.stringify(user));
      return;
    }

    localStorage.removeItem(USER_STORAGE_KEY);
  }, [user]);

  const handleLogin = (accessToken, userData) => {
    setToken(accessToken);
    setUser(userData);
  };

  const handleLogout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem(TOKEN_STORAGE_KEY);
    localStorage.removeItem(USER_STORAGE_KEY);
  };

  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route
            path="/"
            element={
              SKIP_LOGIN ? (
                <Navigate to="/dashboard" replace />
              ) : (
                <PublicOnlyRoute token={token}>
                  <Home />
                </PublicOnlyRoute>
              )
            }
          />

          <Route
            path="/login"
            element={
              <PublicOnlyRoute token={token}>
                <Login onLogin={handleLogin} />
              </PublicOnlyRoute>
            }
          />

          <Route
            path="/register"
            element={
              <PublicOnlyRoute token={token}>
                <Register onLogin={handleLogin} />
              </PublicOnlyRoute>
            }
          />

          <Route
            element={
              <ProtectedLayout
                token={token}
                user={user}
                onLogout={handleLogout}
              />
            }
          >
            <Route path="/dashboard" element={<NeonDashboard />} />
            <Route path="/agentic" element={<AgenticScanConsole />} />
            <Route path="/scan-status" element={<ScanStatus />} />
            <Route
              path="/scan-results/:scanId"
              element={<ScanResult />}
            />
          </Route>

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
