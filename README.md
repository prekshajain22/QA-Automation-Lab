# QA Automation Lab

## Overview

Playwright + Pytest BDD automation framework using Page Object Model (POM).

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest-BDD
- Ruff

## Setup

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Install parallel execution support:

pip install pytest-xdist

## Run Tests

Run all tests:

```bash
pytest -v
```

Run specific test:

```bash
pytest tests/test_browser_launch.py -v
```

## Run tests in parallel

pytest -n auto -v

or

pytest -n 2 -v

## Cross-browser execution

Set browser in .env:

BROWSER=chromium | firefox | webkit

Run tests:

pytest -v

Same test suite runs across different browsers without code changes.

## Code Quality

Format code:

```bash
ruff format .
```

Lint:

```bash
ruff check .
```

## Framework Highlights

- Page Object Model for reusable page actions
- BDD feature files using Pytest-BDD
- External test data using JSON
- Reusable pytest fixtures
- Logging support
- Automatic screenshots on test failure

## Reports

Execution logs:

```
reports/logs/execution.log
```
