# 
import flask
# 
import flask_login
# 
import os
# 
from shop_page.models import Product
# 
from shop_project.settings import data_base
# 
def show_admin():

    is_admin = False

    try:

        is_admin = flask_login.current_user.is_admin

        user_name = flask_login.current_user.name
    
    except:
        
        user_name = ""

    if flask.request.method == "POST" and is_admin:
        # changed_product =Product(
        #     id = product_id,
        #     name = flask.request.form["name"],
        #     count = product.count,
        #     price = product.price,
        #     description = product.description,
        #     discount = product.discount
        # )

        if not "add" in flask.request.form["id"] and not "del" in flask.request.form["id"]:
            
            product_id = flask.request.form["id"]
            product =Product.query.get(product_id)
            if flask.request.form.get("name") != None:
                product.name = flask.request.form.get("name")
                
            if flask.request.form.get("price") != None:
                product.price = flask.request.form.get("price")

            if flask.request.form.get("discount") != None:
                product.discount = flask.request.form.get("discount")

            if flask.request.form.get("description") != None:
                product.description = flask.request.form.get("description")


            images_path = os.path.abspath(__file__ + "/../../shop_page/static/shop_page/images")
            image = flask.request.files["image"]
            if image.filename != "":
                image.save(images_path + f"/{flask.request.form['id']}.png")
            # product_id = flask.request.form["id"]
            # product =Product.query.get(product_id)
            # product.name = flask.request.form["name"]

            # image = flask.request.files["image"]
            # if image.filename != "":
            #     image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/{product_id}.png"))

        elif "del" in flask.request.form["id"]:
            product_id = flask.request.form["id"].split("-")[1]
            selected_product = Product.query.get(product_id)
            data_base.session.delete(selected_product)
            data_base.session.commit()

        else:
            
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"r") as file:
                last_id = int(file.read())
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                file.write('')
            with open(os.path.abspath(__file__ + "/../../shop_project/loger.txt"),"w") as file:
                file.write(str(last_id + 1))
            new_product = Product(
                id = last_id + 1,
                name =  flask.request.form["name"],
                price = flask.request.form["price"],
                count = flask.request.form["count"],
                discount = flask.request.form["discount"],
                description =  flask.request.form["description"]
            )
            if len(Product.query.all()) != 0:
                last_product = Product.query.all()[-1]
                image = flask.request.files["image"]
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/{last_product.id+1}.png"))
            else:
                image = flask.request.files["image"]
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/shop_page/images/1.png"))
            #new_product.id = last_id + 1
            print(new_product.id)
            data_base.session.add(new_product)
        data_base.session.commit()
    #if user_type == "ADMIN":
    if is_admin == True:
        return flask.render_template(template_name_or_list = "admin.html", user_name = user_name, link = "admin", products = Product.query.all(), is_admin = is_admin)
    else:
        return flask.redirect("/")