from project import db, app
from project.Categories.models import Categories
from project.Meat_products.models import Meat_products
from project.Milk_products.models import Milk_products
from project.Fishes.models import Fishes
from project.Pastries.models import Pastries

category1 = Categories(name= "dairy products", Description="Dairy products of all types of milk", link="/Milk_products")
category2 = Categories(name= "meat products", Description="meet by weight and related products", link="/Meat_products")
category3 = Categories(name= "fishes", Description="Fish by weight and related products", link="/Fishes")
category4 = Categories(name= "pastries", Description="Baked products and prepared desserts", link="/Pastries")

Meat_pro1= Meat_products(name="pastrama", price="12.90", Description="Coal pastrami 1 kg, Price for 100 gram")
Meat_pro2= Meat_products(name="chicken", price="50.90", Description="Fresh chicken thighs 1 kg, Price for 100 gram")
Meat_pro3= Meat_products(name="frozen hamburger", price="20.90", Description="5 frozen hamburger units")
Meat_pro4= Meat_products(name="chicken sausages", price="20.90", Description="Chicken sausages 1 kg, Price for 100 gram")


Milk_pro1 = Milk_products(name="milk", price="6.90", Description="milk in a carton 3% 1 liter ")
Milk_pro2 = Milk_products(name="cheese", price="8.90", Description="Cheese 5% 300 grams")
Milk_pro3 = Milk_products(name="yogurt", price="3.90", Description="Danone yogurt 1.7 percent fat 3% 200 grams")
Milk_pro4 =Milk_products(name="chocolate milk", price="8.90", Description="Chocolate family bottle 1 liter")

Fish1 = Fishes(name="salmon", price="99.90", Description="Whole fresh salmon fillet, price for 1 kg")
Fish2 = Fishes(name="tuna", price="19.90", Description="4 tuna units")
Fish3 = Fishes(name="cod", price="69.90", Description="For fresh whole cod, price per 1 kg")
Fish4 =Fishes(name="spices", price="14.90", Description="Set of 6 spices for cooking fish at home")

Pastrie1 = Pastries(name="Melbi cream", price="12.90", Description="Melbi cream, 2 units * 150 gram")
Pastrie2 = Pastries(name="Chocolate mousse", price="15.90", Description="Chocolate mousse and hazelnuts, 2 units * 75 gram")
Pastrie3 = Pastries(name="Cheesecake", price="13.90", Description="Cheesecake with blueberries, 2 units * 92 gram")
Pastrie4 = Pastries(name="chocolate chip cookies", price="11.90", Description="Chocolate chip cookies, 12 units")

with app.app_context():

    db.session.add_all([category1, category2 ,category3, category4])
    db.session.add_all([Meat_pro1, Meat_pro2 ,Meat_pro3 , Meat_pro4])
    db.session.add_all([Milk_pro1, Milk_pro2 ,Milk_pro3, Milk_pro4])
    db.session.add_all([Fish1, Fish2 ,Fish3, Fish4])
    db.session.add_all([Pastrie1, Pastrie2 ,Pastrie3, Pastrie4])

    db.session.commit()

