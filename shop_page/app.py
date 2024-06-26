# 
import flask
# Створення Flask додатку  
shop_app = flask.Blueprint(
    # Даэмо назву додатку
    name = "shop",
    # Вказуэмо місцезнаходження додатку
    import_name = "shop_page",
    # Вказуємо шлях до папки зі статичними файлами  
    template_folder = "templates",
    # Вказуэмо шлях до папки з шаблонами
    static_folder = "static/shop_page"
)