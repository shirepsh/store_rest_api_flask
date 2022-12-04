from flask import Blueprint
from project import db
from project.Meat_products.models import Meat_products

"""
in this file we are defining the Meat_products blue print setting & wrote all the end points that related to Meat products
"""
meat_products = Blueprint('meat_products', __name__, template_folder='templates', static_folder='static')

#display Meat_products:
@meat_products.route('/Meat_products/', methods = ['GET'])
@meat_products.route('/Meat_products/<id>')
def all_Meat_products(id = -1):
    meat_res =[]
    if int(id) == -1:
        for meat_product in Meat_products.query.all():
            meat_res.append({"id":meat_product.id, "name":meat_product.name, "price":meat_product.price, "Description":meat_product.Description})
        return meat_res
    if int(id) > -1: 
        meat_product = Meat_products.query.get(int(id))
        meat_res.append({"id":meat_product.id, "name":meat_product.name, "price":meat_product.price, "Description":meat_product.Description})
        return meat_res