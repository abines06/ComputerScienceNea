class profit_calculator:

  def __init__(self):
    self.quantity = None 
    self.price= None 
    self.profit =None 


  def calculate_profit(self,future_price):
    
    current_revenue = self.quantity * self.price
    #calculating the revenue of the current stock

    future_revenue = self.quantity * future_price
    #calculating the revenue of the future stock

    self.profit = future_revenue - current_revenue
    #calculating the profit by subtracting the current revenue from the future revenue
    return self.profit
  


