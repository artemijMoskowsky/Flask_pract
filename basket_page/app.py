# 
import flask
# Створення Flask додатку  
basket_app = flask.Blueprint(
    # Даэмо назву додатку
    name = "basket",
    # Вказуэмо місцезнаходження додатку
    import_name = "basket_page",
    # Вказуємо шлях до папки зі статичними файлами 
    template_folder = "templates",
    # Вказуэмо шлях до папки з шаблонами
    static_folder = "static/basket_page"
)