# Contributing to core-python

Thanks for your interest in contributing! This doc explains the minimal workflow to develop, test, and publish this project.

**Getting Started**
- **Clone:** `git clone <repo-url>`
- **Project root:** `C:\Users\qchen\Documents\BaiduSyncdisk\kata\CorePython`
- **Use Poetry (recommended):** This project uses Poetry to manage a self-contained virtualenv in `.venv`.

Quick setup (PowerShell):
```pwsh
cd C:\Users\qchen\Documents\BaiduSyncdisk\kata\CorePython
python -m pip install --upgrade pip
python -m pip install poetry
python -m poetry config virtualenvs.in-project true
python -m poetry install
```

**Coding & Style**
- **Formatter:** `black` (project includes pre-commit hooks)
- **Imports:** `isort`
- **Linting:** `flake8` via pre-commit optional

Install and run pre-commit hooks:
```pwsh
python -m poetry run pre-commit install
python -m poetry run pre-commit run --all-files
```

**Branching & Pull Requests**
- **Branch from:** `main` (create a feature branch `feature/your-change`)
- **Commit messages:** Use concise messages; Prefer Conventional Commits style for releases (optional)
- **Open PR:** Target `main`, include description, tests, and changelog notes if applicable.

**Running Tests**
- Run via Poetry (recommended):
```pwsh
python -m poetry run pytest -q
```
- Or using the created venv directly:
```pwsh
.venv\Scripts\python -m pytest -q
```

**Versioning & Publishing**
- Version is defined in `pyproject.toml`. To build and publish using Poetry:
```pwsh
python -m poetry build
# publish via token in CI or local env
python -m poetry publish --username __token__ --password "$POETRY_PYPI_TOKEN_PYPI"
```
- The repo includes a GitHub Actions `publish.yml` that publishes on tag pushes like `v1.2.3`.

**Reporting Issues**
- Open an issue on the repo with a clear title, steps to reproduce, and expected vs actual behavior.

**Contact & Help**
- If you need help, open an issue or reach out via the repo's discussion/PRs.

Thanks — contributions are welcome!