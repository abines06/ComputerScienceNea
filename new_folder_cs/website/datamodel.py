from . import db 
#importing the database from the website package


from flask_login import UserMixin
# importing the usermixin from flask_login to allow for user authentication


class User(db.Model, UserMixin):
    #creating a class called user that inherits from the db.model and usermixin
    id = db.Column(db.Integer, primary_key=True)
    #creating a column in the database called id which is an integer and is the primary key
    stored_email = db.Column(db.String(150), unique=True)
    #creating a column in the database called stored_email which is a string and is unique
    stored_password = db.Column(db.String(150))
    #creating a column in the database called stored_password which is a string

