# Імпортуємо базу даних
from shop_project.settings import data_base

# Імпортуємо щаблон класу користувачів
from flask_login import UserMixin


# Модель користувача
class User(data_base.Model, UserMixin):
    # Унікальний id користувача
    id = data_base.Column(data_base.Integer, primary_key = True)
    # Ім'я користувача
    name = data_base.Column(data_base.String(255), nullable = False)
    # Пароль користувача
    password = data_base.Column(data_base.String(60), nullable = False)
    # Пошта користувача
    email = data_base.Column(data_base.String(60), nullable = False)
    # Наявність прав адміну
    is_admin = data_base.Column(data_base.Boolean, nullable = False)
    # Наявність очикування обробки замовлення
    is_waiting = data_base.Column(data_base.Boolean, nullable = False)
    # Функція що дає коротку інформацію про об'єкт
    def __repr__(self):
        # Повертаємо дані (id та ім'я) з функції
        return f"{self.id}, {self.name}"
    