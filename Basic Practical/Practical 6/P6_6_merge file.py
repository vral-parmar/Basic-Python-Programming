data = data2 = "" 
with open('Basic Practical/file1.txt') as fp: 
	data = fp.read() 
with open('Basic Practical/file2.txt') as fp: 
	data2 = fp.read() 
data += "\n"
data += data2 
with open ('Basic Practical/file3.txt', 'w') as fp: 
	fp.write(data) 
'''
Op:in file3.txt

Hello My name is Viral How are You
Hope You're doing well
in this quadretine day...
this is an example of File megring 
in python prgramming 
so How it is???????????????
'''