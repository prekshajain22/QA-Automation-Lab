# QA Automation Lab

## Overview

Playwright + Pytest BDD automation framework using Page Object Model (POM).

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest-BDD
- Ruff

## Quick Start

1. Create and activate virtualenv:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies and Playwright browsers:

```bash
pip install -r requirements.txt
playwright install
```

3. Add environment overrides in a `.env` file (optional):

```
BASE_URL=https://www.saucedemo.com
BROWSER=chromium
HEADLESS=True
DEFAULT_TIMEOUT=5000
```

## Running Tests (Common Commands)

- Run all tests: `pytest -v`
- Run a single feature or test file: `pytest tests/test_browser_launch.py -v`
- Run tests matching a marker: `pytest -m smoke -v`
- Run tests in parallel: `pytest -n auto -v`
- Run a specific BDD scenario by name: `pytest -k "Login with standard user" -v`

## Cross-browser

Set `BROWSER` in `.env` or the environment to `chromium`, `firefox`, or `webkit` and run `pytest -v`.

## Conventions & Project Layout

- `components/` — reusable UI element wrappers (Button, TextInput, Label).
- `pages/` — Page Objects that compose components and expose page-level actions.
- `actions/` — (Optional) business-level workflows that orchestrate multiple page calls. Keep or remove based on suite size.
- `fixtures/` — pytest fixtures (browser, pages, data, screenshots).
- `tests/step_definitions/` — BDD step implementations for feature files.
- `features/` — Gherkin feature files.

## Adding Tests

1. Add a new feature file in `features/`.
2. Add step implementations in `tests/step_definitions/` or extend `tests/step_definitions/shared_steps.py` for shared steps.
3. Add page helper methods in `pages/` and components in `components/` as needed.

## Code Quality & Tooling

- Format: `ruff format .`
- Lint: `ruff check .`
- Recommended: add `pre-commit` configured to run `ruff` and tests on commit.

## CI Suggestions

- Install Python dependencies and Playwright browsers in CI.
- Run `ruff check .` then `pytest -n auto -v` and publish `reports/test_report.html` as an artifact.

## Troubleshooting

- If you see `ModuleNotFoundError` for local modules, ensure the virtualenv is activated and imports are package-style (e.g., `from config.settings import ...`).
- Clear Python cache if stale imports occur: `Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force` (PowerShell) or `find . -name "__pycache__" -exec rm -r {} +` (Unix).
- If Playwright can't find browsers, run `playwright install`.

## Contribution

- Open a feature branch, add tests, run the suite locally, and open a PR with a short description.

---

# Running the QA Automation Workflow

## 1. Start the n8n Container

```powershell
podman stop n8n
podman start n8n
podman ps
```

## 2. Start the Flask API

Open a new PowerShell window.
Navigate to the project folder and Activate the virtual environment.

```powershell
.\.venv\Scripts\Activate.ps1

Then Run the Flask service.
python automation_services\test_runner.py
```

Leave this terminal running.

## 3. Open n8n

Open your browser and navigate to:

```
http://localhost:5678
```

Execute the workflow.

## 4. Test the Flask API (Optional)

Open another PowerShell window.

```powershell
Invoke-WebRequest http://localhost:5000/run-tests -UseBasicParsing
```

This will execute the test suite and return the JSON response produced by the Flask API.
