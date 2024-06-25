import telebot
import sqlite3
import os
from shop_project.mail_config import ADMINISTRATION_ADRES, ADMINISTRATION_PASSWORD, USER_ADRESS
import smtplib
from email.mime.text import MIMEText



bot = telebot.TeleBot(token = "7288836611:AAEqW2rsGrWsat1iiiXHpEXFGVyXQOfoz5w")
button_1 = telebot.types.InlineKeyboardButton(text = "GET USERS", callback_data = "get_users")
button_2 = telebot.types.InlineKeyboardButton(text = "DELETE USER", callback_data = "delete_user")
button_3 = telebot.types.InlineKeyboardButton(text = "REMOVE ADMIN", callback_data = "remove_admin")
button_3_5 = telebot.types.InlineKeyboardButton(text = "ADD ADMIN", callback_data = "add_admin")
button_4 = telebot.types.InlineKeyboardButton(text = "GET PRODUCTS", callback_data = "get_products")
button_5 = telebot.types.InlineKeyboardButton(text = "DELETE PRODUCT", callback_data = "delete_product")
button_6 = telebot.types.InlineKeyboardButton(text = "ADD PRODUCT", callback_data = "add_product") 

button_apl = telebot.types.InlineKeyboardButton(text = "ПРИЙНЯТИ ЗАМОВЛЕННЯ", callback_data = "apply_order")
button_de = telebot.types.InlineKeyboardButton(text = "ВІДХИЛИТИ ЗАМОВЛЕННЯ", callback_data = "reject_order")

inline_keyboard_cart = telebot.types.InlineKeyboardMarkup()

inline_keyboard_cart.add(button_apl, button_de)

inline_keyboard_1 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_2 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_3 = telebot.types.InlineKeyboardMarkup()

inline_keyboard_1.add(button_1, button_4, button_6)
inline_keyboard_2.add(button_2, button_3, button_3_5)#, button_5, button_6
inline_keyboard_3.add(button_5)
chats = {
    "General": "1",
    "Users": "2",
    "Products": "3",
    "Cart": "4"
}

user_states = {}
new_products = {}

def data_update(command: str):
    data_base =  sqlite3.connect(os.path.abspath(__file__ + "/../../shop_project/data.db"))
    cursor = data_base.cursor()
    cursor.execute(command)
    response = cursor.fetchall()
    data_base.commit()
    data_base.close()
    return response

@bot.message_handler(commands = ["start"])
def start(message: telebot.types.Message):
    print(message.chat.id)
    bot.send_message(chat_id = message.chat.id, message_thread_id = message.message_thread_id, text = "Привіт, користувач!",  reply_markup = inline_keyboard_1)

@bot.message_handler(content_types=["text", "photo"])
def messages(message: telebot.types.Message):
    try:
        if not f"{message.from_user.id}" in new_products.keys():
            new_products[f"{message.from_user.id}"] = []

        if user_states[f"{message.from_user.id}"] == "name":
            new_products[f"{message.from_user.id}"].append(message.text)
            user_states[f"{message.from_user.id}"] = "image"
            bot.send_message(chat_id = message.chat.id,message_thread_id = chats["Products"] , text = "Надішліть зображення: ")
        elif user_states[f"{message.from_user.id}"] == "image":
            file_id = message.photo[-1].file_id
            file_info = bot.get_file(file_id)
            save_file = bot.download_file(file_info.file_path)
            file_name = f"{data_update('SELECT id FROM product ORDER BY id DESC LIMIT 1')[0][0] + 1}.png"
            with open(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/{file_name}"), "wb") as file:
                file.write(save_file)
            user_states[f"{message.from_user.id}"] = "price"
            bot.send_message(chat_id = message.chat.id,message_thread_id = chats["Products"] , text = "Введіть ціну: ")  

        elif user_states[f"{message.from_user.id}"] == "price":
            new_products[f"{message.from_user.id}"].append(message.text)
            user_states[f"{message.from_user.id}"] = "description"
            bot.send_message(chat_id = message.chat.id,message_thread_id = chats["Products"] , text = "Введіть опис: ")
        elif user_states[f"{message.from_user.id}"] == "description":
            new_products[f"{message.from_user.id}"].append(message.text)
            user_states[f"{message.from_user.id}"] = "count"
            bot.send_message(chat_id = message.chat.id,message_thread_id = chats["Products"] , text = "Введіть кількість: ")
        elif user_states[f"{message.from_user.id}"] == "count":
            new_products[f"{message.from_user.id}"].append(message.text)
            user_states[f"{message.from_user.id}"] = "discount"
            bot.send_message(chat_id = message.chat.id,message_thread_id = chats["Products"] , text = "Введіть знижку: ")
        elif user_states[f"{message.from_user.id}"] == "discount":
            new_products[f"{message.from_user.id}"].append(message.text)
            user_states[f"{message.from_user.id}"] = ""
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"r") as file:
                last_id = int(file.read())
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                file.write('')
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                file.write(str(last_id + 1))
            data_update(f"INSERT INTO product (id, name, price, count, description, discount) VALUES ({last_id+1}, '{new_products[str(message.from_user.id)][0]}', {new_products[str(message.from_user.id)][1]}, {new_products[str(message.from_user.id)][3]}, '{new_products[str(message.from_user.id)][2]}', {new_products[str(message.from_user.id)][4]}   )")
            new_products[f"{message.from_user.id}"] = []
            bot.send_message(chat_id = message.chat.id,message_thread_id = chats["Products"] , text = "Ви завершили створення продукту")


    except Exception as _ex:
        print(_ex)
        user_states[f"{message.from_user.id}"] = ""


