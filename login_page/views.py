# Імпортуємо Flask
import flask
# Імпортуємо Flask_login
import flask_login
# Імпортуємо модель користувача
from registration_page.models import User
# Створюємо функцію відображення сторінки
def show_login():
    # Задаємо початкове значення для змінної видповідаючої за модальне вікно
    confirmed = True
    # Перевіряємо чи прийшли якісь дані на сервер
    if flask.request.method == "POST":
        # Задаємо значення що в нас не зареєстрований користувач, тобто модальне вікно з'являєтся
        confirmed = False
        # Записуємо у змінну (name), те що було введено у (<input>) з ім'ям "name"
        name = flask.request.form["name"]
        # Записуємо у змінну (name), те що було введено у (<input>) з ім'ям "password"
        password = flask.request.form["password"]
        # Записуємо дані кожного користувача
        users = User.query.all()

        # Перебираємо дані користувачів
        for user in users:
            # Перевіряємо співпадіння даних
            if user.name == name and user.password == password or user.email == name and user.password == password:
                # Авторизуємо користувача
                flask_login.login_user(user)
                # При авторизації користувач потрапляє на головну сторінку
                return flask.redirect("/")
        # Якщо авторизація не пройшла, тоді користувач бачить модальне вікно
    # Відображає сторінку
    return flask.render_template("login.html", confirmed = confirmed, link="None")