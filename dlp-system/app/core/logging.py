"""Logging configuration"""
import logging
import logging.config
from pathlib import Path

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(filename)s:%(lineno)d: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": "logs/app.log",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
    "loggers": {
        # Our middleware keeps frequent scan polling at DEBUG. Suppress the
        # duplicate Uvicorn access line so the console remains readable.
        "uvicorn.access": {
            "level": "WARNING",
            "handlers": ["console", "file"],
            "propagate": False,
        },
        "sentineldlp.scan": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        },
        "sentineldlp.remediation": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        },
        "app.middleware.logging_middleware": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },
}


def setup_logging():
    """Initialize logging configuration"""
    Path("logs").mkdir(exist_ok=True)
    logging.config.dictConfig(LOGGING_CONFIG)
