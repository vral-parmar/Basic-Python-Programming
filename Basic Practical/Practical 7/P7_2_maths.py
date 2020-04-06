#The program takes the length and breadth from the user and finds the area of the rectangle using classes.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
 
    def area(self):
        return self.length * self.breadth
 
 
a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = Rectangle(a, b)
print("Area of rectangle:", obj.area())

'''
OP: 
Enter length of rectangle: 100
Enter breadth of rectangle: 200
Area of rectangle: 20000'''


'''