#!/usr/bin/env python3

from flask import Flask, Response, render_template
import json

from grupos.blueprint import grupos_routes
from mensagens.blueprint import mensagens_routes
from users.blueprint import users_routes

app = Flask(__name__)
app.register_blueprint(grupos_routes)
app.register_blueprint(mensagens_routes)
app.register_blueprint(users_routes)

@app.route("/")
def index():
    return render_template(
        'index.html',
        title="Lista de nomes",
        nomes=[
            "João",
            "Gabriel",
            "Daniela",
            "Alice",
            "Edu"
        ]
    )

@app.route("/api")
def api():
    retorno = {
        "app": "Sistema de mensagens",
        "version": 1.0
    }
    return Response(
        json.dumps(retorno),
        200,
        content_type="application/json"
    )

if __name__ == "__main__":
    app.run(debug=True)
