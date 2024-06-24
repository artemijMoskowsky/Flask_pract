# 
from shop_project.settings import data_base

# Модель продукту
class Product(data_base.Model):
    # Унікальний id продукту
    id = data_base.Column(data_base.Integer, primary_key = True, autoincrement=False)
    # Ім'я продукту
    name = data_base.Column(data_base.String(50), nullable = False)
    # Ціна продукту
    price = data_base.Column(data_base.Integer, nullable = False)
    # Опис продукту
    description = data_base.Column(data_base.Text, nullable = False)
    # Кількість товару
    count = data_base.Column(data_base.Integer, nullable = False)
    # Знижка товару
    discount = data_base.Column(data_base.Integer, nullable = False)