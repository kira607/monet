Yaba deployment
===============

To deploy yaba:

1. Create a pull request with a feature.
2. Merge pull request
3. Go to pythonanywhere
4. Open a consolve under yaba venv
5. Apply migrations
    ```bash
    flask db upgrade
    ```
6. If required, reinstall app with fresh dependencies:
    ```bash
    ~/yaba $ pip install -e --force-reinstall .
    ```
7. Reload app
