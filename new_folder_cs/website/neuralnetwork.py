from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dropout, Dense
import matplotlib.pyplot as plt

class neural_network:

    def __init__ (self,):
        self.model= Sequential()
        #creating an instance of the sequential model

    def layers(self,x_data):
        self.model.add(SimpleRNN(units=50, activation='tanh', return_sequences=True, input_shape=(x_data.shape[1], 1)))
        #adding a simple RNN layer with 50 units, tanh activation function, returning sequences and input shape of x data
        self.model.add(Dense(units=1))
        #adding a dense layer with 1 unit
    

    
    def train_model (self,x_data, y_data, epoch, batch_size):#uses training data 
        return self.model.fit(x_data, y_data ,epoch, batch_size) 
        #training the neural network with our training data for x amount of epochs and batch size 
    
    def evalulate_loss(self, x_data, y_data):#uses training data 
        return self.model.evaluate(x_data, y_data)
    #evaluating the loss of the model with the training data 
    
    def predict(self, x_data): #uses testing data 
        return self.model.predict(x_data)
# this function will predict the stock price for unseen data 
    
    def plot_graph(self,result ,actual):
        #function used to plot the graph of the predicted stock price against the actual stock price
        plt.plot(result, color='blue', label='predicted closing price')
        #plotting the predicted stock price in blue
        plt.plot(actual, color='red', label='actual closing price')
        #plotting the actual stock price in red
        plt.title('prediction vs actual')
        #setting the title of the graph
        plt.xlabel('timesteps')
        #setting the x axis label
        plt.ylabel('close price')   
        #setting the y axis label
        plt.legend()
        #adding a legend to the graph
        plt.show()
        #displaying the graph        
       


