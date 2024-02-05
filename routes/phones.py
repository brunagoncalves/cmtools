""" Imports """
from flask import Blueprint, render_template

phoneRoutes = Blueprint("phoneRoutes", __name__)


@phoneRoutes.route("/phones/insert")
def insert_phone():
    """ Inserir ramais/whatsapp """
    return render_template("phones/insert.html")

@phoneRoutes.route("/phones/list")
def list_phone():
    """ Listar ramais/whatsapp """
    return render_template("phones/list.html")
