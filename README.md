![Logo](project/static/store.png)

## **store management**

This site was built to manage stores in a good and convenient way for the customers

- Submitted by Shir epshtein
- As part of the John Bryce course

- using the following technologies: python, flask, flask-sqlAlchemy

**note!**

**This is the back, which is uploaded to Render cloud.**

### **project locator:**
https://github.com/shirepsh/store_rest_api_render_cloud

### **guide line:**
- If you have not installed Python3, please do
- Please make sure you have 'pip' installed on your OS. 
If it is not installed, please refer to the link below and follow the steps: [Link to PyPa.io](https://pip.pypa.io/en/stable/cli/pip_install/)

1. download the project from GitHub by the comment:
```bash
git clone
```
2. install virtualenv
```bash 
pip install virtualenv
```
3. open venv named venv
```bash
python -m virtualenv venv
```
4. get into the venv 
```bash
venv\Scripts\active
```
5. install all the right packages with the requirements file
```bash
pip install -r requirements.txt  
``` 
6. run the application by the comment:
```
py app.py
```
7. once the code is active press ctrl+ click on the link that created ("http://127.0.0.1:5000") 

to make sure everything works, you can browse between the sundry Ends points.

### **The structure of the project**
the project build from:
- **instance folder** - contain the db

- **__init__db** file-  
This file's purpose is to insert pre-set data into the Library database

- **app.py file** - the run file  

- **README.md file** - Project description 

- **project folder**  
that contain:

    **1. static folder**- contain png icon  

    **2. _init__.py file**- Responsible for create the app, database setup, register blueprints

    ***3. subdirectory:*** **Categories**, **Fishes**, **Meat_products**, **Milk_products**, **Pastries**             
    each subdirectory contain:

    **__init__.py file**- an empty file 
    this file allows us to import components into main app.py file
    python needs this for it to understand that this is a module that it can import
    its also use for initializing the prog  

    **models.py file**- Responsible for creating the model and initializing it  
    
    **views.py file**- contains all the end points

