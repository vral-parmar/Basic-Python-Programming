#Create a student class with attributes rool_no, name, age and create parameterized constructor to define values of it. Also use PrintDetails() function to print values of 5 different students and print total number of objects created.
class Student:
    def __init__(self,name,ids,college):
        print("This is a parmeterized costructor in python:")
        self.name=name
        self.ids=ids
        self.college=college
        
    def Display_Details(self):
        print("Student Details:")
        print("Student Name:",self.name)
        print("Student ids:",self.ids)
        print("Student college:",self.college)

student=Student("Yash",2023,"Kcc")
student.Display_Details()
student=Student("Rajesh",2021,"Gcc")
student.Display_Details()
student=Student("Ramesh",2028,"Pcc")
student.Display_Details()
student=Student("suresh",2028,"Scc")
student.Display_Details()
student=Student("Raj",2122,"Bcc")
student.Display_Details()


'''
OP:
This is a parmeterized costructor in python:
Student Details:
Student Name: Yash
Student ids: 2023
Student college: Kcc
This is a parmeterized costructor in python:
Student Details:
Student Name: Rajesh
Student ids: 2021
Student college: Gcc
This is a parmeterized costructor in python:
Student Details:
Student Name: Ramesh
Student ids: 2028
Student college: Pcc
This is a parmeterized costructor in python:
Student Details:
Student Name: suresh
Student ids: 2028
Student college: Scc
This is a parmeterized costructor in python:
Student Details:
Student Name: Raj
Student ids: 2122
Student college: Bcc

'''