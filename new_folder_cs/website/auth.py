
from flask import Blueprint , render_template, flash , request, redirect, url_for
#importing blueprint to this file
from .datamodel import User 
#importing the User class from the datamodel.py
from werkzeug.security import generate_password_hash, check_password_hash
#generating function to hash and check the password
from flask_login import login_user, login_required, logout_user, current_user
#importing login_user, login_required, logout_user, current_user from flask_login
from . import db
#importing the database from the __init__.py file




auth_blueprint = Blueprint('auth', __name__)
#creating a blueprint class with the name auth 

@auth_blueprint.route('/', methods= ['GET', 'POST'])#defining the directory on the website for login page 
def login():#defining what will occur on this page 
    if request.method == 'POST': #if the backend recieves a POST request it will carry out the below code 

       
        email= request.form.get('email') #recieiving the email from the html form and storing it in email variable 
        Password= request.form.get('Password')#reciving the password from the html form and storing it in the password variable

       

        if not email == 0: #checks if the email field is empty when post request sent
             flash('please enter a email',category= 'error') #displays and error message on the website
        else:
             pass #if the password field is not empty then the code will continue to run

        if not Password  == 0: #checks if the password field is empty when post request sent
            flash('please enter a password',category= 'error') #displays and error message on the website
        else:
            pass #if the password field is not empty then the code will continue to run
        


        found_user = User.query.filter_by(stored_email= email).first()
        #querys the database for the email entered and stores it in the found_user variable
        if found_user and check_password_hash(found_user.stored_password, Password):
        #checks if the email entered is in the database and if the password entered is correct
            flash('you are now logged in', category= 'success')
            login_user(found_user, remember=True) #logs the user in and stores the user in the current_user variable
            return redirect(url_for('start_prediction.start_new_prediction')) #takes them to the home page

        elif not found_user: #if the email entered is not in the database
             new_user= User(stored_email= email, stored_password= generate_password_hash(Password, method= 'pbkdf2:sha256'))
             db.session.add(new_user)#adds the new user to the database
             db.session.commit()#commits the changes to the database
             flash('account created', category= 'success') #displays a success message on the website
             login_user(new_user, remember=True) #logs the new user in and stores the user in the current_user variable
             return redirect(url_for('start_prediction.start_new_prediction')) #takes them to the home page

        else: #checks if the email is stored but password incorrect plus any other errors 
             flash('password or email incorrect', category= 'error') #displays an error message on the website
             return render_template("auth.html") #takes them back to the login page
    else:
             return render_template("auth.html") #outputting a html file on page to test
 
@auth_blueprint.route('/logout')
#defining the directory on the website for the logout page
@login_required
#requiring the user to be logged in to access this page
def logout():
    logout_user()
      #logs the user out usign the logout_user function
    return redirect(url_for('auth.login'))
      #takes the user back to the login page

