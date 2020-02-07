from . import main
from flask import render_template

items = ["Python","Flask","Django"]
@main.route("/home")
def home():
    return render_template("home.html",name="MC24",items=items)
