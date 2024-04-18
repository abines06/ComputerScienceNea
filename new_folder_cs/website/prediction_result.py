from flask import Blueprint,render_template, request
# importing blueprint, render_template, request from flask
from flask_login import login_required, current_user
# importing login_required, current_user from flask_login
import os
# importing os
from website.plot_graph import visualisation
from website.start_prediction import create_csv
# importing the create_csv function from the start_prediction.py file
import pandas as pd 
# importing pandas as pd
from website.processing import csv_file_processor 
# importing the csv_file_processor class from the processing.py file
from website.neuralnetwork import neural_network

from website.start_prediction import ProfitLoss

from flask import redirect, url_for


prediction_result_blueprint = Blueprint('prediction_result', __name__)
#creating a blueprint class with the name prediction_result 

@prediction_result_blueprint.route('/prediction_result',methods= ['GET', 'POST'])
#defining the directory on the website for the prediction result page 
@login_required
#requiring the user to be logged in to access this page
def prediction_result():#defining what will occur on this page , for now just a test

    if request.method == 'GET': #if it is a get request do the below
    
     path_to_stored= '/Users/abines/Documents/new_folder_cs/website/recieved_files_folder'
        #defining the folder directory where the file is saved 
     
     for filename in os.listdir(path_to_stored): 
         #for each file in the folder directory we are joining the folder directory with the file name
         file_path= os.path.join(path_to_stored, filename)
            #creating a file path to the csv file 
     
     csv= create_csv(file_path) #calling the function to create the dataframe from the csv file
     os.remove(file_path) #deleting the file from the folder directory 

     processed_data= csv_file_processor(csv) #instnatating the class to process the data
     processed_data.separate_csv()
     #calling the function to separate the csv file into training and testing 

     processed_data.process_csv(processed_data.csv_train, 5)
       #calling the function to process the training csv file
     
     rnn= neural_network()
     #instantiating the class to create the neural network model

     rnn.layers(processed_data.x_data)
     #calling the function to create the layers of the neural network model

     rnn.model.compile (optimizer='adam', loss='mean_absolute_error', metrics=['mean_absolute_error']) 
       #calling the function to compile the model
     
     rnn.train_model(processed_data.x_data, processed_data.y_data,5,10)
         #calling the function to train the model
     
     
     processed_data.process_csv(processed_data.csv_test, 5)

     #calling the function to process the testing csv file
     

     result= rnn.predict (processed_data.x_data)
       #calling the function to predict the data
     
     result = result.reshape(result.shape[0], -1)
         #reshaping the result to be able to inverse transform it
     
     result= processed_data.scaler.inverse_transform(result)
       #scaling the result back to the original values
      
     print (result)
     

     evaluation= rnn.evalulate_loss(processed_data.x_data, processed_data.y_data)
       #calling the function to evaluate the model
     
     print (evaluation)

     #rnn.plot_graph (result, processed_data.y_data)
       #calling the function to plot the graph of the prediction result
     processed_data.add_date()
     
     visuals= visualisation(processed_data.x_plot_values, processed_data.y_plot_actual)
      #instantiating the class to plot the graph

     visuals.get_y_pred_values(result)
      #calling the function to get the y values for the graph

     prediction = result[-1][-1]
     print (prediction)
     #getting the last value of the last array of the result array which is our next day's price prediction

     calculated_result= round(ProfitLoss.calculate_profit(prediction), 2)
      #calculating the profit or loss from the prediction

     print (calculated_result) 
      #printing the profit or loss from the prediction
    


     
     date= visuals.x_plot_values
     #converting the dates values to a list
     actual= [round(value,2) for value in visuals.y_plot_actual.tolist()]
      #converting the actual values to a list and rounding to 2dp as it is a price. 
     predicted=[round(value,2) for value in visuals.y_graph_values.tolist()]
      #converting the predicted values to a list and rounding as it is a price 



     return render_template("results.html", prediction= prediction, calculated_result= calculated_result,
                             data=zip(date, predicted, actual))
      #outputting the html file on page and passing the variables to the html file
    else:
     
     return redirect(url_for('start_prediction.start_new_prediction')) #outputting a html text on page to test if directory works

