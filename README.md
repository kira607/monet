# yaba

![Tests](https://github.com/kira607/yaba/actions/workflows/tests.yaml/badge.svg)

A web app for planning, analysis, and visualization of the personal and company budget.

## Linting and Testing

From the repo root run:

1. This command to run mypy accorss sources and tests
    ```bash
    mypy src
    ```
2. This command to run tests:
    ```bash
    pytest
    ```
3. This command to run flake8 linter:
    ```bash
    flake8 src tests
    ```
4. This command to sort imports
    ```bash
    isort src tests
    ```
5. This command to run tox:
    ```bash
    tox
    ```

## Migrations

If db models are changed do following:

1. Create new version:
    ```bash
    flask db migrate -m "Migration message."
    ```
2. Check generated script (`migrations/version/<new_file>`)
3. Upgrade local database.
    ```bash
    flask db upgrade
    ```
4. After deployment upgrade prod database.