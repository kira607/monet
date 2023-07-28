from flask_restx import Model
from flask_restx.fields import String

user_model = Model(
    "User",
    {
        "id": String(),
        "email": String(),
        "first_name": String(),
        "last_name": String(),
    },
)
