class Person():
	def __init__(self, name : str, age : int):
		self.name = name 
		self.age = age
		
	def introduce(self):
		print(f"Hola soy {self.name} y tengo {self.age} años.")

class Bus():
	def __init__(self, max_passengers : int ):
		self.max_passengers = max_passengers
		self.passengers = [] #Almacenar la cantidad de personas que van subiendo al bus

	def add_passengers(self, person : Person ):
		if len(self.passengers) < self.max_passengers:
			self.passengers.append(person)
			print(f"{person.name} ha subido al bus.")
		else:
			print("El bus está lleno.")

	def remove_passengers(self, person : Person ):
		if person in self.passengers:
			self.passengers.remove(person)
			print(f"{person.name} ha bajado del bus.")
		else:
			print("Esta persona no está en este bus.")


persona_1= Person("Jonathan", 25)
persona_2= Person("Marbely", 32)
persona_3= Person("Angelica",51 )
persona_4= Person("Alberto", 49)
persona_5= Person("David", 22)
persona_6= Person("Emanuel", 17)

my_bus = Bus(3)

my_bus.add_passengers(persona_1)
my_bus.add_passengers(persona_2)
my_bus.add_passengers(persona_3)
my_bus.add_passengers(persona_4)

my_bus.remove_passengers(persona_3)

