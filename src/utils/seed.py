"""Reproducibility: fixing random seeds across all libraries."""

from __future__ import annotations

import os
import random

import numpy as np


def set_seed(seed: int) -> None:
    """Set random seeds for Python, NumPy, and PyTorch (if available).

    Sets the seed for:
    - Python's `random`
    - NumPy
    - `PYTHONHASHSEED` environment variable
    - PyTorch (CPU and CUDA), if installed
    - PyTorch's deterministic algorithms flag

    Note:
        Full determinism in PyTorch also requires:
        - `torch.backends.cudnn.deterministic = True`
        - `torch.backends.cudnn.benchmark = False`
        These are set automatically when PyTorch is available.

    Args:
        seed: Integer seed value (typically 42).
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        # PyTorch not installed yet — that's fine for early stages
        pass
