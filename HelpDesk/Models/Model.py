from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("run")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String(),unique=True)

    def __init__(self,nome="",email=""):
        self.nome = nome
        self.email = email
