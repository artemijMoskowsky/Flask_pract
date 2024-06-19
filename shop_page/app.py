# 
import flask

# 
shop_app = flask.Blueprint(
    # 
    name = "shop",
    # 
    import_name = "shop_page",
    # 
    template_folder = "templates",
    # 
    static_folder = "static/shop_page"
)