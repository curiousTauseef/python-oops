# Polymorphism

'''
Polymorphism means the ability to take various forms. 
Polymorphism allows us to define methods in the child class with the same name as defined in their parent class
'''

class Bird():
    def fly(self):
        print("Every bird can fly")

class Parrot(Bird):

    def fly(self):
        print("Parrot can fly")
    
    def talk(self):
        print("Parrots can imiatate human talk")

class Penguin(Bird):

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
a_parrot = Parrot()
a_penguin = Penguin()

# passing the object
flying_test(a_parrot)
flying_test(a_penguin)
