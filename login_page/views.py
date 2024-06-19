import flask
import flask_login
from registration_page.models import User

def show_login():

    confirmed = True
    if flask.request.method == "POST":
        confirmed = False
        name = flask.request.form["name"]
        password = flask.request.form["password"]
        users = User.query.all()


        for user in users:
            if user.name == name and user.password == password or user.email == name and user.password == password:
                flask_login.login_user(user)
                return flask.redirect("/")
                
    return flask.render_template("login.html", confirmed = confirmed, link="None")