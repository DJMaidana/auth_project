from wsgiref.validate import validator
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

db.create_all()

import models, routes