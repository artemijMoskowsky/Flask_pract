# 
from shop_project.settings import data_base

# 
class Product(data_base.Model):
    # 
    id = data_base.Column(data_base.Integer, primary_key = True)
    # 
    name = data_base.Column(data_base.String(50), nullable = False)
    # 
    price = data_base.Column(data_base.Integer, nullable = False)
    # 
    description = data_base.Column(data_base.Text, nullable = False)
    # 
    count = data_base.Column(data_base.Integer, nullable = False)
    # 
    discount = data_base.Column(data_base.Integer, nullable = False)