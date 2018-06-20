class Product(object):
    
    def __init__(self, price, name, weight, brand,returnReason):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status= 'for sale'
        self.reason = returnReason
        
    def sold(self):
        self.status= 'sold'
        return self

    def addTax(self):
        self.price = (self.price * 1.1)
        return self

    def returnReason(self):

        if self.reason =='defective':
            self.status='defective'
            self.price=0
            return self

        elif self.reason =='like new':
            self.status
            return self

        elif self.reason == 'used':
            self.status='used'
            self.price-=(self.price * 0.2)
            return self

    def displayAll(self):
        return 'Price: {} \nName: {} \nWeight: {} lb \nBrand: {} \nStatus: {}'.format(self.price,self.name,self.weight,self.brand,self.status)

product1=Product(40, 'Shoes', 1, 'Nike', 'like new')

print product1.returnReason().displayAll()