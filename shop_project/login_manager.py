# Імпортуємо Flask_login
import flask_login
# Імпортуємо головний додаток
from .settings import project_shop
# Імпортуємо модель користувача 
from registration_page.models import User

# Створюємо об'єкт класу Login_mamager
login_manager = flask_login.LoginManager(app = project_shop)
# Створюємо secret_key
project_shop.secret_key = ".kjsrglhgsrhghwreuighuy"
# Передаємо до декоратору user_loader функцію авторизації користувача
@login_manager.user_loader
# Створюємо функцію авторизації користувача
def load_user(id):
    # Повертаємо об'єкт тої моделі яку ми хочемо авторизувати
    return User.query.get(id)