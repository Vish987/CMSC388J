from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError


from .models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=8, max=20)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")

class BudgetForm(FlaskForm):
    category = StringField("Category", validators=[InputRequired(), Length(min=1, max=50)])
    amount = FloatField("Amount", validators=[InputRequired()])
    start_date = DateField("Start Date", validators=[InputRequired()])
    end_date = DateField("End Date", validators=[InputRequired()])
    submit = SubmitField("Create Budget")

class ExpenseForm(FlaskForm):
    category = StringField("Category", validators=[InputRequired(), Length(min=1, max=50)])
    amount = FloatField("Amount", validators=[InputRequired()])
    description = StringField("Description", validators=[Length(max=200)])
    date = DateField("Date", validators=[InputRequired()])
    submit = SubmitField("Log Expense")