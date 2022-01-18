class Student:
	name = 'anusha'	
	def __init__(self,rollno):
		self.roll = rollno
a = Student(1)
print ("Initially")

print ("a.name =", a.name )
a.name = "anu"

print ("\nAfter changing a.name")
print ("a.name =", a.name )

