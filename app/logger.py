"""Application-wide logger configuration."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("task-api")
"""Module-level logger instance for the Task Management API."""
