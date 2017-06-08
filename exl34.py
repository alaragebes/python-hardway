## Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        ## dog is-a animal has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):
    def __init__ (self, name):
        ## cat is-a animal has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__ (self, name):
        ## person is-a object has-a name
        self.name = name

        ## person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__ (self, name, salary):
        ## super refers back to the upper class
        super (Employee, self).__init__(name)
        ## employee is-a person has-a salary
        self.salary = salary
         


## Fish is-a object
class Fish(object):
    pass
## Salmon is-a Fish
class Salmon (Fish):
    pass
## Halibut is-a fish
class Halibut (Fish):
    pass

## rover is-a dog has-a name Rover
rover = Dog ("Rover")

## satan is-a cat has-a name Satan
satan = Cat ("Satan")

## mary is-a person has-a name Mary
mary = Person ("Mary")

## mary has-a pet has-a satan kind
mary.pet = satan

## frank is-a employee has-a name Frank, has-a salary 120000
frank = Employee ("Frank", 120000)

## frank has-a pet has-a rover kind
frank.pet = rover

## flipper is-a Fish
flipper = Fish()
## crouse is-a Salmon
crouse = Salmon ()
## harry is-a halibut
harry = Halibut ()

frank.__init__("Frank", 120000)
print frank.__init__("Frank", 120000)
