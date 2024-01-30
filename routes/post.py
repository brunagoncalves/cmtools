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
    posts = mongo.cx.cmtools.posts.find()
    return render_template("posts/list_posts.html", posts=posts)


@postRoutes.route("/edit_post")
def edit_post():
    """ Editar Post """
    return render_template("posts/edit_post.html")


@postRoutes.route("/delete_post")
def delete_post():
    """ Editar Post """
    return "delete"
