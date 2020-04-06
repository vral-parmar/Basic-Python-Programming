#Use of multiple Inheritance
class Father:
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
class Mother:
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "mukesh"
s1.mothername = "Sonia"
s1.show_parent()
'''
OP:
Father : Mark
Mother : Sonia
'''