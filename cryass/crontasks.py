from flask import render_template, url_for, flash, redirect
from cryass import app, db, crontab
from binance import Client
from datetime import datetime
from binance.exceptions import BinanceAPIException
import json


@crontab.job(minute="35", hour="21")
def scheduled_job():
    """
    TODO: implement exchanges polling
    An app context is automatically activated for every job run, so that you can access objects that are attached to app context. Then add the job to crontab:

    $ flask crontab add

    That's it! If you type in crontab -l in your shell, you can see some new lines created by flask-crontab.

    Show jobs managed by current app:

    $ flask crontab show

    Purge all jobs managed by current app:

    $ flask crontab remove
    https://pypi.org/project/flask-crontab/
    """
    # list of assets not to  be dusted
    
    assets = ('BNB', 'BTC', 'BCH', 'USDT', 'BUSD', 'TRX', 'DOGE', 'NFT')
    
    dust = ""

    exchange = Exchange.query.filter_by(name="Binance").first()
    if exchange:
        with open('readme.txt', 'w') as f:
            f.write(json.dumps(exchange))
        api_key = exchange.api_key
        api_secret = exchange.api_secret

        client = Client(api_key, api_secret)

        info = client.get_account()
        
 
            
        for balance in info["balances"]:
            if float(balance["free"]) > 0:
                # listing of coins on Earn wallet to ledger file
                balance = Balance(name="Binance", account="free", currency=balance["asset"], balance=balance["free"])
                db.session.add(balance)

            if float(balance["locked"]) >0:
                balance = Balance(name="Binance", account="free", currency=balance["asset"], balance=balance["free"])
                db.session.add(balance)
        db.session.commit()
    
