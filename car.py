class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed =speed
        self.fuel=fuel
        self.mileage=mileage
        self.tax=0
          
        if self.price>10000:
            self.tax=0.15
        else:
            self.tax=0.12

    def displayAll(self):
        return 'Price: {} \nSpeed: {}mph \nFuel: {} \nMileage: {}mpg \nTax: {}'.format(self.price,self.speed, self.fuel, self.mileage,self.tax)

car1=Car(2000, 35, "Full",15)
car2=Car(2000, 5, "Not Full",105)
car3=Car(2000, 15, "Kind of Full",95)
car4=Car(2000, 25, "Full",25)
car5=Car(2000, 45, "Full",25)
car6=Car(20000, 35, "Empty",15)

print car1.displayAll()
print car2.displayAll()
print car3.displayAll()
print car4.displayAll()
print car5.displayAll()
print car6.displayAll()