# 
import flask 
# Створення Flask додатку  
admin_app = flask.Blueprint(
    # Даэмо назву додатку
    name = "admin",
    # Вказуэмо місцезнаходження додатку
    import_name = "admin_page",
    # Вказуємо шлях до папки зі статичними файлами   
    static_folder = "static/admin",
    # Вказуэмо шлях до папки з шаблонами
    template_folder = "template"
)