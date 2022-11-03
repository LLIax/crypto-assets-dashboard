from flask import Flask, render_template, url_for
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
def hello_world():
    return render_template('home.html', title = 'Main page')

@app.route("/settings")
def settings():
    binanceform = BinanceForm()
    
    poloniexform = PoloniexForm()
    return render_template('settings.html', binanceform=binanceform, poloniexform=poloniexform, title = 'Settings')
