class Car:
	lightsOn = False
	engineOn = False
	doorsClosed = True
	drive = False
	owner = ""
	def __init__(self, owner):
		print ("Here is a shiny new car!")
		self.owner = owner	
	def openDoor(self):
		if self.doorsClosed:
			self.doorsClosed = False
			print ("We have opened the doors")
	def start_engine(self):
		if not self.engineOn: 
			self.engineOn = True
			print ("The engine has started!") 

class BMWCar(Car):
	def __init__(self, owner):
		Car.__init__(self,owner)
		print ("A BMW not just any car!")

	def adjust_seat(self):
		print ("Seat adjusted!")

	def openDoor(self):
		Car.openDoor(self)
		print("Not just any car but a BMW!")

class AudiCar(Car):
	def __init__(self,owner):
		super().__init__(owner)
		print ("Don't mess with me, I'm an Audi")

	def start_engine(self):
		super().start_engine()
		print ("Roar! Roar!")

class MercedesCar(Car):
	def __init__(self,owner):
		super(MercedesCar,self).__init__(owner)
		print ("Elegance is a trademark!")

class Food:
	pizza= True
	brocoli = False 
	lemonade = True
	kid= ""
	def __init__ (self, kid):
		print ("Who's hungry?")
		self.kid=kid
	def hungry (self):
		if self.pizza: 
			print ("Not Hungry")
