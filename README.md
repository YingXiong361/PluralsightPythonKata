# core-python

This repository shows a minimal scaffold for a Python package using Poetry.

Structure
- `core_python/` — package root
  - `project1/`, `project2/`, `project3/` — example subpackages
- `tests/` — pytest tests

Quick start

1. Install Poetry (if not installed):

```pwsh
python -m pip install --upgrade pip
pip install poetry
```

2. Install dependencies and create a virtualenv managed by Poetry:

```pwsh
cd C:\Users\qchen\Documents\BaiduSyncdisk\kata\CorePython
poetry install
```

3. Run tests:

```pwsh
poetry run pytest -q
```

4. Build and publish (example):

```pwsh
poetry build
poetry publish --username __token__ --password "$POETRY_PYPI_TOKEN_PYPI"
```

Replace the package and module names as desired. This scaffold shows best-practice layout for publishing and CI.
