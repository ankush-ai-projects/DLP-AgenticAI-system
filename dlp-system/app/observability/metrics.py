"""Prometheus metrics with a no-op fallback for minimal local installs."""


class _NoopMetric:
    def labels(self, **kwargs):
        return self

    def inc(self, amount=1):
        return None

    def observe(self, value):
        return None


try:
    from prometheus_client import Counter, Histogram

    SCANS_TOTAL = Counter("dlp_scans_total", "DLP scans", ["asset_type", "status"])
    FINDINGS_TOTAL = Counter("dlp_findings_total", "Verified findings", ["entity_type", "risk"])
    AGENT_DURATION = Histogram("dlp_agent_duration_seconds", "Agent duration", ["agent"])
except ImportError:
    SCANS_TOTAL = FINDINGS_TOTAL = AGENT_DURATION = _NoopMetric()
