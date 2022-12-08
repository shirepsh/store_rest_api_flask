from flask import Blueprint
from project import db
from project.Pastries.models import Pastries

"""
in this file we are defining the Pastries blue print setting & wrote all the end points that related to Pastries
"""
pastries = Blueprint('pastries', __name__, static_folder='static')

#display Pastries:
@pastries.route('/Pastries/', methods = ['GET'])
@pastries.route('/Pastries/<id>')
def all_Pastries(id = -1):
    Pastries_res =[]
    if int(id) == -1:
        for Pastrie in Pastries.query.all():
            Pastries_res.append({"id":Pastrie.id, "name":Pastrie.name, "price":Pastrie.price, "Description":Pastrie.Description, "img":Pastrie.img})
        return Pastries_res
    if int(id) > -1: 
        Pastrie = Pastries.query.get(int(id))
        Pastries_res.append({"id":Pastrie.id, "name":Pastrie.name, "price":Pastrie.price, "Description":Pastrie.Description, "img":Pastrie.img})
        return Pastries_res
