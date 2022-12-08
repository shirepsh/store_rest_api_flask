from project import db,app

#create the Categories table
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15), nullable= False)
    Description = db.Column(db.String(100), nullable= False)
    link = db.Column (db.String(30), nullable= False)
    img = db.Column (db.String(30), nullable= False)

    # initialise 
    def __init__(self, name, Description, link, img):
        self.name = name
        self.Description = Description
        self.link = link
        self.img = img
       
    

