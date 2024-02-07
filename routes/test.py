""" Imports """
from flask import Blueprint
from extentions.database import mongo

testRoutes = Blueprint("testRoutes", __name__)


@testRoutes.route('/test/testMails')
def test_mails():
    """ Teste Conexão """
    collection = mongo.cx.cmtools.mails
    collection.insert_one({
        'email': 'suporte@suporte.com.br',
        'password': "senha123"
    })
    return '<h1>E-mail adicionado no banco!</h1>'


@testRoutes.route('/test/testPost')
def test_post():
    """ Teste Conexão """
    collection = mongo.cx.cmtools.posts
    collection.insert_one({
        'title': 'Post teste',
        'slug': "post-teste",
        'author': "Administrador",
        'content': "Adicionando um post teste!"
    })
    return '<h1>Post adicionado no banco!</h1>'


@testRoutes.route('/test/testPhone')
def test_phone():
    """ Teste Conexão """
    collection = mongo.cx.cmtools.phones
    collection.insert_one({
        'user': 'suporte@suporte.com.br',
        'phone': "48991736262",
        'whatsapp': "48991736262"
    })
    return '<h1>Telefone adicionado no banco!</h1>'
