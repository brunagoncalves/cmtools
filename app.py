""" Imports """
import os
from flask import Flask
# from flask_pymongo import PyMongo
from extentions.database import mongo
from routes.post import postRoutes
from routes.main import home

MONGO_URI = os.environ.get("MONGO_URI")

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
app.config["SECRET_KEY"] = os.urandom(48)
mongo.init_app(app)
# mongo = PyMongo(app)
app.register_blueprint(home)
app.register_blueprint(postRoutes)


@app.route('/test')
def test():
    """ Teste Conexão """
    collection = mongo.cx.cmtools.posts
    collection.insert_one({'name': 'Cristina'})
    collection.insert_one({'name': 'Derek'})
    return '<h1>Added a User!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
