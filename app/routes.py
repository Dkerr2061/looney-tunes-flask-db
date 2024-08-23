# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from app import app, db, api
from flask import render_template


@app.route("/")
@app.route("/<int:id>")
def index(id=0):
    return render_template("index.html")
