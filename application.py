from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost:3306/mysql?charset=utf8'

db = SQLAlchemy(app)




