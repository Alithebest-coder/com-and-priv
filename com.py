#Write a program to create a class Computer with a private attribute max_price and 
# methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). 
# Now create an object for the class Computer. 
# Try changing the value of max price and use the sell function to display the updated price.
# Use a setter function to update the value and again display the price

class computer:
    def __init__(self):
        self .__maxprice=1
    def sell(self):
        print("THE PRICE NOW IS ",self.__maxprice)
    def sellmax(self,price):
        self.__maxprice=price
obj=computer()
obj.sell()
obj.sellmax(100000000)
obj.sell()