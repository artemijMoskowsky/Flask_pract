# 
import flask
# 
home_app = flask.Blueprint(
    # 
    name = "home",
    # 
    import_name = "home_page",
    # 
    static_folder = "static/home_page",
    # 
    template_folder = "templates"
)