class Animal(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayinfo(self):
        print "My Name is {}".format(self.name)
        print "My Health is {}".format(self.health)
        return self     

animal1 = Animal("Cookie")
animal1.walk().walk().walk().run().run().displayinfo()
# walk 3 times run 2 times display info

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)
    def displayinfo(self):
        print "My name is {}".format(self.name)
        print "My health is {}".format(self.health)
        print "I'm a Dragon"
        return self
    def fly(self):
        self.health -= 10
        return self

dog1 = Dog("Bucky")
dog2 = Dog("Wendy")
dog1.displayinfo()    


dragon1 = Dragon("Wing")
dragon1.displayinfo()