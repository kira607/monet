"""Flask CLI/Application entry point."""
import os

from monet.app import create_app
from monet.orm import db

app = create_app(os.getenv("FLASK_ENV", "dev"))


@app.shell_context_processor
def shell():
    return {"db": db}
