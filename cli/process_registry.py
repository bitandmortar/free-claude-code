"""Process registry and cleanup for free-claude-code."""

import os
import signal
from loguru import logger

def kill_all_best_effort():
    """Kill all subprocesses in the current process group as a safety net."""
    try:
        # In a real implementation, we would track PIDs.
        # This is a stub to allow the server to start.
        logger.info("CLI: performing best-effort process cleanup (stub)")
    except Exception as e:
        logger.error(f"CLI: cleanup error: {e}")
