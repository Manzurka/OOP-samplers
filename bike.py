class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles=0
        

    def displayInfo(self):
        return '{} {} {}' .format(self.price,self.max_speed,self.miles)
    def ride(self):
        raise_amount=10
        self.miles+=raise_amount
        return 'Riding'
        
    def reverse(self):
        decrease_amount=5
        if self.miles ==0:
            return self.miles
        else:
            self.miles-=decrease_amount
            return 'Reversing'


bike1 = Bike(200, "25mph")
bike2 = Bike(300, "35mph")
bike3 = Bike(400, "40mph")


print bike1.ride(),bike1.ride(),bike1.ride(),bike1.reverse(),bike1.displayInfo()
print bike2.ride(),bike2.ride(), bike2.reverse(),bike2.reverse(),bike2.displayInfo()
print bike3.reverse(),bike3.reverse(),bike3.reverse(),bike3.displayInfo()