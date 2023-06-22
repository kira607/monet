from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class UserRegistrationForm(FlaskForm):
    """A form for user registration."""

    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email("Invalid Email")])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=50,
                message="Password length must be at least 8 and at most 50 characters",
            ),
        ],
    )
    password_confirmation = PasswordField(
        "Password Confirmation",
        validators=[
            EqualTo("password", "Passwords dot not match"),
        ],
    )
    submit = SubmitField("Let's go!")


class UserLoginForm(FlaskForm):
    """A form for user login."""

    email = StringField("Email", validators=[DataRequired(), Email("Invalid Email")])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me", default=False)
    submit = SubmitField("Login")
