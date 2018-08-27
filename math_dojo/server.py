class MathDojo(object):
    def __init__(self):
        self.number = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.number += k
            else:
                self.number += 1
        return self
    def subtract(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.number += k
            else:
                self.number += 1
        return self
    def result(self):
        print "Total is", self.number
        return self


num1 = MathDojo() 
num1.add(2).add(2,5).subtract(3,2).result()
