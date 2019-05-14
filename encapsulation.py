class Human():

    #private var
    __privateVar = "this is __private variable"

    # constructor method
    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    # public method
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    # private method
    def __privateMethod(self):
        return "Private method"

    # public method that returns a private variable
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def showClassName(self):
        return "Male"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    def showClassName(self):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()


human = Human()
print(human.className)
print(human.showName("Vasya"))
print(human.showPrivate())
# print(human.privateMethod())
print("\n")

male = Male()
print(m.className)
print(male.showClassName())
# print(male.showPrivate())
print("\n")

female = Female()
print(female.className)
print(female.showClassName())
print("\n")
