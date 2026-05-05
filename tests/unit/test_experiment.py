"""Tests for experiment ID generation and parsing."""

from pathlib import Path

import pytest

from src.tracking.experiment import Experiment, ExperimentID, hash_config


class TestExperimentID:
    def test_generate_returns_valid_id(self) -> None:
        exp_id = ExperimentID.generate()
        assert str(exp_id).startswith("EXP-")
        assert len(exp_id.suffix) == 4

    def test_generate_with_custom_name(self) -> None:
        exp_id = ExperimentID.generate(custom_name="baseline")
        assert "baseline" in str(exp_id)

    def test_two_generates_are_different(self) -> None:
        exp_id1 = ExperimentID.generate()
        exp_id2 = ExperimentID.generate()
        # Even within the same second, suffix differs
        assert exp_id1.suffix != exp_id2.suffix or exp_id1.timestamp != exp_id2.timestamp

    def test_round_trip_parsing(self) -> None:
        original = ExperimentID.generate(custom_name="my-test")
        parsed = ExperimentID.from_string(str(original))
        assert parsed == original

    def test_round_trip_no_custom_name(self) -> None:
        original = ExperimentID.generate()
        parsed = ExperimentID.from_string(str(original))
        assert parsed == original

    def test_invalid_id_raises(self) -> None:
        with pytest.raises(ValueError, match="must start with"):
            ExperimentID.from_string("not-an-experiment")
        with pytest.raises(ValueError, match="Malformed"):
            ExperimentID.from_string("EXP-toofew")

    def test_short_form(self) -> None:
        exp_id = ExperimentID(timestamp="20260505-143015", suffix="a3f9", custom_name="cot")
        assert exp_id.short == "EXP-a3f9-cot"


class TestExperiment:
    def test_create_makes_output_dir(self, tmp_path: Path) -> None:
        exp = Experiment.create(outputs_root=tmp_path, custom_name="test")
        assert exp.output_dir.exists()
        assert exp.output_dir.is_dir()
        assert "test" in exp.output_dir.name


class TestHashConfig:
    def test_same_input_same_hash(self) -> None:
        assert hash_config("foo") == hash_config("foo")

    def test_different_input_different_hash(self) -> None:
        assert hash_config("foo") != hash_config("bar")

    def test_hash_is_short_hex(self) -> None:
        h = hash_config("test")
        assert len(h) == 12
        assert all(c in "0123456789abcdef" for c in h)
