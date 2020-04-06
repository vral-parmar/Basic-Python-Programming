#multi-level Inheritance
class Family:
    def show_family(self):
        print("This is our family:")
 
class Father(Family):
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
class Mother(Family):
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)

class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  
s1.fathername = "Mukesh"
s1.mothername = "Sonia"
s1.show_family()
s1.show_parent()
'''
This is our family:
Father : Mukesh
Mother : Sonia
'''


