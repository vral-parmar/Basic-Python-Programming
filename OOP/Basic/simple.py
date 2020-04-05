'''
#Self is used when we dont have to pass an argument the we can write self
class Test: 
	def fun(self): 
		print("Hello") 

obj = Test() 
obj.fun() 

#__init__method is similer to the Constructor in c or java

# A Sample class with init method 
class Person: 
	def __init__(self, name): 
		self.name = name 

	def say_hi(self): 
		print('Hello, my name is', self.name) 

p = Person('Viral') 
p.say_hi() 

# Python program to show that the variables with a value 
# assigned in class declaration, are class variables and 
# variables inside methods and constructors are instance 
# variables. 

# Class for Computer Science Student 
class CSStudent:  
	stream = 'cse'			
	def __init__(self, roll):  
		self.roll = roll	 

a = CSStudent(101) 
b = CSStudent(102) 

print(a.stream) # prints "cse" 
print(b.stream) # prints "cse" 
print(a.roll) # prints 101 

print(CSStudent.stream) 

# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
class MyClass: 
	__hiddenVariable = 10

myObject = MyClass()	 
print(myObject._MyClass__hiddenVariable) 

#printing an Objects
class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	def __str__(self): 
		return "From str method of Test: a is %s, b is %s" % (self.a, self.b) 		 
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 

# A Python program to demonstrate inheritance 

# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# equivalent to "class Person(object)" 
class Person(object): 
	def __init__(self, name): 
		self.name = name 

	def getName(self): 
		return self.name 

	def isEmployee(self): 
		return False

class Employee(Person): 
	def isEmployee(self): 
		return True

emp = Person("Viral") # An Object of Person 
print(emp.getName(), emp.isEmployee()) 

emp = Employee("virus") # An Object of Employee 
print(emp.getName(), emp.isEmployee()) 
'''
