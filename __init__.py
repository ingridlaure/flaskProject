from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '004f0993a6b9ef141c9975139332b81a'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anonyme:anonyme@localhost/projet_recette'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:postgresql://localhost:5432/projet_recette'
db = SQLAlchemy(app)

from . import routes
