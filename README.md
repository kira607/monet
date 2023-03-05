# budget

![Tests](https://github.com/kira607/yaba/actions/workflows/tests.yaml/badge.svg)

A web app for planning, analysis, and visualization of the personal and company budget.

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