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
