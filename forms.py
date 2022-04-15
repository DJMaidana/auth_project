from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit  = SubmitField("Enter")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    register = SubmitField("Create User")