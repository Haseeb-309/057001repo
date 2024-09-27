class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price\
      
  def get_price(self, quantity):
      pass
  
  def make_purchase(self, quantity):
        if quantity <= 0:
            print("Purchase quantity must be greater than zero.")
        if quantity > self.amount:
            print(f"Insufficient quantity: only {self.amount} items available.")
        
        total_price = self.get_price(quantity)
        self.amount = self.amount - quantity
        print(f"Purchase successful: {quantity} {self.name}(s) bought for ${total_price:.2f}.")
        print(f"Remaining stock: {self.amount}")

 
  

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase