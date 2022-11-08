from datetime import datetime
from flask import Flask, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BinanceForm, PoloniexForm

app = Flask(__name__)

app.config['SECRET_KEY'] ='6734a63ba14b2ab5a397a44b81d3fcc0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/lliax/crypto-assets/database.db'

db = SQLAlchemy(app)

app.app_context().push()

""" 
Init_db: 

Run in terminal
    >python
    >>>from app import app
    >>>from app import db
    >>>db.create_all()

TODO: Write init_db script
"""

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    api_key = db.Column(db.String(255), nullable=False)
    api_secret = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    balances = db.relationship('Balance', backref='exchange', lazy=True)

    def __repr__(self):
        return f"Exchange('{self.name}', '{self.api_key}')"

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'), nullable=False)
    account = db.Column(db.String(255), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Balance('{self.exchange_id}', '{self.account}', '{self.currency}', '{self.balance}', '{self.data}')"


exchanges =[
    {
        'name': 'Binance',
        'logo': '/static/img/binance.svg', 
        
    },
    {
        'name': 'Poloniex',
        'logo': '/static/img/poloniex.svg',
        
    }
]

@app.route("/")
def home():
    return render_template('home.html', title = 'Main page')

@app.route("/settings", methods=['GET','POST'])
def settings():
    
    binanceform = BinanceForm()
    if binanceform.binancesubmit.data and binanceform.validate_on_submit():
        flash(f'Binance API key {binanceform.api_key.data} saved', 'success')
    
    poloniexform = PoloniexForm()
    if poloniexform.poloniexsubmit.data and poloniexform.validate_on_submit():
        flash(f'Poloniex API key {poloniexform.api_key.data} saved', 'success')
    
    # TODO: separate setting pages
    return render_template('settings.html', binanceform=binanceform, poloniexform=poloniexform, title = 'Settings')
