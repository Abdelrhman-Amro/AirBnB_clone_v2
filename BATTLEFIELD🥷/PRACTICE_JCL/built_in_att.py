#!/usr/bin/python3
class Employee:
   Ahmed = "GGGGAhmedGGGG"
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

obj = Employee()

print(obj.__class__)
print(obj.__dict__)

for x, y in obj.__dict__.items():
   print(x, y)
