# Імпортуємо Flask
import flask
# Імпортуємо Flask_login
import flask_login
# Із моделей додатку (shop) імпортуємо модель продуктів
from shop_page.models import Product
# Створюємо функцію відображення  
def show_home():
    # Завдаємо початкове значення для флагу (is_admin) * ДЛЯ ПЕРЕВІРКИ ЧИ КОРИСТУВАТЧ МАЄ ПРАВА АДМІНІСТРАТОРА *
    is_admin = False
    
    try:
        # Завдаємо значення для флагу, від поточного користувача * ДЛЯ ПЕРЕВІРКИ ЧИ КОРИСТУВАТЧ МАЄ ПРАВА АДМІНІСТРАТОРА * 
        is_admin = flask_login.current_user.is_admin
        # Стврорюємо змінну у якій буде зберігатися ім'я поточного користувача * ДЛЯ ВІДООБРАЖЕННЯ ІМЕНІ КОРИСТУВАЧА *  
        user_name = flask_login.current_user.name
    except:
        # Обнуляємо змінну імені користуватча * ДЛЯ ТОГО ЩОБ ІМЕНА НЕ ПОВТОРЮВАЛИСЬ І НЕ БУЛО ПОМИЛКИ *
        user_name = ""
    # Створюємо список з id продуктів
    list_products_ids = []
    # перебираємо список продуктів
    for product in Product.query.all():
        # Добовляємо у список (list_products_ids) останнім значенням id продукту, яке ми отримали у базі даних 
        list_products_ids.append(product.id)    
    # Відображаємо сторінку передаючі усі необхідні данні
    return flask.render_template(template_name_or_list = "home.html", user_name = user_name, link = "home", is_admin = is_admin, list_products_ids = list_products_ids)