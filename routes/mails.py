""" Imports """
from flask import Blueprint, render_template

mailsRoutes = Blueprint("mailsRoutes", __name__)


@mailsRoutes.route("/mails/insert")
def insert_mail():
    """ Inserir e-mails """
    return render_template("mails/insert.html")
