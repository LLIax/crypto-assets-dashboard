from flask import render_template, url_for, flash, redirect
from cryass import app, db
from cryass.forms import BinanceForm, PoloniexForm, HuobiForm
from cryass.models import Exchange, Balance

from binance import Client
from datetime import datetime
from binance.exceptions import BinanceAPIException
import ccxt
import json


@app.route("/")
def home():
    return render_template('home.html', title = 'Main page')

@app.route("/settings", methods=['GET','POST'])
def settings():
    
    binanceform = BinanceForm()
    if binanceform.binancesubmit.data and binanceform.validate_on_submit():
        exchange = Exchange(name="Binance", api_key=binanceform.binanceapi_key.data, api_secret=binanceform.binanceapi_secret.data, is_active=True)
        db.session.add(exchange)
        db.session.commit()
        flash(f'Binance API key {binanceform.binanceapi_key.data} saved', 'success')
    
    huobiform = HuobiForm()
    if huobiform.huobisubmit.data and huobiform.validate_on_submit():
        exchange = Exchange(name="Huobi", api_key=huobiform.huobiapi_key.data, api_secret=huobiform.huobiapi_secret.data, is_active=True)
        db.session.add(exchange)
        db.session.commit()
        flash(f'Huobi API key {huobiform.huobiapi_key.data} saved', 'success')

    poloniexform = PoloniexForm()
    if poloniexform.poloniexsubmit.data and poloniexform.validate_on_submit():
        exchange = Exchange(name="Poloniex", api_key=poloniexform.poloniexapi_key.data, api_secret=poloniexform.poloniexapi_secret.data, is_active=True)
        db.session.add(exchange)
        db.session.commit()
        flash(f'Poloniex API key {poloniexform.poloniexapi_key.data} saved', 'success')
    
    # TODO: separate setting pages
    return render_template('settings.html', binanceform=binanceform, poloniexform=poloniexform, huobiform=huobiform, title = 'Settings')

@app.route("/binance", methods=['GET','POST'])
def binance():
    
    exchange = Exchange.query.filter_by(name="Huobi").first()
    
    if exchange:

        
        api_key = exchange.api_key
        api_secret = exchange.api_secret
        #binance = ccxt.binance({'apiKey': api_key, 'secret':api_secret})
        huobi = ccxt.huobi({'apiKey': api_key, 'secret':api_secret})
        balance = huobi.fetchBalance()
        #balance = binance.sapiGetStakingPosition ({"product":"STAKING"})
        #balance = binance.fetchAccountPositions()
        #balance = binance.fetch_balance({'type':'interest'})
        outp = {}
        for bal in balance['total']:
            if balance['total'][bal] > 0:
                outp[bal]=balance['total'][bal] 

        return(outp)#    return(f'caught {type(e)}: e')
            
    
