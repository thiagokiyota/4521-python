#!/usr/bin/env python3

from flask import Blueprint, render_template, redirect, url_for, session
import requests

gitlab_routes = Blueprint("gitlab", __name__, url_prefix="/gitlab")
token = "QT95C2zL6vBssWwsni6t"

@gitlab_routes.route("")
def index():
    if not "logged" in session or not session["logged"]:
        return redirect(url_for('index'))
    try:
        usuarios = requests.get("http://192.168.0.100/api/v4/users?private_token=%s"%(token))
        usuarios = usuarios.json()
        projetos = requests.get("http://192.168.0.100/api/v4/projects?private_token=%s"%(token))
        projetos = projetos.json()
    except Exception as error:
        return "%s"%(error)
    return render_template("gitlab.html", users=usuarios, projects=projetos)