.PHONY: help install install-dev sync clean test lint format check pre-commit run-ci

# Default target — show help
help:
	@echo "Available commands:"
	@echo "  make install       — install runtime dependencies"
	@echo "  make install-dev   — install runtime + dev dependencies"
	@echo "  make sync          — sync venv with uv.lock (after git pull)"
	@echo "  make test          — run all tests with coverage"
	@echo "  make lint          — run ruff linter (no fixes)"
	@echo "  make format        — auto-format code with ruff"
	@echo "  make check         — run lint + tests (CI-equivalent)"
	@echo "  make pre-commit    — run pre-commit on all files"
	@echo "  make clean         — remove caches and build artifacts"
	@echo "  make run-ci        — run the full CI suite locally"

# Dependencies
install:
	uv sync

install-dev:
	uv sync --extra dev

sync:
	uv sync --extra dev

# Testing
test:
	uv run pytest tests/ -v --tb=short --cov=src --cov-report=term-missing

# Code quality
lint:
	uv run ruff check src/ tests/ scripts/

format:
	uv run ruff format src/ tests/ scripts/
	uv run ruff check --fix src/ tests/ scripts/

check: lint test

pre-commit:
	uv run pre-commit run --all-files

run-ci: check pre-commit

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build dist htmlcov .coverage
