import flask
import flask_login
from shop_page.models import Product

def show_home():
    is_admin = False

    try:

        is_admin = flask_login.current_user.is_admin
        user_name = flask_login.current_user.name
    except:
        user_name = ""

    list_products_ids = []
    for product in Product.query.all():
        list_products_ids.append(product.id)    
    return flask.render_template(template_name_or_list = "home.html", user_name = user_name, link = "home", is_admin = is_admin, list_products_ids = list_products_ids)