#!/usr/bin/env python3

from flask import Flask
app = Flask("__name__")

@app.route("/exemplo/<int:id>")
def hello(id):
    return "Hello World, %s" %(id)

@app.route("/teste")
def teste():
    return "Teste de nova rota"

if __name__ == "__main__":
    app.run(debug=True)
