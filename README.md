# Проект "FlaskWorldITDiplom"
## Опис:
Це проект написаний на Flask що являє собою інтернет магазин. У проекті є такі сторінки як: /, /shop, /basket, /admin. Проект можна запустити на слабкому сервері тому що частина того що можна реалізувати через базу даних реалізовано через cookies.

## Перелік учасників

- [Московський Артемій]()
- [Науменко Нікіта]()
- [Олефіренко Глеб]()
- [Лесковець Кирило]()
- [Мартиненко Святослав]()

## Технології та мови:
1. Python/Flask - Використовувался для розробки серверної частини проекту.
2. FlaskMigrate/FlaskSQLAlchemy - Використовувался для роботи з базою даних через Python/Flask.
3. FlaskLogin - Використовувался для того щоб авторізовувати користувачів на сайт.
4. JavaScript - Використовувался для Frontend розробки. Робота з елементами сторінки та cookies.
5. HTML - Використовувался для структури сайту.
6. CSS - Використовувался для стилів сайту.
7. sqlite3 - Використовувался для роботи з базою даних через бота.
8. Figma - Використовувалася для створення дизайну проекту.
9. Jinja - Використовувалася для передачі даних з Python/Flask до HTML.

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

## admin_page/views:
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
    #
    is_admin = False
    #
    try:
        #
        is_admin = flask_login.current_user.is_admin
        #
        user_name = flask_login.current_user.name
    #
    except:
        #
        user_name = ""
    #
    if flask.request.method == "POST" and is_admin:
        #
        if not "add" in flask.request.form["id"] and not "del" in flask.request.form["id"]:
            #
            product_id = flask.request.form["id"]
            #
            product =Product.query.get(product_id)
            #
            if flask.request.form.get("name") != None:
                #
                product.name = flask.request.form.get("name")
            #
            if flask.request.form.get("price") != None:
                #
                product.price = flask.request.form.get("price")
            #
            if flask.request.form.get("discount") != None:
                #
                product.discount = flask.request.form.get("discount")
            #
            if flask.request.form.get("description") != None:
                #
                product.description = flask.request.form.get("description")

            #
            images_path = os.path.abspath(__file__ + "/../../shop_page/static/shop_page/images")
            #
            image = flask.request.files["image"]
            #
            if image.filename != "":
                #
                image.save(images_path + f"/{flask.request.form['id']}.png")
        #
        elif "del" in flask.request.form["id"]:
            #
            product_id = flask.request.form["id"].split("-")[1]
            #
            selected_product = Product.query.get(product_id)
            #
            data_base.session.delete(selected_product)
            #
            data_base.session.commit()
        #
        else:
            #
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"r") as file:
                #
                last_id = int(file.read())
            #
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                #
                file.write('')
            #
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                #
                file.write(str(last_id + 1))
            #
            new_product = Product(
                #
                id = last_id + 1,
                #
                name =  flask.request.form["name"],
                #
                price = flask.request.form["price"],
                #
                count = flask.request.form["count"],
                #
                discount = flask.request.form["discount"],
                #
                description =  flask.request.form["description"]
            )
            #
            if len(Product.query.all()) != 0:
                #
                last_product = Product.query.all()[-1]
                #
                image = flask.request.files["image"]
                #
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/{last_product.id+1}.png"))
            #
            else:
                #
                image = flask.request.files["image"]
                #
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/1.png"))
            #
            data_base.session.add(new_product)
        #
        data_base.session.commit()
    #
    if is_admin == True:
        #
        return flask.render_template(template_name_or_list = "admin.html", user_name = user_name, link = "admin", products = Product.query.all(), is_admin = is_admin)
    #
    else:
        #
        return flask.redirect("/")
```

## JavaScript:
### shop_page/js:
```js
const list_button = document.querySelectorAll(".product_button");
const basketCount = document.querySelector("#basket-count");
const list_rbuttons = document.querySelectorAll(".readmore")
const list_description = document.querySelectorAll(".read-more")
const productList = document.querySelectorAll("#p_object")
const dataReader = document.querySelector(".dataReader")

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
### basket_page/js:
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

if (placingButton != null){
    placingButton.addEventListener("click", function(){
        let form = document.querySelector(".placing2")
        form.style.display = "flex"
    })
}


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

function setPrice(){
    sum_tag_h.textContent = parseInt(price_sum_tag_h.textContent.split(" ")[0]) - parseInt(discount_tag_h.textContent.split(" ")[0]) + " грн"
}
setPrice()
```
### admin_page/js:
```js
const basketCount3 = document.querySelector("#basket-count");
basketCount3.style.display = "None"

const changeButtonList = document.querySelectorAll(".change")
const formList = document.querySelectorAll(".p_object")
const popUpWindow = document.querySelector(".pop-up-window")
const add_product_button = document.querySelector(".add-button")


add_product_button.addEventListener("click", () => {
    add_product_button.previousElementSibling.style.display = "flex"
})

for(let count = 0; count < changeButtonList.length; count++){
    let changeButton = changeButtonList[count]
    changeButton.addEventListener(
        'click',
        function(){
            for(let count2 = 0; count2 < formList.length; count2++){
                let form = formList[count2]
                if (changeButton.id == form.getAttribute("id")){
                    let image = form. getElementsByClassName("p_image")[0]
                    popUpWindow.style.display = "flex"
                    if (changeButton.value != "image"){
                        let windowDiv = popUpWindow.getElementsByClassName("window_text_div")[0]
                        windowDiv.style.display = "flex"
                        let text = form.getElementsByClassName("p_" + changeButton.value)[0].textContent
                        let type = "text"
                        if (changeButton.value == "discount"){
                            text = text.split(" ")[1].replace("%", '')
                            type = "number"
                        } else if (changeButton.value == "price"){
                            text = text.split(" ")[0]
                            type = "number"
                        }
                        
                        let windowInput = windowDiv.getElementsByClassName("w_input")[0]
                        windowInput.name = changeButton.value
                        windowInput.value = text
                        windowInput.type = type
                    } else{
                        let windowDiv = popUpWindow.getElementsByClassName("window_image_div")[0]
                        windowDiv.style.display = "flex"
                        let windowImage = windowDiv.getElementsByClassName("w_image")[0]
                        windowImage.src = image.src
                    }
                    let apply_button = popUpWindow.getElementsByClassName("w_button")[0]
                    apply_button.value = changeButton.id

                }
            }
        }
    )
}

// Получаем елемент input всплывающего окна и добавляем функцию для события "onchange"
popUpWindow.getElementsByClassName("w_image_input")[0].addEventListener("change", function(event) {
    // Получаем елемент input
    let target = event.target;
    // Создаём объект класса FileReader
    let fileReader = new FileReader();
    // Добавляем прослушку события load
    fileReader.onload = function() {
        // Загружаем картинку в тег img
        popUpWindow.getElementsByClassName("w_image")[0].src = fileReader.result;
    }
    // Загружаем в fileReader изображение
    fileReader.readAsDataURL(target.files[0]);
})
```
