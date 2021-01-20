# Inheritance allows us to define a class that inherits all the methods and properties from another class.

#Parent class is the class being inherited from, also called base class.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Child class is the class that inherits from another class, also called derived class.
class Patient(Person):
    def patientID(self, numberID):
        self.nID = numberID
        print("Patient", self.firstname, self.lastname, "ID is:", self.nID)

#person1 = Person("Mickey", "Mouse")
patient1 = Patient("Mickey", "Mouse")
patient1.patientID("88")
