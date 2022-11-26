from flask import render_template, url_for, flash, redirect
from cryass import app, db, crontab
from binance import Client
from datetime import datetime
from binance.exceptions import BinanceAPIException
import json


@crontab.job(minute="0", hour="21")
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
    
    exchange = Exchange.query.filter_by(name="Binance").first()
    
    if exchange:

        api_key = exchange.api_key
        api_secret = exchange.api_secret
        exchange_id = str(exchange.id)
        
        client = Client(api_key, api_secret)
        

        info = client.get_account()
        
        for balance in info["balances"]:
            
            if float(balance["free"]) > 0:
                # listing of coins on Earn wallet to ledger file
                if balance["asset"].startswith("LD"):
                    account = "lending"
                    currency = balance["asset"][2:]
                else:
                    account = "free"
                    currency = balance["asset"]

                dbbalance = Balance(exchange_id=exchange_id, account=account, currency=currency, balance=float(balance["free"]))
                db.session.add(dbbalance)

            if float(balance["locked"]) > 0:
                # listing of coins on Earn wallet to ledger file
                if balance["asset"].startswith("LD"):
                    account = "lending-locked"
                    currency = balance["asset"][2:]
                else:
                    account = "locked"
                    currency = balance["asset"]

                dbbalance = Balance(exchange_id=exchange_id, account="locked", currency=balance["asset"], balance=float(balance["locked"]))
                db.session.add(dbbalance)
        db.session.commit()
    exchange = Exchange.query.filter_by(name="Huobi").first()
    if exchange:
        api_key = exchange.api_key
        api_secret = exchange.api_secret

        huobi = ccxt.huobi({'apiKey': api_key, 'secret':api_secret})
        balance = huobi.fetchBalance()
            