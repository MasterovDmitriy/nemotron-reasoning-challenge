"""Smoke test to verify the testing infrastructure works."""


def test_imports() -> None:
    """Verify that the main src package can be imported."""
    import src  # noqa: F401


def test_truth() -> None:
    """Sanity check."""
    assert 1 + 1 == 2
