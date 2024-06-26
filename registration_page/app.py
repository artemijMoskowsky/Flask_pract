# 
import flask
# Створення Flask додатку
reg_app = flask.Blueprint(
    # Даэмо назву додатку
    name="reg_app",
    # Вказуэмо місцезнаходження додатку
    import_name="registration_page",
    # Вказуємо шлях до папки зі статичними файлами  
    static_folder="static/registration_page",
    # Вказуэмо шлях до папки з шаблонами
    template_folder="templates",
    # Вказуємо шлях до статичних файлів  
    static_url_path="/static"

)