import telebot
import sqlite3
import os
import emoji

bot = telebot.TeleBot(token = "7288836611:AAEqW2rsGrWsat1iiiXHpEXFGVyXQOfoz5w")

button_1 = telebot.types.InlineKeyboardButton(text = "GET USERS", callback_data = "get_users")
button_2 = telebot.types.InlineKeyboardButton(text = "DELETE USER", callback_data = "delete_user")
button_3 = telebot.types.InlineKeyboardButton(text = "REMOVE ADMIN", callback_data = "remove_admin")

inline_keyboard_1 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_2 = telebot.types.InlineKeyboardMarkup()

inline_keyboard_1.add(button_1)
inline_keyboard_2.add(button_2, button_3)

chats = {
    "General": "1",
    "Users": "2",
    "Products": "3",
    "Cart": "4"
}

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
    bot.send_message(chat_id = message.chat.id, message_thread_id = message.message_thread_id, text = "Привіт, користувач!",  reply_markup = inline_keyboard_1)




@bot.callback_query_handler(func = lambda call: True)
def callback(cb: telebot.types.CallbackQuery):
    if "get_users" in cb.data:
        bot.send_message(chat_id = cb.message.chat.id, message_thread_id = chats["Users"],  text = "List of users: ")
        users_list = data_update("SELECT * FROM user")
        for user in users_list:
            inline_keyboard_2.keyboard[0][0].callback_data = f"delete_user {user[0]}"
            inline_keyboard_2.keyboard[0][1].callback_data = f"remove_admin {user[0]} {user[1]} {user[2]}"
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