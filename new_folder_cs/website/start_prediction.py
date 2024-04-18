
from flask import Blueprint, render_template, request, flash, redirect, url_for
# importing blueprint, render_template, request, flash, redirect, url_for from flasks
from flask_login import login_required, current_user
# importing login_required, current_user from flask_login
from werkzeug.utils import secure_filename
# importing secure_filename from werkzeug.utils
import os 
# importing os
import numpy as np
# importing numpy as np
import pandas as pd 
# importing pandas as pd

from website.profit_calculation import profit_calculator

ProfitLoss= profit_calculator()

def create_csv( file_path):
  #defining a function to create the csv dataframe 
  if os.path.getsize(file_path) > 0: 
    #this if statement checks if the csv file is empty
    csv = pd.read_csv(file_path) 
    #reading the csv file and storing it in the variable csv
    return csv
  else: #if the csv file is empty it carrys out the below 
    flash('The csv file is empty', category='error')  
    #if the csv file is empty it will display an error message on the website
    return render_template("start_prediction.html") #outputting the html file on page



def validate_csv(csv, file_path): 
  #defining a function to validate the csv file 
  Date = 'Date'
  #assigning the string 'Date' to the variable Date
  Close = 'Close'
  #assigning the string 'Close' to the variable Close

  if len(csv)== 250: #this if statement checks if the csv file has the correct amount of rows 
    pass #code will skip the rest of this if statement if it has the correct amount of rows 
  else:
    os.remove(file_path) #deletes a the file
    flash('The csv file does not have the correct number of rows', category='error') 
    #if the csv file does not have the correct amount of rows it will display an error message on the website
    return render_template("start_prediction.html")  #outputting the html file on page
  
  if csv.isnull().any(axis=None) : #this if statement checks if the csv file has any missing values
    os.remove(file_path) #deletes a the file
    flash('The csv file has missing values', category='error')
    # if the csv file has missing values it will display an error message on the website
    return render_template("start_prediction.html") #outputting the html file on page
  else:
    pass
  
  if Date in csv.columns and Close in csv.columns: #this if statement checks if the csv file has the correct columns
    flash ('file uploaded successfully', category='success') #displaying a success message on the website
    return redirect (url_for('prediction_result.prediction_result'))  
    

  #if the csv file has the correct column names it will take the user to the prediction result page
  else: 
    os.remove(file_path) #deletes a the file
    flash('The csv file does not have the correct columns', category='error')
    #if the csv file does not have the correct column names it will display an error message on the website
    return render_template("start_prediction.html") #outputting the html file on page
  


start_prediction_blueprint = Blueprint('start_prediction', __name__)
#creating a blueprint class with the name start_prediction 

@start_prediction_blueprint.route('/start_new_predictions',methods= ['GET', 'POST'])
#defining the directory on the website for the data loader page 
@login_required
#requiring the user to be logged in to access this page
def start_new_prediction():#defining what will occur on this page
    if request.method == 'POST':#if it is a post request do the below
      file_recieved = request.files['file_upload'] #assigining the file recieved from the front end to the variable file_recieved
      file_name = secure_filename(file_recieved.filename) #assigning the file name to the variable filename

      ProfitLoss.quantity = int(request.form.get('quantity')) #assigning the quantity to the variable quantity
      print (ProfitLoss.quantity)

      ProfitLoss.price = int(request.form.get('price')) #assigning the buy price to the variable price
      print (ProfitLoss.price)

    
      if file_name == None: #if no file name is found it is not accepted
        flash('Please upload a csv file', category='error')
        return render_template("start_prediction.html") #outputting a html file on page
      
      elif file_name.lower().endswith('.csv') == False: #if the file is not a csv file it is not accepted
        flash('Please upload a csv file', category='error')
        return render_template("start_prediction.html") #outputting a html file on page
      
      else:
        folder_directory = '/Users/abines/Documents/new_folder_cs/website/recieved_files_folder'
        #defining the folder directory where the file will be saved
        file_recieved.save(os.path.join(folder_directory, file_name)) 
        #saving the file to the folder directory and joining the folder directory with the file name

        file_path = os.path.join(folder_directory, file_name)
          #joining the folder directory with the file name to get the file path
        csv = create_csv(file_path)  #calling the function to create the csv file
        return  validate_csv(csv,file_path) #calling the function to validate the csv file 
      #depending on if it is a valid csv it will output the prediction result page or the start prediction page
      
      
    else: #if it is not a post request do the below
     return  render_template("start_prediction.html") #outputting a html file on page 
