from flask import render_template, url_for, flash, redirect
from cryass import app, db, crontab

from datetime import datetime

import ccxt
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
    # Binance
    
    exchange = Exchange.query.filter_by(name="Binance").first()
    
    if exchange:

        api_key = exchange.api_key
        api_secret = exchange.api_secret
        exchange_id = str(exchange.id)
        
        binance = ccxt.binance({'apiKey': api_key, 'secret':api_secret})
        balance = binance.fetchBalance()
        
        for bal in balance['total']:
            if balance['total'][bal] > 0:
                if bal.startswith("LD"):
                    account = "lending"
                    currency = bal[2:]
                else: 
                    account = "free"
                    currency = bal
                value = balance['total'][bal]
                dbbalance = Balance(exchange_id=exchange_id, account=account, currency=currency, balance=float(value))
                db.session.add(dbbalance)
        # Getting locked settings not shown in total balances
        balance = binance.sapiGetStakingPosition ({"product":"STAKING"})
        for bal in balance:
            if float(bal['amount']) > 0:
                dbbalance = Balance(exchange_id=exchange_id, account="locked", currency=bal['asset'], balance=float(bal['amount']))
                db.session.add(dbbalance)
        db.session.commit()

    # Huobi
    exchange = Exchange.query.filter_by(name="Huobi").first()
    if exchange:
        api_key = exchange.api_key
        api_secret = exchange.api_secret
        exchange_id = str(exchange.id)

        huobi = ccxt.huobi({'apiKey': api_key, 'secret':api_secret})
        balance = huobi.fetchBalance()
        for bal in balance['total']:
            if balance['total'][bal] > 0:
                account = "free"
                dbbalance = Balance(exchange_id=exchange_id, account=account, currency=bal, balance=float(balance['total'][bal]))
                db.session.add(dbbalance)

        db.session.commit()
    