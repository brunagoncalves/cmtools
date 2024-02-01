""" Imports """
import base64
import datetime
from pymongo import TEXT
from bson import ObjectId
from flask import Blueprint, render_template, request, flash, redirect, url_for
from slugify import slugify
from extentions.database import mongo


postRoutes = Blueprint("postRoutes", __name__)


@postRoutes.route("/solutions/insert", methods=["GET", "POST"])
def insert_solution():
    """ Insert Post """

    if request.method == "GET":
        return render_template("posts/insert.html")
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
        mongo.cx.cmtools.posts.insert_one(
            {
                "title": title,
                "slug": slug,
                "date": datetime.datetime.now(),
                "author": author,
                "content": content,
                "image_base64": image_base64
            }
        )

        flash("Post inserido com sucesso!")
        return redirect(url_for("postRoutes.list_all_solutions"))


# @postRoutes.route("/solutions/list")
# def list_all_solutions():
#     """ Listar Post """
#     posts_cursor = mongo.cx.cmtools.posts.find()
#     posts = list(posts_cursor)
#     return render_template("posts/list.html", posts=posts)

@postRoutes.route("/solutions/list", methods=["GET"])
def list_all_solutions():
    """ Listar Post """
    # Crie um índice de texto na coleção 'posts' nos campos 'title' e 'content'
    mongo.cx.cmtools.posts.create_index([("title", TEXT), ("content", TEXT)])

    query = request.args.get(
        'query')  # Obter o parâmetro de consulta 'query' da URL
    if query:
        # Se houver uma consulta, encontrar posts que correspondam à consulta
        posts_cursor = mongo.cx.cmtools.posts.find(
            {"$text": {"$search": query}})
    else:
        # Caso contrário, retornar todos os posts
        posts_cursor = mongo.cx.cmtools.posts.find()

    posts = list(posts_cursor)
    return render_template("posts/list.html", posts=posts)


@postRoutes.route("/solutions/<string:slug>")
def view_solution(slug):
    """ Encontra o post corresponde ao slug """
    posts_cursor = mongo.cx.cmtools.posts.find()  # Buscar os posts novamente
    posts = list(posts_cursor)

    post_data = next((post for post in posts if post['slug'] == slug), None)
    if post_data:
        return render_template('posts/view.html', post=post_data)
    else:
        return 'Post not found', 404


@postRoutes.route("/solutions/delete/<string:solution_id>")
def delete_solution(solution_id):
    """ Delete post """
    result = mongo.cx.cmtools.posts.delete_one({"_id": ObjectId(solution_id)})
    if result.deleted_count == 1:
        flash("Solução excluida com sucesso!")
    else:
        flash("ID não encontrado")
    return redirect(url_for("postRoutes.list_all_solutions"))


@postRoutes.route("/solutions/edit/<string:solution_id>", methods=["GET", "POST"])
def edit_solution(solution_id):
    """ Editar post """
    if request.method == "GET":
        post_data = mongo.cx.cmtools.posts.find_one(
            {"_id": ObjectId(solution_id)})
        return render_template("posts/edit.html", post=post_data)
    else:
        # Obter dados do formulário de edição
        title = request.form.get('title')
        author = request.form.get('author')
        image_base64 = request.form.get('image_base64')
        content = request.form.get('content')

        # Atualizar os dados do post
        result = mongo.cx.cmtools.posts.update_one(
            {"_id": ObjectId(solution_id)},
            {"$set": {"title": title, "author": author,
                      "content": content, "image_base64": image_base64}}
        )

        if result.modified_count == 1:
            flash("Post atualizado com sucesso!")
        else:
            flash("Falha ao atualizar o post.")

        return redirect(url_for("postRoutes.list_all_solutions"))
