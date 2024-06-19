# 
import flask

# 
reg_app = flask.Blueprint(
    # 
    name="reg_app",
    # 
    import_name="registration_page",
    # 
    static_folder="static/registration_page",
    # 
    template_folder="templates",
    # 
    static_url_path="/static"

)