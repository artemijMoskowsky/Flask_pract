# 
import flask 

# 
login_app = flask.Blueprint(
    # 
    name = "login",
    # 
    import_name = "login_page",
    # 
    static_folder = "static/login_page",
    # 
    template_folder = "templates",
)