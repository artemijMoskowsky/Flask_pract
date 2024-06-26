# Проект "Flask_WorldIT_Diplom"

## Перелік учасників

- [Московський Артемій](https://github.com/artemijMoskowsky)
- [Науменко Нікіта](https://github.com/Naumenko0Nikita)
- [Олефіренко Глеб](https://github.com/GlebOlefirenko)
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

#### Запуск сайту:
1. Перейдіть до дерикторії головного додатку: `cd shop_project`
2. Ініціалізуйте базу даних: `flask --app settings db init`
3. Проведіть міграції бази даних: `flask --app settings db migrate`
4. Зробіть оновлення версії бази даних: `flask --app settings db upgrade`
5. Поверніться до попередньої дерикторії: `cd /..`
6. Запустити файл manage.py: `python manage.py`

#### Запуск бота:
1. Перейти до дерикторії бота: `cd Flask_pract/bot_app`
2. Запустити файл settings.py: `python settings.py`

## Структура проекту:
![image](./images/screenshot.jpg)

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

## Views нашого проекту:
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
