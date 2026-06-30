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

## Run Tests

Run all tests:

```bash
pytest -v
```

Run specific test:

```bash
pytest tests/test_browser_launch.py -v
```

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
