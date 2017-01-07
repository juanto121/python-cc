#__variable sets visibility to private

class Animal:
	__name = None
	__height = 0
	__sound = 0

	def __init__(self, name, height, sound):
		self.__name = name
		self.__height = height
		self.__sound = sound

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_sound(self, sound):
		self.__sound = sound

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} tall says {}".format(self.__name,self.__height, self.__sound)

cat = Animal('SAM', 40, 'cat the cat')
print(cat.toString())

class Dog(Animal):
	__owner = ""

	def __init__(self, name, height, sound, owner):
		self.__owner = owner
		super(Dog, self).__init__(name, height, sound)

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dawg")

	def toString(self):
		return "Dog: {} is {} tall says {} from {}".format(self.get_name(),self.get_height(), self.get_sound(),self.__owner)

snoop = Dog("snoop", 49, "woof!", "Juan")

print(snoop.toString())


class AnimalTest:
	def get_type(self, animal):
		animal.get_type()

test_animal = AnimalTest()
test_animal.get_type(cat);
test_animal.get_type(snoop);

