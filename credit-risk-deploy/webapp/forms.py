from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import Required, Email

class LoanForm(FlaskForm):
    amount = IntegerField(
        'Loan Amount',
        validators=[Required()])

    duration = IntegerField(
        'Loan Duration in Years',
        validators=[Required()])

    name = StringField(
        'Your Name',
        validators=[Required()])

    email = StringField(
        'Email address',
        validators=[Required(), Email()])

    age = IntegerField(
        'Your Age',
        validators=[Required()])

    income = IntegerField(
        'Anual Income',
        validators=[Required()])

    ownership = SelectField(
        'Home Ownership',
        choices = [
            ('RENT', 'Rent'),
            ('MORTGAGE', 'Mortgage'),
            ('OWN', 'Own'),
        ])
