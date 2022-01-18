class Vehicle:
	type1='vehicle1'
	type2='vehicle2'
class Bus(Vehicle):
	type3='govtbus'
	type4='privatebus'
class Car(Vehicle):
	type5='BMW'
	type6='maruti'
b=Bus()
print(b.type3)
c=Car()
print(c.type5)