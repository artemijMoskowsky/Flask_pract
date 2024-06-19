import flask
import flask_login
from shop_page.models import Product

def show_basket():


    is_admin = False

    try:

        is_admin = flask_login.current_user.is_admin

        user_name = flask_login.current_user.name
    
    except:
        user_name = ""

    products_list = []
    product_unique_id_list = []
    id_counts = []

    try:
        product_ids = flask.request.cookies.get("products").split(" ")
        
        for id in product_ids:
            if id not in product_unique_id_list:
                product_unique_id_list.append(id)
            # products_list.append(Product.query.get(id))

        for unique_id in product_unique_id_list:
            count = 0
            for id in product_ids: # первый который второй 
                if unique_id == id:
                    count = count + 1
            id_counts.append(count)
        
        for unique_id in product_unique_id_list:
            product_info = Product.query.get(unique_id)
            product = Product(
                id = product_info.id,
                name = product_info.name,
                price = product_info.price,
                description = product_info.description,
                discount = product_info.discount,
                count = id_counts[product_unique_id_list.index(unique_id)]
            )
            products_list.append(product)

    except:
        pass
    
    return flask.render_template(template_name_or_list = "basket.html", user_name = user_name, link = "basket", products = products_list, is_admin = is_admin)