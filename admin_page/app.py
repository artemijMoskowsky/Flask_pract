# 
import flask 
# 
admin_app = flask.Blueprint(
    # 
    name = "admin",
    # 
    import_name = "admin_page",
    # 
    static_folder = "static/admin",
    # 
    template_folder = "template"
)