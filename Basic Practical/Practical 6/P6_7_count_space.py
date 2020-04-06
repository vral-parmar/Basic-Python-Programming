f = open ('Basic Practical/test.txt', 'r')
s = f.read()
count=0
line = s
for i in line:
    if(i.isspace()):
        count=count+1
print("The number of blank spaces is: ",count)

'''
OP: 
content of file 
Hello 
This is RSU 
This is Lavad 
This is Dehgam 


The number of blank spaces is:  14
'''