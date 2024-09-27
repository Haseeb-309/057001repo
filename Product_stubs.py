class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price
      
  def get_price(self, quantity):
     if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
     if quantity < 10:
        unit_price = self.price
     if quantity >= 10 and quantity < 50:
        unit_price = self.price * 0.8
     if quantity >= 50:
        unit_price = self.price * 0.5

     product_price = quantity * unit_price
     return product_price
    

  def make_purchase(self, quantity):
        if quantity <= 0:
            print("Purchase quantity must be greater than zero.")
        if quantity > self.amount:
            print(f"Insufficient quantity: only {self.amount} items available.")
        
        total_price = self.get_price(quantity)
        self.amount = self.amount - quantity
        print(f"Purchase successful: {quantity} {self.name}(s) bought for ${total_price:.2f}.")
        print(f"Remaining stock: {self.amount}")

product = Product("Widget", 100, 10)
product.make_purchase(5)  
product.make_purchase(15)  
product.make_purchase(60) 
product.make_purchase(0)  
product.make_purchase(200)     

 
  


# do not forget to handle exceptions
# print the remaining stock after each purchase
# create product object
# make purchases against different product quantities (make sure to run each test case)