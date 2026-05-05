"""Tests for seed-setting utilities."""

import os
import random

import numpy as np

from src.utils.seed import set_seed


class TestSetSeed:
    """Verify seed setting produces reproducible results."""

    def test_python_random_is_reproducible(self) -> None:
        set_seed(42)
        first = [random.random() for _ in range(5)]
        set_seed(42)
        second = [random.random() for _ in range(5)]
        assert first == second

    def test_numpy_random_is_reproducible(self) -> None:
        set_seed(42)
        first = np.random.rand(10)
        set_seed(42)
        second = np.random.rand(10)
        np.testing.assert_array_equal(first, second)

    def test_pythonhashseed_is_set(self) -> None:
        set_seed(123)
        assert os.environ["PYTHONHASHSEED"] == "123"

    def test_different_seeds_give_different_results(self) -> None:
        set_seed(42)
        first = np.random.rand(10)
        set_seed(43)
        second = np.random.rand(10)
        assert not np.array_equal(first, second)
