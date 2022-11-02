from flask import Flask, render_template, url_for

app = Flask(__name__)

exchanges =[
    {
        'name': 'Binance',
        'logo': '/static/img/binance.svg'
    },
    {
        'name': 'Poloniex',
        'logo': '/static/img/poloniex.svg'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', title = 'Main page')

@app.route("/settings")
def settings():
    return render_template('settings.html', exchanges = exchanges, title = 'Settings')
