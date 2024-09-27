class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price
      
  def get_price(self, quantity):
     if quantity < 10:
        unit_price = self.price
     if quantity >= 10 and quantity < 50:
        unit_price = self.price * 0.8
     if quantity >= 50:
        unit_price = self.price * 0.5

     product_price = quantity * unit_price
     return product_price
    

  def make_purchase(self, quantity):
      pass 
  

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase