import flask 
# З моделей імпортуємо модель користувача 
from .models import User
# З основної деректоріїї імпортуємо базу данних
from shop_project.settings import data_base
# Створюємо функцію візуалізаціїї додатку реєстрації (registration_page)
def show_regestration():
    # Задаємо початкове значення для перевірки * ДЛЯ ПРОПОЗИЦІЇ ПЕРЕЙТИ ДО АВТОРИЗАЦІЇ *
    confirmed = False
    # Робимо перевирку: якщо метод запросу строго дорівнює "POST"
    if flask.request.method == "POST":
        # Записуємо у змінну (name), те що було введено у (<input>) з ім'ям "name"
        name = flask.request.form["name"]
        # Записуємо у змінну (name), те що було введено у (<input>) з ім'ям "email"
        email = flask.request.form["email"]
        # Записуємо у змінну (name), те що було введено у (<input>) з ім'ям "password"
        password = flask.request.form["password"]
        # Записуємо у змінну (name), те що було введено у (<input>) з ім'ям "password_confirm"
        password_confirm = flask.request.form["password_confirm"]

        try:
            # Створюємо змінну (user) для отримання всіх данних з моделі (User) 
            users = User.query.all()
            # Задаємо початкове значення для флагу (is_user) на "False", * ДЛЯ ТОГО ЩОБ ПЕРЕВІРЯТИ ЧИ Є ЗБІГИ У БАЗІ ДАНИХ *
            is_user = False
            # Робимо перевірку: Якщо збігаються змінні (password) та (password_confirm)
            if password == password_confirm:
                # Перебираємо список користувачів 
                for user in users:
                    # Робимо перевірку: Якщо збігаються данні з бази данних з данимми які були введені у формі 
                    if user.name == name and user.password == password:
                        # Задаємо значення для флагу (is_user) на "True", * ДЛЯ ТОГО ЩОБ ПЕРЕВІРЯТИ ЧИ Є ЗБІГИ У БАЗІ ДАНИХ *
                        is_user = True
                # Робимо перевірку: Якщо данні не збігаються
                if not is_user:
                    # Задаємо значення для перевірки * ДЛЯ ПРОПОЗИЦІЇ ПЕРЕЙТИ ДО АВТОРИЗАЦІЇ *
                    confirmed = True
                    # Створюємо нового користувача та передаємо туди усі данні, які були збережені з форми 
                    new_user = User(name = name, email = email, password = password, is_admin = False, is_waiting = False)
                    # Звертаємося до бази данних та додаємо створеного користувача 
                    data_base.session.add(new_user)
                    # Звертаємося до бази данних та зберігаємо данні які були добавленні у базу данних 
                    data_base.session.commit()

        except Exception as _ex:

            print(_ex)
    # Відображаємо сторінку передаючі усі необхідні данні
    return flask.render_template("registration.html", confirmed = confirmed, link="None")