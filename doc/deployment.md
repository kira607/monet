Yaba deployment
===============

To deploy yaba:

* Create a pull request with a feature.
* Merge pull request
* Go to pythonanywhere
* If required update environment variables.
* Open a consolve under yaba venv
* Apply migrations
    ```bash
    flask db upgrade
    ```
* If required, reinstall app with fresh dependencies:
    ```bash
    ~/yaba $ pip install -e --force-reinstall .
    ```
* Reload app
