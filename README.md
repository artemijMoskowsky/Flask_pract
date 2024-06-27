# Проект "Flask_WorldIT_Diplom"

## Перелік учасників

- [Московський Артемій](https://github.com/artemijMoskowsky)
- [Науменко Нікіта](https://github.com/Naumenko0Nikita)
- [Олефіренко Гліб](https://github.com/GlebOlefirenko)
- [Мартиненко Святослав](https://github.com/SviatMartynenko)

## Опис проекту:
Сайт-магазин написаний на мові програмування Python та JavaScript. Сайт надає можливість купувати товар, оформлювати замовлення, та за наявністю прав адміна додавати, редагувати та видаляти товар з магазину. Також сайт зв'язаний з телеграм ботом який надає адмінам можливість прийняти/відхилити ваше замовлення. При замовленні товару на почту користувача приходить повідомлення про здійснену покупку, та підтвердження замовлення.

## Чому проект корисний:
Цей проект дав нам змогу попрацювати з фреймворком Flask. При роботі над цим проектом ми познайомились зі структурою серверу, обробкою запитів, роботою з базами даних, роботою: з телеграм ботом, cookies, сесіями, gmail. Створення верстки, та розміщення проекту на pythonanywhere.
<br><br> Для оточуючих цей проект дає розуміння, як працюють усі вище перераховані технології.

## Початок роботи:
### Для роботи з нашим проектом вам знадобляться наступні модулі:
- alembic==1.13.1
- blinker==1.7.0
- certifi==2024.6.2
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- emoji==2.12.1
- Flask==3.0.3
- Flask-Login==0.6.3
- Flask-Mail==0.10.0
- Flask-Migrate==4.0.7
- Flask-SQLAlchemy==3.1.1
- greenlet==3.0.3
- idna==3.7
- itsdangerous==2.2.0
- Jinja2==3.1.3
- Mako==1.3.3
- MarkupSafe==2.1.5
- pyTelegramBotAPI==4.19.1
- requests==2.32.3
- SQLAlchemy==2.0.29
- telebot==0.0.5
- typing_extensions==4.11.0
- urllib3==2.2.1
- Werkzeug==3.0.2

### Як завантажити та запустити проект:
#### Завантажити проект:
1. Клонуйте репозиторій: `git clone https://github.com/artemijMoskowsky/Flask_pract.git
2. Перейдіть до дерикторії проекту: `cd Flask_pract`
3. Завантажте залежності: `pip install -r requirements.txt`

#### Налагодження проекту:
1. Перейдіть до дерикторії головного додатку: `cd shop_project`
2. Ініціалізуйте базу даних: `flask --app settings db init`
3. Проведіть міграції бази даних: `flask --app settings db migrate`
4. Зробіть оновлення версії бази даних: `flask --app settings db upgrade`
5. Поверніться до попередньої дерикторії: `cd /..`

#### Запуск сайту:
1. Перевірте що ви знаходитесь у дерикторії проекту Flask_pract
2. Запустити файл manage.py: `python manage.py`

##### Запуск бота:
1. Перейти до дерикторії бота: `cd bot_app`
2. Запустити файл settings.py: `python settings.py`

## Структура проекту:
![image](./images/screenshot.jpg)

## Технології та мови:
1. Python/Flask - Використовувался для розробки серверної частини проекту.
2. FlaskMigrate/FlaskSQLAlchemy - Використовувался для роботи з базою даних через Python/Flask.
3. FlaskLogin - Використовувался для того щоб авторізовувати користувачів на сайт.
4. JavaScript - Використовувался для Frontend розробки. Робота з елементами сторінки та cookies.
5. HTML - Використовувался для структури сайту.
6. CSS - Використовувался для стилів сайту.
7. telebot - Використовувался для роботи з телеграм ботом.
8. requests - Використовувался для надсилання повідомлень від імені бота, але за межою додатку bot_app.
9. sqlite3 - Використовувался для роботи з базою даних через бота.
10. Figma - Використовувалася для створення дизайну проекту.
11. Jinja - Використовувалася для передачі даних з Python/Flask до HTML.

## Опис додатків

### Додаток home_page: 
Додаток відповідаючий за роботу та відображення домашньої сторніки.
Має такі можливості:
 - Якщо користувач не авторизований тоді на сторінці є лише 2 кнопки: реєстрація та авторизація.
 - Якщо користувач авторизований тоді кнопки реєстрації та авторизації зникають та з'являються посилання на сторінки магазину.

### Додаток registration_page: 
Додаток відповідаючий за роботу та відображення сторніки реєстрації. При заповнені форми відображається модальне вікно яке пропонує перейти до авторизації.

### Додаток login_page: 
Додаток відповідаючий за роботу та відображення сторніки авторізації. При вводі ім'я/email та паролю йде перехід на домашню сторінку. Якщо такого користувача немає у базі даних, відображається модальне вікно з пропозицією перейти до реєстрації.

### Додаток shop_page: 
Додаток відповідаючий за роботу та відображення сторніки магазину. На цій сторінці відображаються усі товари що є у базі даних на цей момент, та заносить усі куплені товари у cookies.

### Додаток basket_page: 
Додаток відповідаючий за роботу та відображення сторніки корзини. На цій сторінці відображається увесь товар який був обран на сторінці магазину, загальна сума товару, знижка та сума з врахуваням знижки. id товарів береться з cookies.
Має такі можливості:
- Можна збільшити/зменьшити кільксть товару або повністю видалити його з корзини.
- При натискані на кнопку "Оформити замовлення" відкривається модальне вікно де користувач може ввести усі необхідні данні для зв'язку з ним. Відправляється запит через телеграм бота, можна відмінити замовлення або прийняти замовлення.

### Додаток admin_page: 
Додаток відповідаючий за роботу та відображення сторніки адміну. Сторінка доступна лише для тих користувачів що є адмінами.
Має такі можливості:
- Додавання нових товарів до бази даних магазину. Важливим моментом є те що при додаванні товару його id береть з файлу loger.txt, тому цей файл не бажано чипати.
- Редагування існуючих товарів.
- Видалення товарів з бази данних.

### Для чого потрібен loger.txt:
Цей фал відповідає за збереження останнього id що існувало у базі даних, це потрібно для того щоб id котре було видалено ніколи не з'явилось знову. Завдяки цьому коректно працює додаток basket_page, тому що старі id перестають працювати, та при видаленні товару зайві id з cookies стають не активними.

### Додаток bot_app:
Додаток відповідає за роботу бота який працює на адмін сервері у телеграмі. Бот має змогу:
- Виводити усіх користувачів.
- Видаляти користувача.
- Забирати права адміну.
- Виводити товар.
- Видаляти товар.
- Отримувати сповіщення про замовлення.
- Відхилити замовлення.
- Прийняти замовлення.

### Приклад створення головного додатку:
```python
import flask, flask_sqlalchemy, flask_migrate 
import os
# Створюємо константу абсолютного шляху до файлу
PATH = os.path.abspath(__file__+"/..")
# Створюємо зміну для головного додатку
project_shop = flask.Flask(
    # Вказуємо папку у якій знаходиться проект
    import_name = "shop_project",
    # Вказуємо шлях до папки зі статичними файлами 
    static_folder = "static/shop_project",
    # Вказуємо шлях для ініциалізації бази данних
    instance_path = PATH
)
# Робимо конфігурацію проєкту для роботи з базою данних "sqlite", вказуємо ім'я бази данних "data.db" і вказуємо те що вона локальна
project_shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# Створюємо об'єкт бази данних
data_base = flask_sqlalchemy.SQLAlchemy(app = project_shop)
# Створюємо об'єкт міграцій
migrate = flask_migrate.Migrate(app = project_shop, db = data_base)
```

### Приклад створення додатку:
```python
import flask
# Створення Flask додатку
home_app = flask.Blueprint(
    # Даэмо назву додатку
    name = "home",
    # Вказуэмо місцезнаходження додатку
    import_name = "home_page",
    # Вказуємо шлях до папки зі статичними файлами 
    static_folder = "static/home_page",
    # Вказуэмо шлях до папки з шаблонами
    template_folder = "templates"
)
```

## Приклад створення urls:
```python
# Імпортуємо головний додаток.
from .settings import project_shop
# Імпортуємо додаток домашньої сторінки та функція відображення.
from home_page import home_app, show_home
# Імпортуємо додаток реєстрації та функція відображеня.
from registration_page import reg_app, show_regestration
# Імротуємо додаток логіну та функції відображення.
from login_page import login_app, show_login
# Імротуємо додаток корзини та функції відображення.
from basket_page import basket_app, show_basket
# Імротуємо додаток магазину та функції відображення.
from shop_page import shop_app, show_shop
# Імротуємо додаток контакту та функції відображення.
from contacts_page import contact_app, show_contacts
# Імротуємо додаток адміну та функції відображення.
from admin_page import admin_app, show_admin

# Додаємо налагодження додатку домашньої сторінки.
home_app.add_url_rule(
    # Додаємо посилання.
    rule = "/",
    # Додаємо функцію відображення.
    view_func = show_home,
)

# Додаємо налагодження додатку реєстрації.
reg_app.add_url_rule(
    # Додаємо посилання.
    rule = "/registration",
    # Додаємо функцію відображення реєстрації. 
    view_func = show_regestration,
    # Додаємо метод функції реєстрації.
    methods = ["GET", "POST"]
)

# Додаємо налагодження додатку логіну.
login_app.add_url_rule(
    # Додаємо посилання.
    rule = "/login",
    # Додаємо функцію відображення логіну
    view_func = show_login,
    # Додаємо метод функції логіну.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку корзини.
basket_app.add_url_rule(
    # Додаємо посилання.
    rule = "/basket",
    # Додаємо функцію відображення корзини.
    view_func = show_basket,
    # Додаємо метод функції корзини.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку магазину.
shop_app.add_url_rule(
    # Додаємо посилання.
    rule = "/shop",
    # Додаємо функцію відображення магазину.
    view_func = show_shop,
    # Додаємо метод функції магазину.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку контаку.
contact_app.add_url_rule(
    # Додаємо посилання.
    rule = "/contacts",
    # Додаємо функцію відображення контакту.
    view_func = show_contacts,
    # Додаємо метод функції контакта.
    methods = ["GET", "POST"]

)

# Додаємо налагодження додатку адміна.
admin_app.add_url_rule(
    # Додаємо посилання.
    rule = "/admin",
    # Додаємо функію відображення адміна.
    view_func = show_admin,
    # Додаємо метод функції адміна.
    methods = ["GET", "POST"]

)

# Реєструємо додаток адміна.
project_shop.register_blueprint(blueprint= admin_app)
# Реєструємо додаток домашньої сторінки.
project_shop.register_blueprint(blueprint = home_app)
# Реєструємо додаток реєстрації.
project_shop.register_blueprint(blueprint = reg_app)
# Реєструємо додаток логіна.
project_shop.register_blueprint(blueprint = login_app)
# Реєструємо додаток корзини.
project_shop.register_blueprint(blueprint = basket_app)
# Реєструємо додаток магазину.
project_shop.register_blueprint(blueprint = shop_app)
# Реєструємо додаток контакта.
project_shop.register_blueprint(blueprint = contact_app)
```

## Views нашого проекту:

### Home_page:
```python
# Імпортуємо Flask
import flask
# Імпортуємо Flask_login
import flask_login
# Із моделей додатку (shop) імпортуємо модель продуктів
from shop_page.models import Product
# Створюємо функцію відображення  
def show_home():
    # Завдаємо початкове значення для флагу (is_admin) * ДЛЯ ПЕРЕВІРКИ ЧИ КОРИСТУВАТЧ МАЄ ПРАВА АДМІНІСТРАТОРА *
    is_admin = False
    
    try:
        # Завдаємо значення для флагу, від поточного користувача * ДЛЯ ПЕРЕВІРКИ ЧИ КОРИСТУВАТЧ МАЄ ПРАВА АДМІНІСТРАТОРА * 
        is_admin = flask_login.current_user.is_admin
        # Стврорюємо змінну у якій буде зберігатися ім'я поточного користувача * ДЛЯ ВІДООБРАЖЕННЯ ІМЕНІ КОРИСТУВАЧА *  
        user_name = flask_login.current_user.name
    except:
        # Обнуляємо змінну імені користуватча * ДЛЯ ТОГО ЩОБ ІМЕНА НЕ ПОВТОРЮВАЛИСЬ І НЕ БУЛО ПОМИЛКИ *
        user_name = ""
    # Створюємо список з id продуктів
    list_products_ids = []
    # перебираємо список продуктів
    for product in Product.query.all():
        # Добовляємо у список (list_products_ids) останнім значенням id продукту, яке ми отримали у базі даних 
        list_products_ids.append(product.id)    
    # Відображаємо сторінку передаючі усі необхідні данні
    return flask.render_template(template_name_or_list = "home.html", user_name = user_name, link = "home", is_admin = is_admin, list_products_ids = list_products_ids)
```

### Shop_page:
```python
# Імпортуємо Flask
import flask
# Імпортуємо Flask_login
import flask_login
# Імпортуємо клас з моделю нашого продукта
from .models import Product

# Створюємо функція для відображення продукта
def show_shop():    
    # Задаєтся початкове значення is_admin
    is_admin = False
    # Задаєтся початкове значення user_name
    user_name = ""
    try:
        # Перезаписує значення is_admin, спираючись на значення користувача     
        is_admin = flask_login.current_user.is_admin
        # Перезаписує значення user_name, спираючись на значення користувача  
        user_name = flask_login.current_user.name
    

    except:
        pass
    # Створюємо список для збереження (id) продуктів
    list_products_ids = []
    # Перебираємо список продуктів
    for product in Product.query.all():
        # Додаємо id продуктів в список
        list_products_ids.append(product.id)    
    # Відтворюємо сторінку магазину, передаючі усі необхідні параметри
    return flask.render_template(template_name_or_list = "shop.html", user_name=user_name, link="shop", products = Product.query.all(), is_admin = is_admin, list_products_ids = list_products_ids)
```

### Registration_page:
```python
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
                    # Задаємо початкове значення для перевірки * ДЛЯ ПРОПОЗИЦІЇ ПЕРЕЙТИ ДО АВТОРИЗАЦІЇ *
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
```

### Login_page:
```python
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
```

### Basket_page:
```python
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
```

### Admin_page:
```python
# Імпортуємо модуль flask
import flask
# Імпортуємо модуль flask_login
import flask_login
# Імпортуємо модуль os
import os
# Імпортуємо модель продуктів
from shop_page.models import Product
# Імпортуємо базу даних
from shop_project.settings import data_base
# Створюємо функцію відображення
def show_admin():
    # Задаємо початкове значення флагу is_admin що відповідає за права адміна користувача
    is_admin = False
    # Задаємо початкове значення флагу user_name що відповідає за відображене на сторінці ім'я
    user_name = ""
    try:
        # Перезаписуємо значення флагу is_admin з користувача
        is_admin = flask_login.current_user.is_admin
        #Перезаписуємо значення флагу user_name з користувача
        user_name = flask_login.current_user.name
    except:
        pass
    # Якщо на сайт прийшов запит та у користувача є права адміну
    if flask.request.method == "POST" and is_admin:
        # Якщо це запит не на додавання продукту та не на видалення (Це запит на редагування)
        if not "add" in flask.request.form["id"] and not "del" in flask.request.form["id"]:
            # Отримуємо id продукту з форми на сайті
            product_id = flask.request.form["id"]
            # Записуємо усі дані про продукт з бази даних використовуючі id з форми
            product = Product.query.get(product_id)
            # Якщо у форму передається змінена назва продукту
            if flask.request.form.get("name") != None:
                # Змінюємо ім'я товару на те що прийшло з форми
                product.name = flask.request.form.get("name")
            # Якщо у форму передається змінена ціна продукту
            if flask.request.form.get("price") != None:
                # Змінюємо ціну товару на те що прийшло з форми
                product.price = flask.request.form.get("price")
            # Якщо у форму передається змінена знижка продукту
            if flask.request.form.get("discount") != None:
                # Змінюємо знижку товару на те що прийшло з форми
                product.discount = flask.request.form.get("discount")
            # Якщо у форму передається змінений опис продукту
            if flask.request.form.get("description") != None:
                # Змінюємо опис товару на те що прийшло з форми
                product.description = flask.request.form.get("description")

            # Отримуємо абсолютний путь до папки у якій зберігаються зображення
            images_path = os.path.abspath(__file__ + "/../../shop_page/static/shop_page/images")
            # Отримуємо зображення з (<input type = "file">)
            image = flask.request.files["image"]
            # Якщо файл не пустій (Має ім'я)
            if image.filename != "":
                # Зберігаємо зображення % Передаючи шлях до зображення (images_path) та id з форми (flask.request.form['id']) та взавдаємо тип зображення %
                image.save(images_path + f"/{flask.request.form['id']}.png")
        # Якщо прийшов запит на видалення товару
        elif "del" in flask.request.form["id"]:
            # створюємо id продукту за допомогою (flask.request.form["id"].split("-")[1] це id, яке ми отримали)
            product_id = flask.request.form["id"].split("-")[1]
            # Отримуємо об'єкт продукту з бази даних за id з форми
            selected_product = Product.query.get(product_id)
            # Видаляємо зображення видаленого продукту з статичних файлів
            os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/{product_id}.png"))
            # Видаляємо об'єкт з бази даних
            data_base.session.delete(selected_product)
            # Звертаємося до бази даних та зберігаємо данні
            data_base.session.commit()
        # Якщо запит додавання продукту
        else:
            # Безпечно відкриваємо файл (loger.txt) з метою прочитання 
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"r") as file:
                # Отримуємо останній використаний у базі данних id
                last_id = int(file.read())
            # Безпечно відкриваємо файл (loger.txt) з метою очищення
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                # Чистимо файл
                file.write('')
            # Безпечно відкриваємо файл (loger.txt) з метою збереження максимального Id * ДЛЯ ТОГО ЩОБ ЗБЕРІГАТИ МАКСИМАЛЬНЕ ID В БАЗУ ДАНИХ *
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                # Записуємо останній id (який зараз буде використаний)
                file.write(str(last_id + 1))
            # Створюэмо змінну для нового продукту
            new_product = Product(
                # Записуємо останній доступний id + 1 
                id = last_id + 1,
                # Записуємо ім'я з форми
                name =  flask.request.form["name"],
                # Записуємо ціну з форми
                price = flask.request.form["price"],
                # Записуємо кількість з форми 
                count = flask.request.form["count"],
                # Записуємо знижку з форми
                discount = flask.request.form["discount"],
                # Записуємо опис з форми 
                description =  flask.request.form["description"]
            )
            # Якщо база даних не пуста
            if len(Product.query.all()) != 0:
                # Записуємо останній продукт
                last_product = Product.query.all()[-1]
                # Отримуємо зображення з фомрми
                image = flask.request.files["image"]
                # Зберігаємо зображення (по останньому ID + 1)
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/{last_product.id+1}.png"))
            # Якщо база даних пуста
            else:
                # Записуємо зображення з форми 
                image = flask.request.files["image"]
                # Зберигаємо зображення 
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/1.png"))
            # Додаємо до бази данних новий продукт 
            data_base.session.add(new_product)
        # Зберігаємо Базу 
        data_base.session.commit()
    # Якщо у користувача є права адміну
    if is_admin == True:
        # Відображаємо сторінку передаючі усі необхідні данні
        return flask.render_template(template_name_or_list = "admin.html", user_name = user_name, link = "admin", products = Product.query.all(), is_admin = is_admin)
    # Якщо прав адміну немає
    else:
        # Робимо перехід на іншу сторінку (home_page)
        return flask.redirect("/")
```

## Моделі проекту:
### Модель користувача:
#### Опис:
Модель користувача була створена для авторизацію користувача на сайті. Завдяки цієї моделі ми розуміємо хто саме зараз зайшов на сайт. Завдяки моделі користувача ми відстежуємо хто купує товар, або перевіряємо наявність прав адміну.
#### Код:
```python
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
```

### Модель продукту:
#### Опис:
Модель товару була створена для зберігання усіх даних про товар що зараз є у базі даних.
#### Код:
```python
# Імпортуємо базу даних
from shop_project.settings import data_base

# Модель продукту
class Product(data_base.Model):
    # Унікальний id продукту
    id = data_base.Column(data_base.Integer, primary_key = True, autoincrement=False)
    # Ім'я продукту
    name = data_base.Column(data_base.String(50), nullable = False)
    # Ціна продукту
    price = data_base.Column(data_base.Integer, nullable = False)
    # Опис продукту
    description = data_base.Column(data_base.Text, nullable = False)
    # Кількість товару
    count = data_base.Column(data_base.Integer, nullable = False)
    # Знижка товару
    discount = data_base.Column(data_base.Integer, nullable = False)
```

## JS нашого проекту:
### basket_page:
```js
const plus_buttons = document.querySelectorAll(".cart_buttons_p")
const minus_buttons = document.querySelectorAll(".cart_buttons_m")
const counters = document.querySelectorAll(".counter")
const price_list = document.querySelectorAll(".price") 
const price_sum_tag_h = document.querySelector("#p_priceT")
const list_p_content = document.querySelectorAll(".p_content")
const discount_tag_h = document.querySelector("#p_discountT")
const sum_tag_h = document.querySelector("#p_sumT")
const span_count = document.querySelector("#p_countT")
const basketCount2 = document.querySelector("#basket-count");
const productList2 = document.querySelectorAll("#p_object")
const placingButton = document.querySelector("#placing_button")
const countReader = document.querySelectorAll(".count_reader")

if (placingButton != null){
    placingButton.addEventListener("click", function(){
        let form = document.querySelector(".placing2")
        form.style.display = "flex"
    })
}

// Оновлюється лічильник поряд с корзиною
function updateBasketCount() {
    let count = 0

    for(let prod = 0; prod < productList2.length; prod++){
        let product = productList2[prod]
        let counter = product.getElementsByClassName("counter")[0]
        count += parseInt(counter.textContent)
    }
    basketCount2.textContent = count
    if (count > 0){
        basketCount2.style.display = "flex"
    } else {
        basketCount2.style.display = "none"
    }


}
updateBasketCount()

if (placingButton != null){
for(let id = 0; id < plus_buttons.length; id++){
    let button = plus_buttons[id]
    let counter = counters[id]
    let countr = countReader[id]

    button.addEventListener("click", function(){
        counter.textContent = parseInt(counter.textContent) + 1
        let cookie = document.cookie.split("=")[1]
        document.cookie = `products = ${cookie} ${button.id}`
        setPriceSum()
        setDiscount()
        setPrice()
        updateBasketCount()

    })
}

for(let id = 0; id < minus_buttons.length; id++ ){
    let button = minus_buttons[id]
    let counter = counters[id]
    button.addEventListener("click", function(){
        if(counter.textContent != "1"){
            counter.textContent = parseInt(counter.textContent) - 1
            let cookie = document.cookie.split("=")[1].split(" ")
            for (let i = 0; i < cookie.length; i ++){
                if (cookie[i] == button.id){
                    cookie.splice(i, 1)
                    break
                }
            }
            document.cookie = `products = ${cookie.join(" ")}`
            setPriceSum()
            setDiscount()
            setPrice()
            updateBasketCount()
        } else {
            counter.textContent = parseInt(counter.textContent) - 1
            setPriceSum()
            setDiscount()
            setPrice()
            updateBasketCount()
            button.parentElement.parentElement.parentElement.remove()
            let cookie = document.cookie.split("=")[1].split(" ")
            for (let i = 0; i < cookie.length; i ++){
                if (cookie[i] == button.id){
                    cookie.splice(i, 1)
                    break
                }
            }
            document.cookie = `products = ${cookie.join(" ")}`
        }
    })
}
}
// Функція для розрахунку суми товарів (без знижки) (грн)
function setPriceSum() {
    let price_sum = 0
    let counts = 0    
    for(let sum = 0; sum < price_list.length; sum++ ){
        let price = price_list[sum].textContent.split(" ")[0]
        let count = parseInt(counters[sum].textContent)
        counts += count
        price_sum += parseInt(price) * count

    }
    if (span_count != null){
        span_count.textContent = counts
    }
    price_sum_tag_h.textContent = price_sum  + " грн"

}
setPriceSum()

// Функція розрахунку єкономії за рахунок знижки (грн)
function setDiscount(){
    let discount = 0
    for(let dis = 0; dis < price_list.length; dis++ ){
        let price = price_list[dis].textContent.split(" ")[0]
        let count = parseInt(counters[dis].textContent)
        let discount_percent = parseInt(list_p_content[dis].id)
        discount += parseInt(parseInt(price) / 100 * discount_percent * count)

    }
    discount_tag_h.textContent = discount + " грн"
    
}
setDiscount()

// Функція розрахунку суми з врахуванням знижки (грн)
function setPrice(){
    sum_tag_h.textContent = parseInt(price_sum_tag_h.textContent.split(" ")[0]) - parseInt(discount_tag_h.textContent.split(" ")[0]) + " грн"
}
setPrice()
```

### Shop_page:
```js
const list_button = document.querySelectorAll(".product_button");
const basketCount = document.querySelector("#basket-count");
const list_rbuttons = document.querySelectorAll(".readmore")
const list_description = document.querySelectorAll(".read-more")
const productList = document.querySelectorAll("#p_object")
const dataReader = document.querySelector(".dataReader")

// Оновлюється лічильник поряд с корзиною
function updateBasketCount() {
    let cookies = document.cookie.split("=")[1].split(" ");
    let count = 0
    let validID = dataReader.getAttribute("data-products_ids").slice(1, -1).replace(/,/g, "").split(" ")


    for(let i = 0; i < cookies.length; i++){
        if( validID.includes(cookies[i])){
            count += 1
        }
    }
    basketCount.textContent = count
    if (count > 0){
        basketCount.style.display = "flex"
    } else {
        basketCount.style.display = "none"
    }

}

for (let i = 0; i < list_button.length; i++){
    let button = list_button[i];
    button.addEventListener("click", function() {
        if (document.cookie != ""){
            let products = document.cookie.split("=")[1]
            document.cookie = `products = ${products} ${button.id}; Path = /`
        }
        else{
            document.cookie = `products = ${button.id}; Path = /`
        }
        updateBasketCount()
        
    })
}

if (document.cookie == ""){
    basketCount.style.display = "None"
} else {
    updateBasketCount()
}

for (let i = 0; i < list_rbuttons.length; i++) {
    let button = list_rbuttons[i];
    button.addEventListener("click", function(){
        for (let j = 0; j < list_description.length; j++){
            let text = list_description[j]
            if (text.id == button.id){
                if (button.textContent == "Читати далі"){
                    text.style.overflow = "visible"
                    text.style.textOverflow = "clip"
                    text.style.whiteSpace = "normal"
                    button.textContent = "Згорнути"
                }
                else{
                    text.style.overflow = "hidden"
                    text.style.textOverflow = "ellipsis"
                    text.style.whiteSpace = "nowrap"
                    button.textContent = "Читати далі"
                }
            }  
        }
    })
}
document.body.style.overflowX = "hidden";
```

## HTML шаблони нашого проекту:
### Базовий шаблон:
#### Опис:
Це основа усіх інших шаблонів, цей шаблон створений для того щоб на кожному подальшому шаблоні були кнопки навігації. Якщо користувач ще не авторизован то на панелі навігації будуть кнопки "" та "". Якщо ж користувач пройшов авторизацію то кнопки "" та "" зникають, таз'являються кнопки "home", "shop", "basket", та якщо у користувача є права адміну то з'являється кнопка "admin".
#### Код:
```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <title>{% block title %}  {% endblock  %}</title>

        <meta charset="UTF-8">

        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <link rel="stylesheet"  href="{{ url_for('static', filename = 'css/style.css') }}">
        {% block style %}
        
        {% endblock %}

        {% block script %}

        {% endblock %}
        
        
    </head>

    <body>

        <div id = "header">
            
            
            <div id = "buttons">
                {% if link != "None" %}
                    <style>
                        #{{link}}{
                            font-weight: bold;
                            text-decoration: underline;
                        }
                    </style>
                    {% if user_name != "" %}
                        <button type="submit" class = "nav-button"><a id = "home" class = "button-a" href = "/">HOME</a></button>
                        <button type="submit" class = "nav-button"><a id = "shop" class = "button-a" href = "/shop">SHOP</a></button>
                        <div class = "basket_"><button type="submit" class = "nav-button"><a id = "basket" class = "button-a" href = "/basket">CART</a></button><p id="basket-count"></p></div>
                        <button type="submit" class = "nav-button"><a id = "contacts" class = "button-a" href = "/contacts">CONTACTS</a></button>
                        {% if is_admin %}
                            <button type="submit" class = "nav-button"><a id = "admin" class = "button-a" href = "/admin">ADMIN</a></button>
                        {% endif %}
                    {% endif %}
                {% endif %}
            </div>
            {% if user_name == "" %}
                <div id = "links" style="margin-top: 28px;">
                    <a class = "autoreg_link" href = "/registration" >REGISTRATION</a>
                    <a class = "autoreg_link" href = "/login" >AUTHORISATION</a>
                </div>
            {% else %}
                <div id = "links" style="margin-top: 18px;">
                    <h1 style="margin-top:0.5vh; text-transform: uppercase; font-family: sans-serif;">{{ user_name }}</h1>
                </div>
            {% endif %}

            
        </div>

        {% block content %}
        


        {% endblock  %}

    </body>

</html>
```

### Home_page:
#### Опис:
Домашня сторінка немає ніякого власного функціоналу, все що є на цій сторінці це надпис "HOME PAGE"
#### Код:
```html
{% extends "base.html" %}

{% block title %} Home {% endblock %}

{% block style %}
    <link rel="stylesheet"  href="{{ url_for('home.static', filename = 'css/style.css') }}"> 
{% endblock  %}

{% block script %}
    <script defer src= "{{ url_for('shop.static', filename = 'js/script.js') }}"></script>
{% endblock %}

{% block content %}
    <div class = "dataReader" style = "display: none;" data-products_ids = '{{ list_products_ids }}'>
    </div>
    <h1 id="home_page" align = "center">HOME PAGE</h1>
    <script src="{{ url_for('home.static', filename = 'js/home.js') }}"></script>
{% endblock %}
```

### Shop_page:
#### Опис:
Сторінка магазину це сторінка на якій відображається товар, та у користувача є можливість купити цей товар. Коли користувач заходить на цю сторінку, весь товар з бази даних відображається, та при натисканні на кнопку "Купити" id цього товару потрапляє до cookies.
#### Код:
```html
{% extends "base.html" %}

{% block title %} SHOP {% endblock  %}



{% block style %}
    <link rel="stylesheet"  href="{{ url_for('shop.static', filename = 'css/style.css') }}"> 
{% endblock  %}

{% block script %}
    <script defer src= "{{ url_for('shop.static', filename = 'js/script.js') }}"></script>
{% endblock %}


{% block content %}

    {% for product in products %}
        <div class = "dataReader" style = "display: none;" data-products_ids = '{{ list_products_ids }}'>
            
        </div>
    
        <div id = "p_object">
            <img style="align-self: flex-start" id = "p_image" src="{{ url_for('shop.static',filename='images/'+product.id|string+'.png')}}" alt="None">
            <div id = "p_content">
                
                <h1 style="margin-top: 0px; margin-bottom: 4px; font-family: sans-serif;"> {{product.name}} </h1>
                <h2 style="font-family: sans-serif; margin-top: 4px; margin-bottom: 4px; text-decoration: line-through;"> {{product.price}} грн</h2>
                <h2 style="font-family: sans-serif; margin-top: 4px; margin-bottom: 4px;"> Знижка {{product.discount}}%</h2>
                <h1 style="font-family: sans-serif; margin-top: 4px;"> {{((product.price / 100) * (100 - product.discount)) | int}} грн</h1>

                <button type="button" class = "product_button" id = "{{product.id}}">Купити</button>


                <h3 style="font-family: sans-serif; margin-bottom: 0px;">Опис: </h3>                                 

                <div id = "past_content">
                    <div id = "p_capacity">
                        
                        <p class = "read-more" id = "{{product.id}}"> {{product.description}} </p>
                        {% if product.description|length > 70 %}
                            <div style="display:flex;align-items: center;justify-content: center;">
                                <button type="button" class = "readmore" id = "{{product.id}}">Читати далі</button>
                            </div>
                        {% endif %}
                    </div>
                    {% if product.count|int > 0 %}
                    
                        <p style="font-family: sans-serif;"><span class="mark">✔</span> Товар в наявності</p>
                    {% else %}
                        <p style="font-family: sans-serif;"><span class="mark-off"></span>Товару немає в наявності</p>
                    {% endif %}
                    
                </div>
                
          
            </div>
        </div>

    {% endfor %}


{% endblock  %}

```

### Basket_page:
#### Опис:
На сторінці корзини відображається весь товар що ви купили на сторінці магазину, тут ви можете додати більше товару, або навпаки зменьшити його кількість. Також на цій сторінці ви можете оформити замовлення, при натисканні на кнопку відкривається форма, при заповнені якої на сервер приходять усі необхідні дані щоб можна було відправити інформацію про замовлення до телеграм серверу адмінів, та відправити вам на пошту підтвердження що ви замовили цей товар.
#### Код:
```html
{% extends "base.html" %}

{% block title %} Cart {% endblock %}

{% block script %}
    <script defer src= "{{ url_for('shop.static', filename = 'js/script.js') }}"></script>
    <script defer src= "{{ url_for('basket.static', filename = 'js/basket.js') }}"></script>
{% endblock %}

{% block style %}
    <link rel="stylesheet"  href="{{ url_for('basket.static', filename = 'css/style.css') }}"> 
{% endblock %}



{% block content %}

{% if is_waiting == true %}
<h2 align = "center" class = "waiting_title">Ваші дані у обробці<br>
консультант зв’яжеться з вами для підтвердження замовлення</h2>
{% endif %}

<form class = "placing2" method = "post">
    <h2 class = "placing2-title">ОФОРМЛЕННЯ ЗАМОВЛЕННЯ</h2>

    <p class = "placing2-text">Ім'я</p>
    <input type="text" name="name" value="" class = "placing2-input">
    
    <p class = "placing2-text">Прізвище</p>
    <input type="text" name="surname" value="" class = "placing2-input">
    
    <p class = "placing2-text">Номер телефону</p>
    <input type="text" name="phone" value="" class = "placing2-input">
    
    <p class = "placing2-text">Пошта</p>
    <input type="text" name="email" value="" class = "placing2-input">
    
    <p class = "placing2-text">Місто</p>
    <input type="text" name="city" value="" class = "placing2-input">
    
    <p class = "placing2-text">Побажання</p>
    <input type="text" name="wishes" value="" class = "placing2-input">

    <button type="submit" class = "send_button">SEND</button>
</form>

<div class="holder">
    <div>
        {% for product in products %}

            <div id = "p_object">
                <div class = "count_reader" id = "{{ product.count }}" style = "display: none;">
                    
                </div>
                <img style="align-self: flex-start" id = "p_image" src="{{ url_for('shop.static',filename='images/'+product.id|string+'.png')}}" alt="None">
                <div class = "p_content" id = "{{product.discount}}">

                    <h1 style="margin-top: 0px; font-family: sans-serif; width: 400px;text-overflow: ellipsis; overflow: hidden; width:310px; text-align: center;"> {{product.name}} </h1>
                    <div id = "p_buttons">
                        {% if is_waiting == false %}
                        <button type="button" class = "cart_buttons_m" id = "{{product.id}}">-</button>
                        {% endif %}
                        <h1 class = "counter" id = "{{product.id}}">{{product.count}}</h1>
                        {% if is_waiting == false %}
                        <button type="button" class = "cart_buttons_p" id = "{{product.id}}">+</button>
                        {% endif %}
                    </div>
                    <h1 style="font-family: sans-serif; width: 200px;" class = "price" id = "{{product.id}}">{{product.price}} грн</h1>
                </div>
            </div>
        {% endfor %}
    </div>
    {% if is_waiting == false %}
    <div class = "placing">
        <button type="button" id = "placing_button">ПЕРЕЙТИ ДО ОФОРМЛЕННЯ</button>
        <div class = "info_placer">
            <h4 id = "p_count"><span id = "p_countT">1</span> товари на суму</h4>
            <h4 id = "p_priceT">1</h4>
        </div>
        <div class = "info_placer">
            <h4 id = "p_discount">Знижка</h4>
            <h4 id = "p_discountT">1</h4>
        </div>
        <div class = "info_placer">
            <h3 id = "p_sum">Загальна сума</h3>
            <h3 id = "p_sumT">1</h3>
        </div>
    </div>
    {% endif %}
</div>

{% if is_waiting == true %}
<div style = "display: flex; justify-content: center; align-items: center;">
    <h4 style = "display: none;" id = "p_priceT">1</h4>
    <h4 style = "display: none;" id = "p_discountT">1</h4>
    <h1 style = "display: flex;" class = "waiting_sum" id = "p_sum">Загальна вартість замовлення: <h1 id = "p_sumT">1</h1></h1>
</div>

{% if is_waiting == true %}

<style>
.holder{
    align-items: center;
}
#p_object{
    margin-left: 150px;
}
</style>

{% endif %}
<div style = "display: flex; align-items: center; justify-content: center;">
    <form method = "post">
        <button name = "w_button" value = "True" type = "submit" class = "waiting_button">ВІДМІНИТИ ЗАМОВЛЕННЯ</button>
    </form>
</div>
{% endif %}

{% endblock  %}
```

### Admin_page:
#### Опис:
На сторінці адміну у адмінів є можливість додати/видалити/відредагувати товар. Для цього у нас є 3 форми:
1. Форма вікна додавання товару. Адмін має заповнити усі необхідні дані про товар, форма надішле ці дані до серверу, та сервер додає новий товар за цими даними
2. Форма редагування. При натисканні на кнопки редагування відкривається модальне вікно, яке підстроюється під ту кнопку яку ви натиснули. Після відправки форми, значення яке ві змінили змінеться у базі даних.
3. Форма видалення. Ця форма начеплена на весь товар, має у собі id товару, тому коли кнопка видалення натискається товар видаляється з бази даних по id
#### Код:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('admin.static',filename='css/style.css')}}">
{% endblock %}

{% block script %}
<script defer src = "{{url_for('admin.static', filename = 'js/script.js')}}"></script>
{% endblock %}
{% block content %}
    <div style = "display: none; background-color: rgba(255,255,255,0.5); z-index: 10; position:fixed; width: 100vw; height: 100vh; top: 0px;">
    <form method ="post" enctype="multipart/form-data" class="add-product">
        <h1 align="center" style = "margin-bottom: 2px;">Новий продукт</h1>
        <p class = "add-text">Зображення</p>
        <input class = "add-image" type="file" name="image" accept = "image/*">
        <p class = "add-text">Назва</p>
        <input class = "add-input" type="text" name="name" value="">
        <p class = "add-text">Опис</p>
        <textarea class = "add-input" name = "description" ></textarea>
        <p class = "add-text">Ціна</p>
        <input class = "add-input" type="number" name="price" value="">
        <p class = "add-text">Знижка</p>
        <input class = "add-input" type="number" name="discount" value="">
        <p class = "add-text">Кількість</p>
        <input class = "add-input" type="number" name="count" value="">
        
        
        <button class = "w_button" type="submit" name = "id" value = "add" >Додати</button>
    </form>
    </div>
    <button type="button" class = "add-button">
        <h2 style = "margin: 13px;">Додати продукт</h2>
        <p style = "background-color: #D1D8DB; border: 2px solid black; border-radius: 7px; font-size: 40px; padding-left: 10px; padding-right: 10px; margin: 0px;">+</p>
    </button>
    {% for product in products %}
            <form method="post" enctype="multipart/form-data" class = "p_object" id = "{{product.id}}">
                
                <div style="align-self: flex-start; align-items: center" class = "edit">
                    <img class = "p_image" id = "p_image" src="{{ url_for('shop.static',filename='images/'+product.id|string+'.png')}}" alt="None">
                    <button type="button" class = "change" id = "{{product.id}}" value = "image">
                        <img style = "width: 25px; height: 25px; position: relative; left: 0px; top: 0px;" src = "{{ url_for('admin.static',filename='image/edit.jpg') }}" alt="None">
                    </button>

                </div>
                <div id = "p_content">
                    
                    <div class = "edit">
                        <h1 class = "p_name" id = "p_name" style="margin-top: 0px; margin-bottom: 4px; font-family: sans-serif;"> {{product.name}} </h1>
                        <button type="button" class = "change" id = "{{product.id}}" value = "name">
                            <img style = "width: 25px; height: 25px; position: relative; left: 0px; top: 0px;" src = "{{ url_for('admin.static',filename='image/edit.jpg') }}" alt="None">
                        </button>
                    </div>

                    <div class = "edit">
                        <h2 class = "p_price" id = "p_price" style="font-family: sans-serif; margin-top: 4px; margin-bottom: 4px; text-decoration: line-through;">{{product.price}} грн</h2>
                        <button type="button" class = "change" id = "{{product.id}}" value = "price">
                            <img style = "width: 25px; height: 25px; position: relative; left: 0px; top: 0px;" src = "{{ url_for('admin.static',filename='image/edit.jpg') }}" alt="None">
                        </button>
                    </div>



                    <div class = "edit">
                        <h2 class = "p_discount" id = "p_discount" style="font-family: sans-serif; margin-top: 4px; margin-bottom: 4px;">Знижка {{product.discount}}%</h2>
                        <button type="button" class = "change" id = "{{product.id}}" value = "discount">
                            <img style = "width: 25px; height: 25px; position: relative; left: 0px; top: 0px;" src = "{{ url_for('admin.static',filename='image/edit.jpg') }}" alt="None">
                        </button>
                    </div>

                    <h1 style="font-family: sans-serif; margin-top: 4px;"> {{((product.price|int / 100) * (100 - product.discount|int)) | int}} грн</h1>

                    <button type="button" class = "product_button" id = "{{product.id}}">Купити</button>


                    <h3 style="font-family: sans-serif; margin-bottom: 0px;">Опис: </h3>                             


                    <div id = "past_content">
                        <div id = "p_capacity">
                        
                            <div class = "edit">
                                <p class = "read-more p_description" id = "{{product.id}}"> {{product.description}} </p>
                                <button type="button" class = "change" id = "{{product.id}}" value = "description">
                                    <img style = "width: 25px; height: 25px; position: relative; left: 0px; top: 0px;" src = "{{ url_for('admin.static',filename='image/edit.jpg') }}" alt="None">
                                </button>
                            </div>
                            
                            {% if product.description|length > 70 %}
                                <div style="display:flex;align-items: center;justify-content: center;">
                                    <button type="button" class = "readmore" id = "{{product.id}}">Читати далі</button>
                                </div>
                            {% endif %}
                        </div>
                        <button style = "display: flex;border: 0px; background-color: white;" name="id" value="del-{{product.id}}" type="submit" ><img style = " margin-top: 7px; width: 25px; height: 28px;" src = "{{ url_for('admin.static', filename = 'image/pomoyka.jpg') }}" alt = "None"><h3>Видалити товар</h3></button>   
                    
                    
                </div>
            </form>

    {% endfor %}
    <form method = "post" class = "pop-up-window" enctype = "multipart/form-data" style = "display: none; z-index: 1;" >
        <div class = "window">
            
            <div class = "window_image_div" style = "display: none; z-index: 2;">
                <h2 class = "w_text1">Змінити зображення</h2>
                <img class = "w_image" src = "" alt = "" style = "width: 200px; height: 250px; object-fit: contain; display: none;">
                <input class = "w_image_input" id = "file-upload" type="file" name="image" accept = "image/*">
                
            </div>
        
            <div class = "window_text_div" style = "display: none; z-index: 2;">
                <h2 class = "w_text">Змінити текст</h2>
                <input class = "w_input" type="text" name="" value="" style = "width: 350px; height: 35px; font-size: 25px">
            </div>
            <button class = "w_button" name="id" value="" type="submit">SEND</button>
        </div>
   
    </form>
    
{% endblock %}
```

### Registration_page:
#### Опис:
Сторінка реєстрації. На сторінці є лише 1 форма для введення даних акаунту, після надсилання форми на сервер, створюється новий акаунт у базі даних.
#### Код:
```html
{% extends "base.html" %}



{% block title %} Registration {% endblock  %} 

{% block style %}
    <link rel="stylesheet"  href="{{ url_for('reg_app.static', filename = 'css/style.css') }}"> 
{% endblock  %}




{% block content %}

    <div id="body-div">
        <div id="home_placer">
            <p id = "reg_title">REGISTRATION</p>
        </div>
        <div id="reg_placer">
            

            <form method = "post" id = "reg_content">
                <p class = "input_holder">Login</p>
                <input class = "reg_input" type="text" name="name" placeholder="">
                <p class = "input_holder">Email</p>
                <input class = "reg_input" type="text" name="email" placeholder="">
                <p class = "input_holder">Password</p>
                <input class = "reg_input" type="text" name="password" placeholder="">
                <p class = "input_holder">Password confirmation</p>
                <input class = "reg_input" type="text" name="password_confirm" placeholder="">
                <button class="reg_submit" type="submit">SEND</button>
            </form>
        </div>
    </div>
    {% if confirmed %}

       <style>
        
            #body-div{
                opacity: 0.5;
            }
        
        </style>
        
        <div id="div0">
            <h1 id="hh1" align = "center">CONFIRMED</h1>

            <div style="display: flex;" id="div1">
                <p id = "to_login" style="margin: 0;">→</p>
                <a id = "to_login" href="/login">AUTHORISATION</a>           
            </div>
        </div>

     
    {% endif %}


{% endblock  %}
```

### Login_page:
#### Опис:
Сторінка авторизації. Також має лише 1 форму, коли приходить запит до серверу йде перевірка що цей користувач є у базі даних, якщо він є, користувач авторизується та отримає сесіоний ключ до cookies.
#### Код:
```html
{% extends "base.html" %}

{% block title %}  Login  {% endblock  %}

{% block style %}
    <link rel="stylesheet"  href="{{ url_for('login.static', filename = 'css/style.css') }}"> 
{% endblock  %}


{% block content %}

    <div id="body-div">

        <div id="home_placer">

            <p id="log_title">AUTHORISATION</p>

        </div>

        <div id="log_placer">

            

            <form method = "post" id = "log_content">

                <p class = "input_holder">Login or Email</p>

                <input class = "log_input" type="text" name="name" placeholder="">

                <p class = "input_holder">Password</p>

                <input class = "log_input" type="text" name="password" placeholder="">
                
                <button class="log_submit" type="submit">SEND</button>
            </form>
        
        </div>
    
    </div>

    {% if not confirmed %}

       <style>
        
            #body-div{
                opacity: 0.5;
            }
        
        </style>
        
        <div id="div0">
            <h1 id="hh1" align = "center">YOU ARE NOT REGISTERED</h1>

            <div style="display: flex;" id="div1">
                <p id = "to_login" style="margin: 0;">→</p>
                <a id = "to_login" href="/registration">REGISTRATION</a>           
            </div>
        </div>

     
    {% endif %}

{% endblock  %}
```

## Що таке база даних та чому саме SQLite3:
### Що таке база даних:
База даних — це організована сукупність структурованої інформації або даних, яка зберігається електронним способом і керується системою управління базами даних (СУБД). База даних дозволяє зручно зберігати, шукати, змінювати та керувати великими обсягами інформації, забезпечуючи її цілісність, надійність та швидкий доступ.
<br>В даному проекті база даних застосовувалася для зберігання користувачів та продуктів. У чому зручність? Користувачі та продукти знаходяться у одній базі даних у різних таблицях, тобто інформаціє не змішується до купи.
### Чому саме SQLite3:
#### Ми обрали базу даних SQLite3 по наступним причинам:
1. Бібліотека SQLite3 встроєна у Python
2. Ми вже знайомі з цією базою даних
3. Для роботи SQLite3 потрібен 1 файл (Не враховуючі міграції які потрібні при роботі з Flask)
#### Що таке id у базах даних:
ID - це ідентифікатор, можна сказати унікальний номер об'єкту. ID у базах даних потрібен для звернення до конкретного запису у таблиці, без нього ви просто не зможете отримувати дані з таблиці.

# Висновки:
Цей проект був достатньо цікавий та корисний для нашої команди. Ми познайомились з усією необхідною інформацією для того щоб написати сайт для замовника.
<br>
<br>
Під час роботи над проектом ми навчилися:
1. Розробити правильну структуру серверу.
2. Створювати верстку сайту.
3. Обробляти запити.
4. Працювати з моделями.
5. Працювати з smtp (Simple Mail Transfer Protocol).
6. Деплоїти проект на віддалений хостинг.
