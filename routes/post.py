""" Imports """
import base64
import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for
from slugify import slugify
from extentions.database import mongo


postRoutes = Blueprint("postRoutes", __name__)


@postRoutes.route("/insert_post", methods=["GET", "POST"])
def insert_post():
    """ Insert Post """

    if request.method == "GET":
        return render_template("posts/insert_post.html")
    else:
        title = request.form.get('title')
        slug = slugify(title)
        author = request.form.get('author')
        content = request.form.get('content')

        # Calculando o hash da imagem
        image = request.files['image']
        image_data = image.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        # Criando novo post
        post_data = {
            "title": title,
            "slug": slug,
            "date": datetime.datetime.now(),
            "author": author,
            "content": content,
            "image_base64": image_base64
        }

        post_id = mongo.cx.cmtools.posts.insert_one(post_data).inserted_id

        flash(f"Post inserido com sucesso!{post_id}")
        return redirect(url_for("postRoutes.insert_post"))


@postRoutes.route("/list_posts")
def list_posts():
    """ Listar Post """
    posts_cursor = mongo.cx.cmtools.posts.find()
    posts = list(posts_cursor)
    return render_template("posts/list_posts.html", posts=posts)


@postRoutes.route("/post/<string:slug>")
def post(slug):
    """ Encontra o post corresponde ao slug """
    posts_cursor = mongo.cx.cmtools.posts.find()  # Buscar os posts novamente
    posts = list(posts_cursor)

    post_data = next((post for post in posts if post['slug'] == slug), None)
    if post_data:
        return render_template('posts/post.html', post=post_data)
    else:
        return 'Post not found', 404
