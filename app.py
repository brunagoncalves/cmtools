""" Imports """
import os
from flask import Flask
from dotenv import load_dotenv
from extentions.database import mongo
from routes.post import postRoutes
from routes.main import home

# Carrega as variáveis de ambiente armazenadas no arquivo .env
load_dotenv()
# Acessa a variável de ambiente MONGO_URI
MONGO_URI = os.getenv("MONGO_URI")

# Inicia a aplicação
app = Flask(__name__)
# Carrega o caminho do banco de dados armazenado na variável MONGO_URI configurada no arquivo .env
app.config["MONGO_URI"] = MONGO_URI
# Gerar chaves automáticas com 48 caracteres
app.config["SECRET_KEY"] = os.urandom(48)
# Inicializa o banco de dados
mongo.init_app(app)
# Blueprint - Organiza as rotas por grupos
app.register_blueprint(home)
app.register_blueprint(postRoutes)

# Rota simples para teste quando necessário


@app.route('/test')
def test():
    """ Teste Conexão """
    collection = mongo.cx.cmtools.posts
    collection.insert_one({
        'name': 'Teste de Conexão',
        'slug': "teste-de-conexao"
    })
    return '<h1>Conexão OK! Usuário envido cadastrado com sucesso!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
