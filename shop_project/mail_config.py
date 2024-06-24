import flask_mail 
from .settings import project_shop

ADMINISTRATION_ADRES = "tolikslus74@gmail.com"

ADMINISTRATION_PASSWORD = "uoqh refc eyti eisb"

USER_ADRESS = "seryoznitolya@gmail.com"

project_shop.config["MAIL_SERVER"] = "smtp.gmail.com"
project_shop.config["MAIL_PORT"] = 587
project_shop.config["MAIL_USE_TLS"] = True
project_shop.config["MAIL_USE_SSL"] = False
project_shop.config["MAIL_USERNAME"] = ADMINISTRATION_ADRES
project_shop.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD

mail = flask_mail.Mail(app = project_shop)