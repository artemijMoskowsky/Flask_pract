import flask
# Створення Flask додатку
home_app = flask.Blueprint(
    # Даэмо назву додатку
    name = "home",
    # Вказуэмо місцезнаходження додатку
    import_name = "home_page",
    # Вказуємо шлях до папки зі статичними файлами 
    static_folder = "static/home_page",
    # Вказуэмо шлях до папки з шаблонами
    template_folder = "templates"
)