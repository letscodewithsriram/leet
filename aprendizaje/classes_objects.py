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

Class: Template for creating objects. All objects created using same class will have same characteristics
Object: An instance of a class
Instantiate: Create a instance of a class
Method: A function defined in a class
Attribute: A Variable bound to an instance of a class

We can call methods from other methods also

Reference: https://www.geeksforgeeks.org/args-kwargs-python/

*args - Variable no. of arguments - args - Tuple
**kwargs - Variable no. of Key-Value pair arguments - kwargs - Dictionary

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

cp(hamilton, kenwood, type(hamilton), type(kenwood))

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

cp(hamilton.__dict__ , kenwood.__dict__)


class Kettle:

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


hamilton = Kettle("HAMILTON", 1000)
hamilton.power = "15 Watts"
cp(Kettle.__dict__)
cp(hamilton.__dict__)

Kettle.power_source = "atomic"
cp(Kettle.__dict__)
cp(hamilton.__dict__)

hamilton.power_source = "gas"
cp(Kettle.__dict__)
cp(hamilton.__dict__)

########################## Methods - Part - I ##################################

"""
Reference: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/

if __name__ == "__main__": 
    print "Executed when invoked directly"
else: 
    print "Executed when imported"
    
"""

import datetime

class Account:

    @staticmethod
    def _current_time():
        return str(datetime.datetime.utcnow())

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = [("Opened the Account",self._current_time(),self.balance)]

        print("Account created for {} \nCurrent Ledger Balance: {}".format(self.name, self.balance))

    def show_balance(self):
        print("Current Ledger Balance: {0}".format(self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited: {0}".format(amount))
            self.show_balance()
            self.transactions.append(("Deposit", self._current_time(), amount))
        else:
            self.transactions.append("Failed Transaction")

    def with_draw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print("Amount Withdrawn: {0}".format(amount))
            self.transactions.append(("Withdrawn", self._current_time(), -amount))
        else:
            print("In-sufficient Balance - Transaction Cancelled")
            self.transactions.append(self._current_time(), "Transaction Cancelled")
        self.show_balance()

    def show_transactions(self):
        for transact in self.transactions:
            cp(transact)

if __name__ == "__main__":
    ac1 = Account("Sriram Ramanujam", 10000)
    ac1.deposit(500)
    ac1.with_draw(10499)
    ac1.deposit(999)
    ac1.show_balance()
    ac1.with_draw(500)
    ac1.show_transactions()







