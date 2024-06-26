# Імпортуємо Flask
import flask
# Імпортуємо Flask_login
import flask_login
# Імпортуємо клас з моделю нашого продукта
from .models import Product

# Створюємо функція для відображення продукта
def show_shop():    
    # Задаєтся початкове значення is_admin
    is_admin = False
    # Задаєтся початкове значення user_name
    user_name = ""
    try:
        # Перезаписує значення is_admin, спираючись на значення користувача     
        is_admin = flask_login.current_user.is_admin
        # Перезаписує значення user_name, спираючись на значення користувача  
        user_name = flask_login.current_user.name
    

    except:
        pass
    # Створюємо список для збереження (id) продуктів
    list_products_ids = []
    # Перебираємо список продуктів
    for product in Product.query.all():
        # Додаємо id продуктів в список
        list_products_ids.append(product.id)    
    # Відтворюємо сторінку магазину, передаючі усі необхідні параметри
    return flask.render_template(template_name_or_list = "shop.html", user_name=user_name, link="shop", products = Product.query.all(), is_admin = is_admin, list_products_ids = list_products_ids)