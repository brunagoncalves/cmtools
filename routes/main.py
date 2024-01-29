""" Imports """
from flask import Blueprint, render_template

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    """ Route Home """
    return render_template("/index.html")
