class Animal(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def shout(self):
		print(f"Hi fellas my name is true dabber {self.name} and my big man age is a big {self.age} bruv")

class Dog(Animal):
	def __init__(self, name, age):
		super().__init__(name, age)
	

import Animal.shout as hello

dog = Dog("spot", 3)
hello(dog)
		
