import flask, flask_sqlalchemy, flask_migrate 
import os
# Створюємо константу абсолютного шляху до файлу
PATH = os.path.abspath(__file__+"/..")
# Створюємо зміну для головного додатку
project_shop = flask.Flask(
    # Вказуємо папку у якій знаходиться проект
    import_name = "shop_project",
    # Вказуємо шлях до папки зі статичними файлами 
    static_folder = "static/shop_project",
    # Вказуємо шлях для ініциалізації бази данних
    instance_path = PATH
)
# Робимо конфігурацію проєкту для роботи з базою данних "sqlite", вказуємо ім'я бази данних "data.db" і вказуємо те що вона локальна
project_shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# Створюємо об'єкт бази данних
data_base = flask_sqlalchemy.SQLAlchemy(app = project_shop)
# Створюємо об'єкт міграцій
migrate = flask_migrate.Migrate(app = project_shop, db = data_base)