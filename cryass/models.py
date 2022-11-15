from datetime import datetime
from cryass import db

class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    api_key = db.Column(db.String(255), nullable=False)
    api_secret = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    balances = db.relationship('Balance', backref='exchange', lazy=True)

    def __repr__(self):
        return f"Exchange('{self.id}', '{self.name}', '{self.api_key}', '{self.api_secret}')"

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'), nullable=False)
    account = db.Column(db.String(255), nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Balance('{self.exchange_id}', '{self.account}', '{self.currency}', '{self.balance}', '{self.date}')"

