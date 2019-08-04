"""
Notes:
# ValueError: cannot switch from automatic field numbering to manual field specification
# If manual numbering - then give the manual numbering fully.
# If automatic numbering - then leave it python for automatic numbering fully.
# Combination will not work.

print("{0}: {1.make}, {1.price}, {2.make}, {2.price}".format(line_no(), kenwood, hamilton))

Each and every classes will have two attributes
    1) Data Attributes - Variables inside the Class
    2) Method Attributes - Functions inside the Class

We can also create the attributes [both data & method]

What is the difference between method and function?
Ans:
a) Method is always defined inside the class or its instance.
b) Method will pass the variable called 'self'

a) Function is defined outside class or its instance
b) Function will not have a argument called 'self'

"""

import inspect

line_no = lambda: inspect.currentframe().f_back.f_lineno

cp = lambda *args:print("{0}: {1}".format(inspect.currentframe().f_back.f_lineno, args))


class Kettle:
    pass


cp(Kettle, type(Kettle))


class Kettle:
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


hamilton = Kettle("HAMILTON", 100)
kenwood = Kettle("KENWOOD", 200)

# ValueError: cannot switch from automatic field numbering to manual field specification
# If manual numbering - then give the manual numbering fully.
# If automatic numbering - then leave it python for automatic numbering fully.
# Combination will not work.

print("{0}: {1.make}, {1.price}, {2.make}, {2.price}".format(line_no(), kenwood, hamilton))


class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


hamilton = Kettle("HAMILTON", 100)

cp("CURRENT-STATUS:", hamilton.on)

hamilton.switch_on()

cp("CURRENT-STATUS:", hamilton.on)

hamilton.power = "12 Watts"

cp(hamilton.__dict__, kenwood.__dict__)












