from flask import render_template, url_for, flash, redirect
from cryass import app, db
from cryass.forms import BinanceForm, PoloniexForm
from cryass.models import Exchange, Balance


@app.route("/")
def home():
    return render_template('home.html', title = 'Main page')

@app.route("/settings", methods=['GET','POST'])
def settings():
    
    binanceform = BinanceForm()
    if binanceform.binancesubmit.data and binanceform.validate_on_submit():
        exchange = Exchange(name="Binance", api_key=binanceform.api_key.data, api_secret=binanceform.api_secret.data, is_active=True)
        db.session.add(exchange)
        db.session.commit()
        flash(f'Binance API key {binanceform.api_key.data} saved', 'success')
    
    poloniexform = PoloniexForm()
    if poloniexform.poloniexsubmit.data and poloniexform.validate_on_submit():
        flash(f'Poloniex API key {poloniexform.api_key.data} saved', 'success')
    
    # TODO: separate setting pages
    return render_template('settings.html', binanceform=binanceform, poloniexform=poloniexform, title = 'Settings')
