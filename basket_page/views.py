import flask
import flask_login
from flask_mail import Message
from shop_page.models import Product
from registration_page.models import User
from shop_project.mail_config import mail, ADMINISTRATION_ADRES, ADMINISTRATION_PASSWORD
from bot_app import bot, chats, button_apl, button_de, inline_keyboard_cart
from shop_project.settings import data_base
# import smtplib
# from email.mime.text import MIMEText


def show_basket():

    is_admin = False

    try:

        is_admin = flask_login.current_user.is_admin

        user_name = flask_login.current_user.name
    
    except:
        user_name = ""

    products_list = []
    product_unique_id_list = []
    id_counts = []

    
    try:
        product_ids = flask.request.cookies.get("products").split(" ")
        
        for id in product_ids:
            if id not in product_unique_id_list:
                product_unique_id_list.append(id)
            # products_list.append(Product.query.get(id))

        for unique_id in product_unique_id_list:
            count = 0
            for id in product_ids: # первый который второй 
                if unique_id == id:
                    count = count + 1
            id_counts.append(count)
        
        for unique_id in product_unique_id_list:
            product_info = Product.query.get(unique_id)
            if product_info != None:
                product = Product(
                    id = product_info.id,
                    name = product_info.name,
                    price = product_info.price,
                    description = product_info.description,
                    discount = product_info.discount,
                    count = id_counts[product_unique_id_list.index(unique_id)]
                )
                products_list.append(product)

        if flask.request.method == "POST":
            email = flask.request.form["email"]
            message_text = f'Імя: {flask.request.form["name"]}\nПрізвище: {flask.request.form["surname"]}\nНомер телефону: {flask.request.form["phone"]}\nEmail: {email}\nМісто: {flask.request.form["city"]}\nПобажання: {flask.request.form["wishes"]}\n\nСписок замовлення:\n'
            for product in products_list:
                message_text +=f" *{product.name}\n"

            inline_keyboard_cart.keyboard[0][0].callback_data = f"apply_order {flask_login.current_user.id} {email}"
            inline_keyboard_cart.keyboard[0][1].callback_data = f"reject_order {flask_login.current_user.id}"
            bot.send_message(chat_id = "-1002157660034", message_thread_id = chats["Cart"],  text = message_text, reply_markup = inline_keyboard_cart)
            # server = smtplib.SMTP(
            #     host = "smtp.gmail.com",
            #     port = 587,
            # )
            # server.starttls()
            # try:
            #     server.login(ADMINISTRATION_ADRES, ADMINISTRATION_PASSWORD)
            #     msg = MIMEText(message_text)
            #     msg["Subject"] = "Flask_Diplom"
            #     server.sendmail(from_addr = ADMINISTRATION_ADRES, to_addrs = USER_ADRESS, msg = msg.as_string())

            # except Exception as _ex:
            #     print(_ex)
            
            send_message = Message(
                subject = "Замовлення",
                recipients = [email],
                body = f"Ваше замовлення у обробці\n\n\n{message_text}",
                sender = ADMINISTRATION_ADRES
            )
            mail.send(send_message)
            user = User.query.get(flask_login.current_user.id)
            user.is_waiting = True
            data_base.session.commit()

    except Exception as _ex:
        print(_ex)
    return flask.render_template(template_name_or_list = "basket.html", user_name = user_name, link = "basket", products = products_list, is_admin = is_admin, is_waiting = flask_login.current_user.is_waiting)