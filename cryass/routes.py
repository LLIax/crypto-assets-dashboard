from flask import render_template, url_for, flash, redirect
from cryass import app, db
from cryass.forms import BinanceForm, PoloniexForm
from cryass.models import Exchange, Balance

from binance import Client
from datetime import datetime
from binance.exceptions import BinanceAPIException
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
    
    poloniexform = PoloniexForm()
    if poloniexform.poloniexsubmit.data and poloniexform.validate_on_submit():
        exchange = Exchange(name="Poloniex", api_key=poloniexform.poloniexapi_key.data, api_secret=poloniexform.poloniexapi_secret.data, is_active=True)
        db.session.add(exchange)
        db.session.commit()
        flash(f'Poloniex API key {poloniexform.poloniexapi_key.data} saved', 'success')
    
    # TODO: separate setting pages
    return render_template('settings.html', binanceform=binanceform, poloniexform=poloniexform, title = 'Settings')

@app.route("/binance", methods=['GET','POST'])
def binance():
    assets = ('BNB', 'BTC', 'BCH', 'USDT', 'BUSD', 'TRX', 'DOGE', 'NFT')
    
    dust = ""
    
    exchange = Exchange.query.filter_by(name="Binance").first()
    
    if exchange:

        api_key = exchange.api_key
        api_secret = exchange.api_secret
        exchange_id = str(exchange.id)
        
        client = Client(api_key, api_secret)

        info = client.get_account()
        
        for balance in info["balances"]:
            return(balance)
            if float(balance["free"]) > 0:
                # listing of coins on Earn wallet to ledger file
                return(balance)
                
                
                #balance = Balance(exchange_id=exchange_id, account="free", currency=balance["asset"], balance=float(balance["free"]))
                #return(str(balance))
                #db.session.add(balance)
                #db.session.commit()
                #except Exception as e:
                #    return(f'caught {type(e)}: e')
            if float(balance["locked"]) >0:
                return(balance)
                #balance = Balance(exchange_id=exchange_id, account="free", currency=balance["asset"], balance=float(balance["locked"]))
                #return(str(balance))
                #db.session.add(balance)
                #db.session.commit()
        
    
