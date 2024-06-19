# 
import flask_login
# 
from .settings import project_shop
# 
from registration_page.models import User

# 
login_manager = flask_login.LoginManager(app = project_shop)
# 
project_shop.secret_key = ".kjsrglhgsrhghwreuighuy"
# 
@login_manager.user_loader
# 
def load_user(id):
    # 
    return User.query.get(id)