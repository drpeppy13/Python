class Bike(object):
    
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "price", self.price
        print "max_speed", self.max_speed
        print "miles", self.miles
    def ride(self):
        self.miles += 10
        print "Riding"

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5


bike1 = Bike(200, 25)
bike2 = Bike(300, 30)
bike3 = Bike(500, 50)

bike1.ride()
bike1.ride()
bike1.ride()
print bike1.displayinfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
print bike2.displayinfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
print bike3.displayinfo()





