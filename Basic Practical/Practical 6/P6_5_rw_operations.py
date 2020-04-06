
file1 = open("Basic Practical/test.txt","w") 
L = ["This is RSU \n","This is Lavad \n","This is Dehgam \n"] 
file1.write("Hello \n") 
file1.writelines(L) 
file1.close() 
file1 = open("Basic Practical/test.txt","r+") 

print ("Output of Read function is ")
print (file1.read())
print(" ")
file1.seek(0) 
print ("Output of Readline function is ")
print (file1.readline())
print(' ')
file1.seek(0) 
print ("Output of Read(9) function is ")
print (file1.read(9))
print(' ')
file1.seek(0) 
print ("Output of Readline(9) function is ")
print (file1.readline(9))
file1.seek(0) 
print ("Output of Readlines function is ")
print (file1.readlines())
print(' ')
file1.close() 

'''
Output of Read function is 
Hello 
This is RSU 
This is Lavad 
This is Dehgam 

 
Output of Readline function is 
Hello 

 
Output of Read(9) function is 
Hello 
Th
 
Output of Readline(9) function is 
Hello 

Output of Readlines function is 
['Hello \n', 'This is RSU \n', 'This is Lavad \n', 'This is Dehgam \n']
 
crimson@crimson-PC:~/Desktop/Basic-Python-Programming$  env DEBUGPY_LAUNCHER_PORT=46715 /usr/bin/python3 /home/crimson/.vscode/extensions/ms-python.python-2020.3.71113/pythonFiles/lib/python/debugpy/wheels/debugpy/launcher "/home/crimson/Desktop/Basic-Python-Programming/Basic Practical/P6_5_rw_operations.py" 
Output of Read function is 
Hello 
This is RSU 
This is Lavad 
This is Dehgam 

 
Output of Readline function is 
Hello 

 
Output of Read(9) function is 
Hello 
Th
 
Output of Readline(9) function is 
Hello 

Output of Readlines function is 
['Hello \n', 'This is RSU \n', 'This is Lavad \n', 'This is Dehgam \n']


in file
Hello 
This is RSU 
This is Lavad 
This is Dehgam 
'''