from flask import Blueprint
from project import db
from project.Categories.models import Categories

"""
in this file we are defining the Categories blue print setting & wrote all the end points that related to Categories
"""
categories = Blueprint('categories', __name__,  static_folder='static')

#display Categories:
@categories.route('/Categories/', methods = ['GET'])
@categories.route('/Categories/<id>')
def all_Categories(id = -1):
    Categories_res =[]
    if int(id) == -1:
        for category in Categories.query.all():
            Categories_res.append({"id":category.id, "name":category.name, "Description":category.Description, "link":category.link, "img":category.img})
        return Categories_res
    if int(id) > -1: 
        category = Categories.query.get(int(id))
        Categories_res.append({"id":category.id, "name":category.name, "Description":category.Description, "link":category.link, "img":category.img})
        return Categories_res
