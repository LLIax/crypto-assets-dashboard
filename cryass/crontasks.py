from flask import render_template, url_for, flash, redirect
from cryass import app, db, crontab
from binance import Client
from datetime import datetime


@crontab.job(minute="20", hour="18")
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
    with open('readme.txt', 'w') as f:
        f.write('readme')



from binance.exceptions import BinanceAPIException

api_key = "8IfPZfCcZzvQfjVpIEOfRPlDIGgDH89OHuSXD640OhVhblgM1aPGy2LwgesoiQZu"
api_secret = "oirrqn8TRtXs7tlULtoqutx8KYf7CkfX3Lg75cdhWKs9UQ76eyElM9UvoEzVTsFJ"

# list of assets not to  be dusted
assets = ('BNB', 'BTC', 'BCH', 'USDT', 'BUSD', 'TRX', 'DOGE', 'NFT')

dust = ""

client = Client(api_key, api_secret)

info = client.get_account()
print()
print(str(datetime.date(datetime.now())) + " * Binance")
for balance in info["balances"]:
    if float(balance["free"]) > 0 or float(balance["locked"]) >0:
        # listing of coins on Earn wallet to ledger file
        if balance["asset"].startswith("LD"):
            print("    assets:crypto:binance   = " + balance["asset"][2:]+ " " + balance["free"])
        elif balance["asset"] not in assets:
            if dust:
                dust = dust + ", "
            dust = dust + balance["asset"]
print("    income:crypto:interest")
if dust:
    try:
        cmdbnb = str('(asset="' + dust + '")')
        cmdbnb = "client.transfer_dust" + cmdbnb
        #print(cmdbnb)
        result = exec(cmdbnb)
    except:
        print ("; error dedusting"+ str(result))