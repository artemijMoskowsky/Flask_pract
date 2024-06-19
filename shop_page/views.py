# 
import flask
# 
import flask_login
# 
import sqlite3
# 
from .models import Product
# 
import os



# def data_update(command):

#     database = sqlite3.connect( database = os.path.abspath(__file__ + "/../.." + "/shop_project/data.db"))

#     cursor = database.cursor()

#     cursor.execute(command)

#     database.commit()

#     database.close()
# 
def show_shop():
    # data_update("INSERT INTO product (name, price, description, count, discount) VALUES ( 'iPhone 15 Pro Max 256GB Natural Titanium', '49999', '256 Гб', '5', '15') ")
    # data_update("INSERT INTO product (name, price, description, count, discount) VALUES ( 'iPhone 15 Pro Max 512GB Natural Titanium', '65999', '512 Гб', '2', '25') ")
    # data_update("INSERT INTO product (name, price, description, count, discount) VALUES ( 'iPhone 15 Pro Max 256GB Natural Titanium', '49999', 'TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST', '3', '5') ")
    # data_update("INSERT INTO product (name, price, description, count) VALUES ( 'iPhone 15 Pro Max 256GB Natural Titanium', '56999', '512 Гб', '2') ")
    # data_update("INSERT INTO product (name, price, description, count) VALUES ( 'iPhone 15 Pro Max 256GB Natural Titanium', '66999', '1 Тб', '6') ")
    # data_update("INSERT INTO product (name, price, description, count) VALUES ( 'iPhone 15 Pro Max 256GB Natural Titanium', '49999', 'TestTestTest Test estT stTe  tTe Test estT  stTes tTest Test TestTes  tTestTes TestTestT stTes Tes tTestTes tTestT estTestTes tTestTe tTestTe tTestTe TestTes estTest estTes estTestT est Test', '0') ")

    

    is_admin = False

    try:

        is_admin = flask_login.current_user.is_admin
        user_name = flask_login.current_user.name
    # 
    except:
        # 
        user_name = ""
    #  #  # 
    return flask.render_template(template_name_or_list = "shop.html", user_name=user_name, link="shop", products = Product.query.all(), is_admin = is_admin)