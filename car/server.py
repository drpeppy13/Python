class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
    def display_all(self):
        print "This is {}".format(self)
        print "Price is ${}".format(self.price)
        print "Top speed is {}mph".format(self.speed)
        print "Fuel is {}".format(self.fuel)
        print "Mileage is {}".format(self.mileage)
        print "Tax is {}".format(self.tax)
car1 = Car(2000, 15, "full", "15mpg", 0.12)
car2 = Car(3000, 20, "almost full", "20mpg", 0.12)
car3 = Car(5000, 25, "full", "25mpg", 0.12)
car4 = Car(8000, 30, "full", "30mpg", 0.12)
car5 = Car(10000, 35, "full", "35mpg", 0.15)
car6 = Car(12000, 40, "empty", "40mpg", 0.15)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()