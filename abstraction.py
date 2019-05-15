# Abstraction is the property by virtue of which only the essential details are displayed to the user.
# 

#Abstraction

# abstract base class module
import abc

class MyABCClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        return

    @abc.abstractmethod
    def get_val(self):
        return

# Child class inheriting from the above Abstract Base Class
class MyClass(MyABCClass):

    def set_val(self, input):
        self.val = input

    @abc.abstractmethod
    def get_val(self):
        return self.val

    def print_something(self):
        print("Not a abstract method in MyABCClass()")

my_class = MyClass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()
