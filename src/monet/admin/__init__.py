"""Flask admin extention package."""

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from monet.orm import db

admin = Admin()

for model_class in db.Model.__subclasses__():
    admin.add_view(
        ModelView(model_class, db.session, endpoint=f"{model_class.__tablename__}_model")
    )
