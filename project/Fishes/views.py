from flask import Blueprint
from project import db
from project.Fishes.models import Fishes

"""
in this file we are defining the Fishes blue print setting & wrote all the end points that related to Fishes
"""
fishes = Blueprint('fishes', __name__, static_folder='static')

#display Fishes:
@fishes.route('/Fishes/', methods = ['GET'])
@fishes.route('/Fishes/<id>')
def all_Fishes(id = -1):
    fishes_res =[]
    if int(id) == -1:
        for fish in Fishes.query.all():
            fishes_res.append({"id":fish.id, "name":fish.name, "price":fish.price, "Description":fish.Description, "img":fish.img})
        return fishes_res
    if int(id) > -1: 
        fish = Fishes.query.get(int(id))
        fishes_res.append({"id":fish.id, "name":fish.name, "price":fish.price, "Description":fish.Description, "img":fish.img})
        return fishes_res

