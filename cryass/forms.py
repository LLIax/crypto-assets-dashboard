from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class BinanceForm(FlaskForm):
    binanceapi_key = StringField(label='API Key', validators=[DataRequired()])
    binanceapi_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    binanceenable_dust = BooleanField(label='Enable automatic dusting')
    binanceassets = StringField(label='Assets to exclude')
    binancesubmit = SubmitField('Save')


class PoloniexForm(FlaskForm):
    poloniexapi_key = StringField(label='API Key', validators=[DataRequired()])
    poloniexapi_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    poloniexsubmit = SubmitField(label='Save')

class HuobiForm(FlaskForm):
    huobiapi_key = StringField(label='API Key', validators=[DataRequired()])
    huobiapi_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    huobisubmit = SubmitField(label='Save')

class GateIOForm(FlaskForm):
    gateioapi_key = StringField(label='API Key', validators=[DataRequired()])
    gateioapi_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    gateiosubmit = SubmitField(label='Save')

class CoinexForm(FlaskForm):
    coinexapi_key = StringField(label='API Key', validators=[DataRequired()])
    coinexapi_secret = PasswordField(label='API Secret', validators=[DataRequired()])
    coinexsubmit = SubmitField(label='Save')