# 
from .settings import project_shop
# 
from home_page import home_app, show_home
# 
from registration_page import reg_app, show_regestration
# 
from login_page import login_app, show_login
# 
from basket_page import basket_app, show_basket
# 
from shop_page import shop_app, show_shop
# 
from contacts_page import contact_app, show_contacts
# 
from admin_page import admin_app, show_admin

# 
home_app.add_url_rule(
    # 
    rule = "/",
    # 
    view_func = show_home,
)

# 
reg_app.add_url_rule(
    # 
    rule = "/registration",
    # 
    view_func = show_regestration,
    # 
    methods = ["GET", "POST"]
)

# 
login_app.add_url_rule(
    # 
    rule = "/login",
    # 
    view_func = show_login,
    # 
    methods = ["GET", "POST"]

)

# 
basket_app.add_url_rule(
    # 
    rule = "/basket",
    # 
    view_func = show_basket,
    # 
    methods = ["GET", "POST"]

)

# 
shop_app.add_url_rule(
    # 
    rule = "/shop",
    # 
    view_func = show_shop,
    # 
    methods = ["GET", "POST"]

)

# 
contact_app.add_url_rule(
    # 
    rule = "/contacts",
    # 
    view_func = show_contacts,
    # 
    methods = ["GET", "POST"]

)

# 
admin_app.add_url_rule(
    # 
    rule = "/admin",
    # 
    view_func = show_admin,
    # 
    methods = ["GET", "POST"]

)

# 
project_shop.register_blueprint(blueprint= admin_app)
# 
project_shop.register_blueprint(blueprint = home_app)
# 
project_shop.register_blueprint(blueprint = reg_app)
# 
project_shop.register_blueprint(blueprint = login_app)
# 
project_shop.register_blueprint(blueprint = basket_app)
# 
project_shop.register_blueprint(blueprint = shop_app)
# 
project_shop.register_blueprint(blueprint = contact_app)