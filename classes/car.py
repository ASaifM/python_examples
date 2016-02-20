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