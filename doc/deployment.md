Yaba deployment
===============

To deploy yaba:

* Create a pull request with a feature or bugfix.
* Merge pull request
* Check webhook
* Go to pythonanywhere
* If required update environment variables.
* Open a consolve under yaba venv
* source to .env
* If required, reinstall app with fresh dependencies:..
```bash
pip install --force-reinstall -e .
```
* Apply migrations..
```bash
flask db upgrade
```
* Reload app
