""" Imports """
import os
from flask import Flask
from dotenv import load_dotenv
from extentions.database import mongo
from routes.post import postRoutes
from routes.main import home

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
app.config["SECRET_KEY"] = os.urandom(48)
mongo.init_app(app)
app.register_blueprint(home)
app.register_blueprint(postRoutes)


@app.route('/test')
def test():
    """ Teste Conexão """
    collection = mongo.cx.cmtools.posts
    collection.insert_one({'name': 'Cristina'})
    return '<h1>Conexão OK! Usuário envido cadastrado com sucesso!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
