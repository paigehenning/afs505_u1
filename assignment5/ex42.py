#Animal is a class
class Animal(object):
    pass
# dog is a class of animal
class Dog(Animal):
    def __init__(self,name):
        #class dog has a function name (defines name)
        self.name=name
        print("woof")
#cat is a class of animal
class Cat(Animal):
    def __init__(self, name):
        #cat has a function name (defines name)
        self.name=name
        print("Meow")
#Person is a class
human_log={}
class Person(object):
    def __init__(self, name):
        #person has a function to define name
        self.name=name
        print("Hello")
        #person has a pet of some kind -- default is none
        self.pet = None
        human_log.update({name:self.pet})
        if self.pet!=None:
            human_log.update({name:self.pet}) #cannot figure out how to update this with the actual pet -_-
        else:
            pass
#Employee is a class of person
emplyee_log={}
class Employee(Person):
    def __init__(self,name,salary):
        #function defines name(posistion?) and salary
        super(Employee, self).__init__(name)
        emplyee_log.update({name:salary})
        print("Welcome to McDonald's! How may I help you?")
        #setting the variable salary to salary?
        self.salary=salary
        print(emplyee_log)
#there is the class fish
class Fish(object):
    pass
    print('''
       /`-._
      /_,.._`:-
  ,.-'  ,   `-:..-')
 : o ):';      _  {
  `-._ `'__,.-'\`-.)
      `\\\  \,.-'`
    ''')
#salmon is a class of fish
class Salmon(Fish):
    pass
#halibut is a class of fish
class Halibut(Fish):
    pass
#Rover is an object of dog named Rover
rover=Dog("Rover")
#Satan is an object of cat named Satan
satan=Cat("Satan")
#Mary is an object of person
mary = Person("Mary")
#Mary's pet has been defined as satan
mary.pet=satan
print(mary.pet)
#frank is an obhect of Employee with a salary of 120,000
frank=Employee("Frank",120000)
#frank has-a dog
frank.pet=rover
#flipper is an object of fish
flipper=Fish()
#crouse is an object of salmon
crouse=Salmon()
#harry is an object of halibut
harry=Halibut()
print(human_log)
