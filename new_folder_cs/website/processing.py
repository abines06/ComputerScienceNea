import pandas as pd 
import numpy as np 
#importing the pandas and numpy libraries
from sklearn.preprocessing import MinMaxScaler
#importing the MinMaxScaler from the sklearn library
from datetime import timedelta 

class csv_file_processor:
    
 def __init__ (self, csv):
    self.csv= csv
    #defining a function to initialise the csv file 
    #self.csv is the csv file that will be passed into the function

    self.x_plot_values= pd.to_datetime(self.csv['Date'].tail(4))
      #defining the x plot values as the last 4 values of the 'date' column in the csv file and converting it to datetime format
    
    self.y_plot_actual= self.csv['Close'].tail(4)
    #defining the y plot values as the last 4 values of the 'close' column in the csv file


 def separate_csv(self):
#function used to separate the csv dataframe into a training and testing set
   self.csv = self.csv[['Date','Close']]
    #defining the csv dataframe as the columns 'date' and 'close'
   
   
  
   
   self.csv.loc['Date'] = pd.to_datetime(self.csv['Date'])
    #converting the 'date' column to datetime format
   self.csv.set_index('Date',inplace=True)
    #setting the 'date' column as the index of the dataframe
   
   self.csv_train= self.csv[:200]
   print (self.csv_train)
   #defining the training set as the first 200 rows of the csv file

   self.csv_test= self.csv[200:]
      #defining the testing set as the last 50 rows of the csv file
   self.csv_test= self.csv_test.dropna()
   #dropping any missing values in the testing set
   print (self.csv_test)

 def process_csv(self,data,timestep ):
   #function used to prepare the data to be fed into the neural network 
   self.scaler = MinMaxScaler()
   #instantiating the minmaxscaler function
   data = self.scaler.fit_transform(data)

   #normalising the data using the minmaxscaler function 
   self.x_data= []
   self.y_data=[]
   #inintialising the x and y data lists
   rows= data.shape[0]
   #defining the number of rows in the data

   for i in range(timestep, rows):
      #for i values starting from the timesteps to the end of the dataset:
      #append timestep number of values to the x datalist 
      #append the value at the next timestep to the y datalist
       self.x_data.append(data[i-timestep:i])
       self.y_data.append(data[i])


   self.x_data= np.array(self.x_data)
   self.y_data= np.array(self.y_data)

 def add_date(self):
   #function used to add the date of the predicted day to self.x_plot_values
   last_date= self.x_plot_values.iloc[-1]
   #defining the last date in the x plot values list
   predicted_date= last_date+ timedelta(days=1)
   #defining the predicted date as the last date in the list plus one day
   self.x_plot_values= self.x_plot_values._append(pd.Series(predicted_date))
   #appending the predicted date to the x plot values list
   print (self.x_plot_values)




   



   
   

   

