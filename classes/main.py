from car import Car, Food

if __name__ == '__main__':
	car1 = Car("Carmen")
	car2=Car("Pavi")
	car3=Car("Poppy")
	car4=Car("Maria")
	car1.openDoor()
	car1.start_engine()
	car1.brand="BMW"
	print(car1.brand)

if __name__ == '__main__':
	kid1=Food('Carmen')
	kid2=Food('Minna')
	print(kid1.hungry())