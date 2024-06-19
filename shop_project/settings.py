#  #  # 
import flask, flask_sqlalchemy, flask_migrate
# 
import os

# 
PATH = os.path.abspath(__file__+"/..")

# 
project_shop = flask.Flask(
    # 
    import_name = "shop_project",
    # 
    static_folder = "static/shop_project",
    # 
    instance_path = PATH

)

# 
project_shop.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# 
data_base = flask_sqlalchemy.SQLAlchemy(app = project_shop)
# 
migrate = flask_migrate.Migrate(app = project_shop, db = data_base)