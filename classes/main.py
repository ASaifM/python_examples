from car import Car, Food, BMWCar

if __name__ == '__main__':
	car1 = Car("Carmen")
	car2=Car("Pavi")
	car3=Car("Poppy")
	car4=Car("Maria")
	car1.openDoor()
	car1.start_engine()
	car1.brand="BMW"
	print(car1.brand)

	kid1=Food('Carmen')
	kid2=Food('Minna')
	kid1.hungry()

	bmw_car = BMWCar("Zizo")
	bmw_car.start_engine()
	bmw_car.adjust_seat()
	print (bmw_car.owner)
	bmw_car.openDoor()

