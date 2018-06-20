class MathDojo(object):
    def __init__(self):
        self.result=0

    def add(self, *args):
        for item in args:
            if type(item) == list:
                for value in item:
                    self.result += value
            elif type(item) == int:
                self.result += item
            elif type(item) == tuple:
                self.result += value
        return self
    def subtract(self, *args):
        for item in args:
            if type(item) == list:
                for value in item:
                    self.result -= value
            elif type(item) == int:
                self.result -= item
            elif type(item) == tuple:
                self.result -= value    
        return self
      
md = MathDojo().add(2).add(3, 5, 7, 8).subtract(5,5).result

print md

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result