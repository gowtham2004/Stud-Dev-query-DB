from flask import Blueprint, request, json, jsonify

views = Blueprint('views', __name__)

@views.route('/register', methods=["GET", "POST"])
def register():
    d={}
    if request.method =="POST":
        mail = request.form["email"]
        password = request.form["password"]
        return jsonify("welcome mr"+mail+password)


@views.route('/login', methods=["GET", "POST"])
def login():
    d = {}
    if request.method == "POST":
        mail = request.form["email"]
        password = request.form["password"]
        return jsonify("welcome back mr"+mail+password)