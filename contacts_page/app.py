# 
import flask
# 
contact_app = flask.Blueprint(
    # 
    name = "contact",
    # 
    import_name = "contacts_page",
    # 
    static_folder = "static/contacts_page",
    # 
    template_folder = "templates"
)