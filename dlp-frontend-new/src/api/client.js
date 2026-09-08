import axios from 'axios';

// Previously every component created its own axios call with a manually
// built Authorization header, and re-implemented formatApiError/
// redirectToLogin locally (4 separate copies, already drifting -- e.g.
// ScanResult.jsx's formatApiError didn't handle array-shaped FastAPI
// validation details the way AgenticScanConsole.jsx's did). This module
// is the single source of truth for all three.
//
// VITE_API_BASE_URL lets a production build point at a real backend host.
// Left empty, requests stay relative ('/api/v1/...') and rely on Vite's
// dev-server proxy (see vite.config.js) -- that only exists in `npm run
// dev`, so a production deployment MUST set VITE_API_BASE_URL (see
// .env.example) or serve the frontend behind a reverse proxy that maps
// /api to the backend itself.
// TEMPORARY: kept in sync with SKIP_LOGIN in App.jsx. While true, a 401
// (expected on every call, since there's no token yet) does NOT bounce
// the user back to /login -- otherwise landing on /dashboard would
// immediately redirect away again on the first failed API call. Flip
// both flags back to false together when real auth is wired back in.
const SKIP_LOGIN = true;

const TOKEN_STORAGE_KEY = 'token';
const USER_STORAGE_KEY = 'user';

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '',
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem(TOKEN_STORAGE_KEY);

  if (token && !config.headers.Authorization) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401 && !SKIP_LOGIN) {
      localStorage.removeItem(TOKEN_STORAGE_KEY);
      localStorage.removeItem(USER_STORAGE_KEY);

      if (
        typeof window !== 'undefined' &&
        window.location.pathname !== '/login'
      ) {
        window.location.replace('/login');
      }
    }

    return Promise.reject(error);
  },
);

export function formatApiError(error) {
  const detail = error.response?.data?.detail;

  if (Array.isArray(detail)) {
    return detail.map((item) => item.msg || JSON.stringify(item)).join(', ');
  }

  if (detail && typeof detail === 'object') {
    return JSON.stringify(detail);
  }

  return detail || error.message || 'Request failed';
}
