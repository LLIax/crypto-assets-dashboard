from flask import Flask, render_template, url_for, flash
from forms import BinanceForm, PoloniexForm

app = Flask(__name__)

app.config['SECRET_KEY'] ='6734a63ba14b2ab5a397a44b81d3fcc0'

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
