"""
class animals:                       #created class named animal
    def Shape_Size_of_animals(self): #method
        print("shape,size")          #method config

lion = animals()                     #created object named lion and it will have config of class animals
lion.Shape_Size_of_animals()         #accesing config of animal class
"""

""" ------------------------------------creating variables----------------------------------------"""

class animals:
    def __init__(self,size):# constructor
         self.eyes = 2      #private variable eyes
         self.legs = 4      #private variable legs
         self.living = True #protected variable living
         self.size = size



    def geteyes(self):
        return self.eyes

    def getlegs(self):
        return self.legs

    def setlegs(self,legs):
        self.legs = legs

    def getsize(self):
        return self.size

    def setsize(self, size):
        self.size = size

    def getliving(self):
        return self.living

    def setliving(self,living):
        self.living = living


class Lion(animals):

    def eats(self):
        print("Lion eats meat!")

    def color(self):
        print("Color of Lion is Grayish Yellow!")

    def sound(self):
        print("A lion roars!")

    def typeOfAnimal(self):
        print("Lion is a carnivorous animal")

#c = Lion.eats()
#print(c)

class Tiger(animals):

    def eats(self):
        print("A tiger eats meat!")

    def color(self):
        print("Color of Tiger is orange with black stripes!")

    def sound(self):
        print("A tiger roars!")

    def typeOfAnimal(self):
        print("Tiger is a carnivorous animal")

class Giraffe(animals):

    def eats(self):
        print("Giraffe eats leaves off the trees!")

    def color(self):
        print(
            "Giraffe has patterns of dark brown, orange, or chestnut spots broken up by white or cream-coloured stripes!")

    def sound(self):
        print("A giraffe makes a flute like sound!")

    def typeOfAnimal(self):
        print("Giraffe is a herbivorous animal")


class Zebra(animals):

    def eats(self):
        print("Zebra eat grass!")

    def color(self):
        print("A Zebra has black and white stripes on its body.")

    def sound(self):
        print("Zebras either bark, bray or snort!")

    def typeOfAnimal(self):
        print("Zebra is a herbivorous animal")


class Monkey(animals):

    def eats(self):
        print("Monkey eats vegetables and fruits")

    def color(self):
        print("Color of monkey is brown")

    def sound(self):
        print("A monkey makes a screeching sound!")

    def typeOfAnimal(self):
        print("LMonkey is a herbivorous animal")


class Dog(animals):

    def eats(self):
        print("A dog eats meat, veggies, dog-food etc.!")

    def color(self):
        print("A dog could be of any color, it depends on the breed.")

    def sound(self):
        print("A dog barks!")

    def typeOfAnimal(self):
        print("Dog is an omnivorous animal")


class Rat(animals):

    def eats(self):
        print("LRat eats flesh, leftover food, garbage etc.!")

    def color(self):
        print("Rats can be white, black or gray in color!")

    def sound(self):
        print("A rat squeaks!")

    def typeOfAnimal(self):
        print("Rat is an omnivorous animal")


class Kangaroo(animals):

    def eats(self):
        print("A Kangaroo eats vegetables, plants, leaves!")

    def color(self):
        print("A Kangaroo is blue-grey or brown in color!")

    def sound(self):
        print("A Kangaroo growls or barks!")

    def typeOfAnimal(self):
        print("Kangaroo is a herbivorous animal")


class PolarBear(animals):

    def eats(self):
        print("Polar Bear eats meat!")

    def color(self):
        print("Color of Polar Bear is off white or bright white.")

    def sound(self):
        print("A polar bear makes sounds like hissing, growling or champing of teeth!")

    def typeOfAnimal(self):
        print("Polar Bear is a carnivorous animal")


class Deer(animals):

    def eats(self):
        print("A deer eats plants, leaves!")

    def color(self):
        print("Color of Lion is Reddish brown or Grayish brown!")

    def sound(self):
        print("A Deer makes a grunting sound or a bleating sound!")

    def typeOfAnimal(self):
        print("Deer is a herbivorous animal")











