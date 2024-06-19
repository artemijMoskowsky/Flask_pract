import flask 



from .models import User

import sqlite3
import os

from shop_project.settings import data_base

# def data_update(command):

#     database = sqlite3.connect( database = os.path.abspath(__file__ + "/../.." + "/shop_project/data.db"))

#     cursor = database.cursor()

#     cursor.execute(command)

#     database.commit()

#     database.close()

def show_regestration():

    confirmed = False

    # data_update("INSERT INTO admin (name, email, password) VALUES ( 'Admin', 'artemij.mosckowsky.01062008@gmail.com', 'admin_password777' ) ")

    if flask.request.method == "POST":
        
        name = flask.request.form["name"]

        email = flask.request.form["email"]
        
        password = flask.request.form["password"]

        password_confirm = flask.request.form["password_confirm"]

        try:

            users = User.query.all()

            is_user = False

            if password == password_confirm:

                for user in users:
                
                    if user.name == name and user.password == password:
                    
                        is_user = True
    
                if not is_user:
                
                    confirmed = True

                    new_user = User(name = name, email = email, password = password, is_admin = False)
    
                    data_base.session.add(new_user)
    
                    data_base.session.commit()

        except Exception as _ex:

            print(_ex)
  
    return flask.render_template("registration.html", confirmed = confirmed, link="None")