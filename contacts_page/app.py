# 
import flask
# Створення Flask додатку  
contact_app = flask.Blueprint(
    # Даэмо назву додатку
    name = "contact",
    # Вказуэмо місцезнаходження додатку
    import_name = "contacts_page",
    # Вказуємо шлях до папки зі статичними файлами 
    static_folder = "static/contacts_page",
    # Вказуэмо шлях до папки з шаблонами
    template_folder = "templates"
)