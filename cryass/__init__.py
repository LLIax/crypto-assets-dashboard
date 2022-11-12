
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_crontab import Crontab

app = Flask(__name__)

app.config['SECRET_KEY'] ='6734a63ba14b2ab5a397a44b81d3fcc0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/lliax/crypto-assets/database.db'

db = SQLAlchemy(app)

app.app_context().push()

crontab = Crontab(app)

""" 
Init_db: 

Run in terminal
    >python
    >>>from app import app
    >>>from app import db
    >>>db.create_all()

TODO: Write init_db script
"""



from cryass import routes 
from cryass import crontasks