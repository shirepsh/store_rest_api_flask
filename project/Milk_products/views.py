from flask import Blueprint
from project import db
from project.Milk_products.models import Milk_products

"""
in this file we are defining the Milk_products blue print setting & wrote all the end points that related to Milk_products
"""
milk_products = Blueprint('milk_products', __name__, template_folder='templates', static_folder='static')

#display Milk_products:
@milk_products.route('/Milk_products/', methods = ['GET'])
@milk_products.route('/Milk_products/<id>')
def all_Milk_products(id = -1):
    milk_res =[]
    if int(id) == -1:
        for milk in Milk_products.query.all():
            milk_res.append({"id":milk.id, "name":milk.name, "price":milk.price, "Description":milk.Description})
        return milk_res
    if int(id) > -1: 
        milk = Milk_products.query.get(int(id))
        milk_res.append({"id":milk.id, "name":milk.name, "price":milk.price, "Description":milk.Description})
        return milk_res

