
from flask import Flask 
#importing flask library 
from flask_sqlalchemy import SQLAlchemy
#importing the sqlalchemy library to use the database
from flask_login import LoginManager
#importing the login manager from the flask_login library
from os import path
# importing the path function from the os library


db= SQLAlchemy()
#creating an instance of the database
DB_NAME = "login.db"
#creating a database with the name login.db


def create_app():

    from .datamodel import User
     # importing the user class from the datamodel file

    #creating an instance of a flask app 
    app = Flask(__name__)
    #creates an flask instance with the name of the file passed in as __name__
    app.config['SECRET_KEY']= 'QWERTYUIOP'
    #creating a secret key that is used for security purposes that we define 
    

    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #creating a database with the name of the file passed in as DB_NAME
    db.init_app(app)
    #initializing the database with the app 
    with app.app_context(): #this is used to create the database with the tables that we have defined in the datamodel file
         db.create_all() #this creates the database with the tables that we have defined in the datamodel file
    


    login_manager = LoginManager()
    #creating an instance of the login manager
    login_manager.login_view = 'auth.login'
    #setting the login view to the login page
    login_manager.init_app(app)
    #initializing the login manager with the app

    @login_manager.user_loader
    #this is used to load the user into the current_user variable
    def load_user(id):
        #loading the user into the current_user variable
        return User.query.get(int(id))
        #returning the user with the id that is passed in as a parameter
    

    from .auth import auth_blueprint  
    #imports the blueprint class named auth_blueprint from the auth.py file which contains the login directory 
    app.register_blueprint(auth_blueprint,url_prefix= '/')
    #registers the blueprint class named auth_blueprint into the app 
    
    from .prediction_result import prediction_result_blueprint 
    #imports the blueprint class named prediction_result_blueprint from the prediction_result.py file 
    #which contains the  directory for the result page of the prediction
    app.register_blueprint(prediction_result_blueprint, url_prefix= '/')
    #registers the blueprint class named prediction_result_blueprint into the app

    from .start_prediction import start_prediction_blueprint
    #imports the blueprint class named start_prediction_blueprint from the auth.py file 
    #which contains the  directory for the data loader page
    app.register_blueprint(start_prediction_blueprint, url_prefix= '/')
    #registers the blueprint class start_prediction_blueprint into the app

    

    return app 






   