# Проект "FlaskWorldITDiplom"

## Перелік учасників

- [Московський Артемій]()
- [Науменко Нікіта]()
- [Олефіренко Глеб]()
- [Лесковець Кирило]()
- [Мартиненко Святослав]()

## Опис Flask додатків

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

#### Установка и запуск
1. Клонируйте репозиторий: `git clone https://github.com/yourrepo`
2. Перейдите в директорию проекта: `cd yourrepo`
3. Установите зависимости: `pip install -r requirements.txt`
4. Запустите приложение: `flask run`

## Опис Flask моделей

### Модель 1: Користувач
Опис моделі користувача, її поля та методи.

```python
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

    def __repr__(self):
        return f"{self.id}, {self.name}"

```
### Модель 2: Продукт
Опис моделі продукту, її поля та методи.

```python
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