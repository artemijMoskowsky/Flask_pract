# Імпортуємо головний додаток.
from .settings import project_shop
# Імпортуємо додаток домашньої сторінки та функція відображення.
from home_page import home_app, show_home
# Імпортуємо додаток реєстрації та функція відображеня.
from registration_page import reg_app, show_regestration
# Імротуємо додаток логіну та функції відображення.
from login_page import login_app, show_login
# Імротуємо додаток корзини та функції відображення.
from basket_page import basket_app, show_basket
# Імротуємо додаток магазину та функції відображення.
from shop_page import shop_app, show_shop
# Імротуємо додаток контакту та функції відображення.
from contacts_page import contact_app, show_contacts
# Імротуємо додаток адміну та функції відображення.
from admin_page import admin_app, show_admin

# Додаємо налагодження додатку домашньої сторінки.
home_app.add_url_rule(
    # Додаємо посилання.
    rule = "/",
    # Додаємо функцію відображення.
    view_func = show_home,
)

# Додаємо налагодження додатку реєстрації.
reg_app.add_url_rule(
    # Додаємо посилання.
    rule = "/registration",
    # Додаємо функцію відображення реєстрації. 
    view_func = show_regestration,
    # Додаємо метод функції реєстрації.
    methods = ["GET", "POST"]
)

# Додаємо налагодження додатку логіну.
login_app.add_url_rule(
    # Додаємо посилання.
    rule = "/login",
    # Додаємо функцію відображення логіну
    view_func = show_login,
    # Додаємо метод функції логіну.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку корзини.
basket_app.add_url_rule(
    # Додаємо посилання.
    rule = "/basket",
    # Додаємо функцію відображення корзини.
    view_func = show_basket,
    # Додаємо метод функції корзини.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку магазину.
shop_app.add_url_rule(
    # Додаємо посилання.
    rule = "/shop",
    # Додаємо функцію відображення магазину.
    view_func = show_shop,
    # Додаємо метод функції магазину.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку контаку.
contact_app.add_url_rule(
    # Додаємо посилання.
    rule = "/contacts",
    # Додаємо функцію відображення контакту.
    view_func = show_contacts,
    # Додаємо метод функції контакта.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку адміна.
admin_app.add_url_rule(
    # Додаємо посилання.
    rule = "/admin",
    # Додаємо функію відображення адміна.
    view_func = show_admin,
    # Додаємо метод функції адміна.
    methods = ["GET", "POST"]

)

# Реєструємо додаток адміна.
project_shop.register_blueprint(blueprint= admin_app)
# Реєструємо додаток домашньої сторінки.
project_shop.register_blueprint(blueprint = home_app)
# Реєструємо додаток реєстрації.
project_shop.register_blueprint(blueprint = reg_app)
# Реєструємо додаток логіна.
project_shop.register_blueprint(blueprint = login_app)
# Реєструємо додаток корзини.
project_shop.register_blueprint(blueprint = basket_app)
# Реєструємо додаток магазину.
project_shop.register_blueprint(blueprint = shop_app)
# Реєструємо додаток контакта.
project_shop.register_blueprint(blueprint = contact_app)