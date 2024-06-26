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