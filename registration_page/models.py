# 
from shop_project.settings import data_base

# 
from flask_login import UserMixin


# 
class User(data_base.Model, UserMixin):
    # 
    id = data_base.Column(data_base.Integer, primary_key = True)
    # 
    name = data_base.Column(data_base.String(255), nullable = False)
    # 
    password = data_base.Column(data_base.String(60), nullable = False)
    # 
    email = data_base.Column(data_base.String(60), nullable = False)
    # 
    is_admin = data_base.Column(data_base.Boolean, nullable = False)

    # 
    def __repr__(self):
        # 
        return f"{self.id}, {self.name}"
    