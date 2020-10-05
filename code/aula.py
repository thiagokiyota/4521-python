#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, Response, request
import json
app = Flask("__name__")

@app.route("/jsonify")
def opt_jsonify():
    retorno = {
        "message": "Resposta usando jsoify"
    }
    return jsonify(retorno)

# make_response utilizado para controlar o código de resposta que por padrão no jsonify é código 200
@app.route("/make_response")
def opt_make_response():
    headers = {"content-type": "application/json"}
    retorno = {
        "message": "Resposta usando make_response"
    }
    return make_response(json.dumps(retorno), 201, headers)

@app.route("/response")
def opt_response():
    retorno = {
        "message": "Resposta usando response"
    }
    return Response(json.dumps(retorno), 201, content_type="application/json")

@app.route("/request", methods=["POST"])
def opt_request():
    retorno = request.get_json()
    return Response(json.dumps(retorno), 200, content_type="application/json")    

if __name__ == "__main__":
    app.run(debug=True)
