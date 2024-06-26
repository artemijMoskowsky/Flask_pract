import flask_mail 
# Імпортуємо головний додаток 
from .settings import project_shop
# Створюємо константу для пошти адміністратора, та вписуємо її 
ADMINISTRATION_ADRES = "tolikslus74@gmail.com"
# Створюємо константу для паролю додатку
ADMINISTRATION_PASSWORD = "uoqh refc eyti eisb"
# Робимо конфігурацію для того щоб вказати з яким сервісом пошти ми працюємо
project_shop.config["MAIL_SERVER"] = "smtp.gmail.com"
# Робимо конфігурацію вказуємо поштовий порт
project_shop.config["MAIL_PORT"] = 587
# Робимо конфігурацію для того щоб використовувати протокол шифрування та аунтифікаціїї "Transport Leer Securiti"
project_shop.config["MAIL_USE_TLS"] = True
# Робимо конфігурацію для того щоб не використовувати протокол
project_shop.config["MAIL_USE_SSL"] = False
# Робимо конфігурацію та передаємо константу для пошти адміністратора
project_shop.config["MAIL_USERNAME"] = ADMINISTRATION_ADRES
# Робимо конфігурацію та передаємо константу для паролю додатку
project_shop.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD
# Створюємо менеджер поштових повідомленнь 
mail = flask_mail.Mail(app = project_shop)