@bot.callback_query_handler(func = lambda call: True)
def callback(cb: telebot.types.CallbackQuery):
    if "add_product" in cb.data:
        bot.send_message(chat_id = cb.message.chat.id, message_thread_id = chats["Products"], text = "Введіть назву продукту: ")
        user_states[f"{cb.from_user.id}"] = "name"
    else: 
        user_states[f"{cb.from_user.id}"] = ""
        
    if "get_users" in cb.data:
        bot.send_message(chat_id = cb.message.chat.id, message_thread_id = chats["Users"],  text = "List of users: ")
        users_list = data_update("SELECT * FROM user")
        for user in users_list:
            inline_keyboard_2.keyboard[0][0].callback_data = f"delete_user {user[0]}"
            inline_keyboard_2.keyboard[0][1].callback_data = f"remove_admin {user[0]} {user[1]} {user[2]}"
            inline_keyboard_2.keyboard[0][2].callback_data = f"add_admin {user[0]} {user[1]} {user[2]}"
            bot.send_message(chat_id = cb.message.chat.id, message_thread_id = chats["Users"],  text = f"ID: {user[0]}\nName: {user[1]}\nPassword: {user[2]}\n➡️is_admin⚠️: {user[4]}", reply_markup  = inline_keyboard_2)
            
    elif "delete_user" in cb.data:
        id = cb.data.split(" ")[1]
        data_update(f"DELETE FROM user WHERE id = {id}")
        bot.delete_message(chat_id = cb.message.chat.id, message_id = cb.message.message_id)
        
        
    elif "remove_admin" in cb.data:
        id = cb.data.split(" ")[1]
        name = cb.data.split(" ")[2]
        password = cb.data.split(" ")[3]
        data_update(f"UPDATE user SET is_admin = 0 WHERE id = {id}")
        inline_keyboard_2.keyboard[0][0].callback_data = f"delete_user {id}"
        inline_keyboard_2.keyboard[0][1].callback_data = f"remove_admin {id} {name} {password}"
        bot.edit_message_text(chat_id = cb.message.chat.id, message_id = cb.message.message_id, text = f"ID: {id}\nName: {name}\nPassword: {password}\n➡️is_admin⚠️: 0", reply_markup = inline_keyboard_2)
    elif "add_admin" in cb.data:
        id = cb.data.split(" ")[1]
        name = cb.data.split(" ")[2]
        password = cb.data.split(" ")[3]
        data_update(f"UPDATE user SET is_admin = 1 WHERE id = {id}")
        inline_keyboard_2.keyboard[0][0].callback_data = f"delete_user {id}"
        inline_keyboard_2.keyboard[0][1].callback_data = f"remove_admin {id} {name} {password}"
        bot.edit_message_text(chat_id = cb.message.chat.id, message_id = cb.message.message_id, text = f"ID: {id}\nName: {name}\nPassword: {password}\n➡️is_admin⚠️: 1", reply_markup = inline_keyboard_2)

    elif "get_products" in cb.data:
        bot.send_message(chat_id = cb.message.chat.id, message_thread_id = chats["Products"], text = "List of products: ")
        list_product = data_update("SELECT * FROM product")
        for product in list_product:
            inline_keyboard_3.keyboard[0][0].callback_data = f"delete_product {product[0]}"
            # inline_keyboard_3.keyboard[0][1].callback_data = f"edit_product {product[0]} {product[1]} {product[2]} {product[3]} {product[4]} {product[5]}"
            bot.send_message(chat_id = cb.message.chat.id, message_thread_id = chats["Products"] ,text = f"ID: {product[0]}\nName: {product[1]}\nPrice: {product[2]}\nDiscription: {product[3]}\nCount: {product[4]}\nDiscount: {product[5]}", reply_markup = inline_keyboard_3)
    
    elif "delete_product" in cb.data:
        id = cb.data.split(" ")[1]
        data_update(f"DELETE FROM product WHERE id = {id}")
        bot.delete_message(chat_id = cb.message.chat.id, message_id = cb.message.message_id)
            
    elif "reject_order" in cb.data:
        id = cb.data.split(" ")[1]
        data_update(f"UPDATE user SET is_waiting = 0 WHERE id = {id}")
        bot.delete_message(chat_id = cb.message.chat.id, message_id = cb.message.message_id)

    elif "apply_order" in cb.data:
        id = cb.data.split(" ")[1]
        email = cb.data.split(" ")[2]
        data_update(f"UPDATE user SET is_waiting = 0 WHERE id = {id}")
        bot.delete_message(chat_id = cb.message.chat.id, message_id = cb.message.message_id)
        server = smtplib.SMTP(
                host = "smtp.gmail.com",
                port = 587,
            )
        server.starttls()
        try:
            server.login(ADMINISTRATION_ADRES, ADMINISTRATION_PASSWORD)
            print(email)
            msg = MIMEText("Заявка була прийнята")
            msg["Subject"] = "Flask_Diplom"
            server.sendmail(from_addr = ADMINISTRATION_ADRES, to_addrs = email, msg = msg.as_string().encode("utf-8"))
        except Exception as _ex:
            print(_ex)

bot.infinity_polling()