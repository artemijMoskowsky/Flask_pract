import flask

basket_app = flask.Blueprint(
    name = "basket",
    import_name = "basket_page",
    template_folder = "templates",
    static_folder = "static/basket_page"
)