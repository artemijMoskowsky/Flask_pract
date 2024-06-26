# Імпортуємо Flask
import flask
# Імпортуємо requests
import requests
# Імпортуємо flask_login
import flask_login
# Імпортуємо клас Message
from flask_mail import Message
# Імпортуємо клас Product
from shop_page.models import Product
# Імпортуємо клас User
from registration_page.models import User
# Імпортуємо mail, ADMINISTRATION_ADRES
from shop_project.mail_config import mail, ADMINISTRATION_ADRES
# Імпортуємо базу даних
from shop_project.settings import data_base
# Імпортуємо json
import json


# Створюємо функцію відображення сторінки
def show_basket():
    # Задаєтся початкове значення is_admin
    is_admin = False

    try:
        # Перезаписує значення is_admin, спираючись на значення користувача 
        is_admin = flask_login.current_user.is_admin
        # Перезаписує значення user_name, спираючись на значення користувача 
        user_name = flask_login.current_user.name
    
    except:
        # Задаєтся початкове значення user_name
        user_name = ""
    # Створюємо список для продуктів
    products_list = []
    # Створємо список в якому записуєтся id продукту без повторів
    product_unique_id_list = []
    # Створюємо список з кількістю повторенних продуктів
    id_counts = []

    
    try:
        # Отримуємо cookies у вигляді списку
        product_ids = flask.request.cookies.get("products").split(" ")
        # Перебираємо id продуктів з cookies
        for id in product_ids:
            # Перевіряємо чи немає id продкуту в списку product_unique_id_list
            if id not in product_unique_id_list:
                # Додаємо до списку id продукту
                product_unique_id_list.append(id)
        # Перебираємо унікальні id продуктів зі списку унікальних id
        for unique_id in product_unique_id_list:
            # Створюємо змінну кількості повторів
            count = 0
            # Перебираємо id продуктів
            for id in product_ids:
                # Перевіряємо якщо унікальне id співпало з id зі списку
                if unique_id == id:
                    # Додаємо до повторів 1
                    count = count + 1
            # Додаємо кількість повторів до списку повторів
            id_counts.append(count)
        # перебираємо унікальні id в списку унікальних id
        for unique_id in product_unique_id_list:
            # Отримуємо дані продукта по id
            product_info = Product.query.get(unique_id)
            # Перевіряємо що об'єкт існує
            if product_info != None:
                # Створюємо копію продукта передаючі усі дані окрім count
                product = Product(
                    id = product_info.id,
                    name = product_info.name,
                    price = product_info.price,
                    description = product_info.description,
                    discount = product_info.discount,
                    # Записуємо кількість повторів для подальшого зображення на сторінці
                    count = id_counts[product_unique_id_list.index(unique_id)]
                )
                # Додаємо продукти до списку
                products_list.append(product)
        # Перевіряєтся що на сервер прийшов запит
        if flask.request.method == "POST":
            # Перевіряєтся що була відправлена форма замовлення
            if flask.request.form.get("w_button") == None:
                # Записуємо email
                email = flask.request.form["email"]
                # Підготовлюємо текст для відправки до телеграму
                message_text = f'Імя: {flask.request.form["name"]}\nПрізвище: {flask.request.form["surname"]}\nНомер телефону: {flask.request.form["phone"]}\nEmail: {email}\nМісто: {flask.request.form["city"]}\nПобажання: {flask.request.form["wishes"]}\n\nСписок замовлення:\n'
                # Перебираємо продукти в списку продуктів
                for product in products_list:
                    # Додаємо до тексту назву товарів які були в замовленні
                    message_text +=f" *{product.name}\n"
                # Створюємо клавіатуру для подальшої відправки до телеграму
                keyboard = {
                    # Створюємо об'єкт клавіатури
                    "inline_keyboard": [[
                        # Створюємо кнопку для прийняття замовлення
                        {
                        "text": 'Прийняти замовлення',
                        "callback_data": f'apply_order {flask_login.current_user.id} {email}'
                        },
                        # Створюємо кнопку для відміни замовлення 
                        {
                        "text": "Відхилити замовлення",
                        "callback_data": f'reject_order {flask_login.current_user.id}'
                        }
                    ]]
                }
                # Задаємо токен бота
                token = "7288836611:AAEqW2rsGrWsat1iiiXHpEXFGVyXQOfoz5w"
                # Метод який відносится до запиту
                method = "SendMessage"
                # Посилання для запиту до телеграму
                url = f"https://api.telegram.org/bot{token}/{method}"
                # Параметри до запиту
                data = {"chat_id": "-1002157660034","message_thread_id": "4", "text": message_text, "reply_markup": json.dumps(keyboard)}
                # Запит до телеграму
                requests.post(url = url, data = data)
                # Створюємо об'єкт повідомлення до електронної пошти
                send_message = Message(
                    # Заголовок до повідомлення
                    subject = "Замовлення",
                    # Задаємо email отримувача
                    recipients = [email],
                    # Задаємо текст повідомленню
                    body = f"Ваше замовлення у обробці\n\n\n{message_text}",
                    # Задаємо відправника повідомлення
                    sender = ADMINISTRATION_ADRES
                )
                # Відправка повідомлення
                mail.send(send_message)
                # Отримуємо id поточного користувача
                user = User.query.get(flask_login.current_user.id)
                # Змінюємо флаг (is_watring на True) * ДЛЯ ТОГО ЩОБ ЗЬЯВИЛОСЯ МОДАЛЬНЕ ВІКНО : ЗАМОВЛЕННЯ У ОБРОБЦІ : *
                user.is_waiting = True
                # Зберігаємо в базу даних
                data_base.session.commit()
                
            else:
                # Отримуємо id поточного користувача
                user = User.query.get(flask_login.current_user.id)
                # Змінюємо флаг (is_watring на False) * ДЛЯ ТОГО ЩОБ ЗНИКЛО МОДАЛЬНЕ ВІКНО : ЗАМОВЛЕННЯ У ОБРОБЦІ : *
                user.is_waiting = False
                # Зберігаємо в базу даних
                data_base.session.commit()

    except Exception as _ex:
        print(_ex) 
    # Відтворюємо сторінку корзини, передаючи усі подіюні параметри
    return flask.render_template(template_name_or_list = "basket.html", user_name = user_name, link = "basket", products = products_list, is_admin = is_admin, is_waiting = flask_login.current_user.is_waiting)