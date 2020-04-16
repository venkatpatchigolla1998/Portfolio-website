class Pets:
    dog=[]
    def __init__(self,dogs):
        self.dogs=dogs
        self.is_walking=False
    def walk(self):
        self.is_walking=True
        
class Dog:
   species = 'mammal'
   def __init__(self, name, age):
       self.name = name
       self.age = age
       self.is_hungry=True
       self.is_walking=False
   def description(self):
       return "{} is {} years old".format(self.name, self.age)

   def speak(self, sound):
       return "{} says {}".format(self.name, sound)
   def eat(self):
       self.is_hungry=False
   def walk(self):
       self.is_walking=True

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
        
        
my_dogs=[Bulldog("Tom",6),
RussellTerrier("Fletcher",7),
Dog("Larry",9)]
pets=Pets(my_dogs)
print("I Have {} Dogs".format(len(pets.dogs)))
for dog in pets.dogs:
    #print(dog.name,dog.age)
   print("{} is {} years old".format(dog.name,dog.age))
print("and they are {} of course".format(dog.species))
all_are_hungry=False
for dog in pets.dogs:
    if dog.is_hungry:#intially we didn't call the eat function so the parameter is_hungry=True 
        all_are_hungry=True
if all_are_hungry:
    print("My dogs are not hungry")
else:
    print("My dogs are hungry")
for dog in pets.dogs:
    dog.walk()
    if dog.is_walking:
        print("{} is walking".format(dog.name))
