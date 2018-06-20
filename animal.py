class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health-=1
        return "Walk"

    def run(self):
        self.health-=5
        return "Run"

    def displayHealth(self):
        return  "Health: {}".format(self.health)

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self). __init__(name,150)
        # self.name = name
        # self.health=150

    def pet(self):
        self.health+=5
        return "Pet"

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self). __init__(name,170)

    def fly(self):
        self.health-=10
        return "Fly"

    def displayHealth(self):
        return "I am a Dragon. Health: {}".format(self.health)

class Cat(Animal):
    def displayHealth(self):
        # super(Cat, self).displayHealth()
        return "I am a Cat. Health: {}".format(self.health)


a1=Animal("Hippo",100)
d1=Dog('Rex',100)
dr1=Dragon("Falkor", 100)
c1=Cat("Meow",20)

print a1.walk(),a1.walk(),a1.walk(),a1.run(),a1.run(),a1.displayHealth()
print d1.walk(),d1.walk(),d1.walk(),d1.run(),d1.run(),d1.pet(),d1.displayHealth()
print dr1.displayHealth()
print c1.displayHealth()
# print d1.fly(), c1.fly(),c1.pet()