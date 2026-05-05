"""Experiment ID generation and tracking utilities.

Each experiment gets a unique ID like 'EXP-20260505-143015-a3f9' that ties together:
- Lab notebook entries (docs/lab_notebook/experiments/)
- MLflow runs (tagged with exp_id)
- Output artifacts (outputs/<exp_id>/)
- Git commits (referenced in commit messages)
"""

from __future__ import annotations

import hashlib
import secrets
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from src.utils.logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class ExperimentID:
    """Stable, unique identifier for an experiment run.

    Attributes:
        timestamp: When the experiment started (ISO 8601, second precision).
        suffix: 4-character random hex for uniqueness within a second.
        custom_name: Optional human-friendly name (e.g., 'baseline', 'cot-T07').
    """

    timestamp: str
    suffix: str
    custom_name: str | None = None

    @classmethod
    def generate(cls, custom_name: str | None = None) -> ExperimentID:
        """Generate a new experiment ID."""
        return cls(
            timestamp=datetime.now().strftime("%Y%m%d-%H%M%S"),
            suffix=secrets.token_hex(2),
            custom_name=custom_name,
        )

    @classmethod
    def from_string(cls, exp_id: str) -> ExperimentID:
        """Parse an experiment ID from its string representation.

        Examples:
            >>> ExperimentID.from_string("EXP-20260505-143015-a3f9")
            >>> ExperimentID.from_string("EXP-20260505-143015-a3f9-baseline")
        """
        if not exp_id.startswith("EXP-"):
            raise ValueError(f"Experiment ID must start with 'EXP-': {exp_id}")
        parts = exp_id.removeprefix("EXP-").split("-")
        if len(parts) < 3:
            raise ValueError(f"Malformed experiment ID: {exp_id}")
        timestamp = f"{parts[0]}-{parts[1]}"
        suffix = parts[2]
        custom_name = "-".join(parts[3:]) if len(parts) > 3 else None
        return cls(timestamp=timestamp, suffix=suffix, custom_name=custom_name)

    def __str__(self) -> str:
        base = f"EXP-{self.timestamp}-{self.suffix}"
        return f"{base}-{self.custom_name}" if self.custom_name else base

    @property
    def short(self) -> str:
        """Short form for display: 'EXP-a3f9' or 'EXP-a3f9-baseline'."""
        base = f"EXP-{self.suffix}"
        return f"{base}-{self.custom_name}" if self.custom_name else base


@dataclass
class Experiment:
    """Container for experiment metadata and paths."""

    exp_id: ExperimentID
    output_dir: Path
    config_hash: str = ""
    git_commit: str = field(default_factory=lambda: _get_git_commit())

    @classmethod
    def create(
        cls,
        outputs_root: Path | str,
        custom_name: str | None = None,
    ) -> Experiment:
        """Create a new experiment with its own output directory."""
        exp_id = ExperimentID.generate(custom_name=custom_name)
        output_dir = Path(outputs_root) / str(exp_id)
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info("Created experiment %s at %s", exp_id, output_dir)
        return cls(exp_id=exp_id, output_dir=output_dir)


def _get_git_commit() -> str:
    """Get current git commit hash, or empty string if not in a git repo."""
    import subprocess

    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            timeout=2,
        )
        return result.stdout.strip()[:8]
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return ""


def hash_config(config_str: str) -> str:
    """Stable short hash of a config (for detecting duplicate experiments)."""
    return hashlib.sha256(config_str.encode("utf-8")).hexdigest()[:12]
