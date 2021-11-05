from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def default():
    users = User.read_all_users()
    return render_template("users.html",users=users)

@app.route('/user/new')
def create_user():
    return render_template("create_user.html")

@app.route('/add_user',methods = ["POST"])
def add_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create_user(data)
    return redirect("/users")

@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id":id
    }
    user = User.read_user(data)
    return render_template("user.html",user=user)

@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        "id":id
    }
    user = User.read_user(data)
    return render_template("user_edit.html",user=user)

@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    data = {
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    User.update_user(data)
    return redirect("/users")

@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect("/users")