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
![image](https://github.com/artemijMoskowsky/Flask_pract/assets/144718032/03f00dc8-2bf2-4409-b7af-a06680a4bfbc)
