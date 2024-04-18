import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

import matplotlib
matplotlib.use('Agg')

class visualisation:
  def __init__ (self, x_plot_values, y_plot_actual):
    #initialising the class with the x plot values and y plot actual values
    self.x_plot_values= np.array(x_plot_values)
    #converting the x plot values to an array
    self.y_plot_actual= np.append(np.array(y_plot_actual), 0)
    #converting the y plot actual values to an array and appending a 0 to the end of the array
    

  def get_y_pred_values(self,result): #function used to get the y values for the graph
    self.y_graph_values =np.array([row[-1] for row in result[-5:]])
    #getting the last 5 values from the result array from the neural network
    
  def create_graph(self): 
        plt.figure(figsize=(10, 10))     
        #setting the size of the graph
        plt.plot(self.x_plot_values, self.y_plot_actual, color='red', label='actual share price')
        #this is where we plot the actual price over time in a red line. with a label stating it is the actual 
        plt.plot(self.x_plot_values, self.y_graph_values, color='blue', label='predicted share price')
        #this is where we plot the predicted price over time in a blue line. with a label stating it is the predictedvalues 
        plt.ylabel('Share Price')
        #this is where we label the y axis as share price

        plt.ylabel('Date')
        #this is where we label the x axis as date

        plt.legend()
        #used to create a key for the graph


        plt.savefig('website/static')        
        #this is where we display the graph
     