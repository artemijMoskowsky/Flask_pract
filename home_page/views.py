import flask
import flask_login

def show_home():
    is_admin = False

    try:

        is_admin = flask_login.current_user.is_admin
        user_name = flask_login.current_user.name
    except:
        user_name = ""    
    return flask.render_template(template_name_or_list = "home.html", user_name = user_name, link = "home", is_admin = is_admin)