#Class: is a template. A set of things having some property or attribute in common and differentiated from others by kind, type, or quality. 
#In technical terms we can say that class is a blue print for individual objects with exact behaviour.
class PartyAnimal:
    x = 0

    #__init__(): is a reserved method in python classes. It is known as a constructor in object oriented concepts. 
    #            This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
    #self: self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far:', self.x)

    def __del__(self):
        print('I am destructed', self.x)


#call class = cs
cs = PartyAnimal()
cs.party()
cs.party()
cs = 42
print('cs contains', cs)
