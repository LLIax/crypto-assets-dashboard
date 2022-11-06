from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class BinanceForm(FlaskForm):
    api_key = StringField(label='API Key', validators=[DataRequired()])
    api_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    enable_dust = BooleanField(label='Enable automatic dusting'),
    assets = StringField(label='Assets to exclude')
    binancesubmit = SubmitField('Sign Up')


class PoloniexForm(FlaskForm):
    api_key = StringField(label='API Key', validators=[DataRequired()])
    api_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    poloniexsubmit = SubmitField(label='Save')