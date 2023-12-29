class Car:
    # Class variables
    wheels = 4

    def __init__(self):
        # those are instance variables
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()
print(c1.com, c1.mil)
print(c2.com, c2.mil)