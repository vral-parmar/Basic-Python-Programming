#WAP to Count the number of objects of a class using constructor.

class Student :
    counter = 0
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        Student.counter += 1

    def printDetails(self) :
        print(self.name,self.age,"years old")

    
student1 = Student('Viral',22)
student2 = Student('prince',21)
student3 = Student('vanraj',21)

print("Total number of objects created: ",Student.counter)


'''
OP:
Total number of objects created:  3
'''