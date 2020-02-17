'''
#Syntax
def function_name(perameters):
    #code
    statements


'''

'''
#hello World in function
def my_func():
    print('kem 6o Mja ma :D')

my_func()

#use of return function
def sum (a, b):
    return a + b
a = int(input('Enter a Number: '))
b = int(input('Enter b Number: '))
print('Sum is: ',sum(a, b))

#When we dont know the arguments
def fun (*kids):
    print('The Youngest Child is: ',kids[2])
fun('emil','tobias','linus','lorem','ipsum')

#call by refrance by Passing Mutable Object 
def change(list1):
    list1.append(20)
    list1.append(30)
    list1.append(40)
    print('List inside Function: ',list1)
list1 = [1,2,3,4,5,6]
print('Outside The Function: ',list1)
change(list1)


#call by refrance using immutable object 
def lst(str):
    str = str + ' Hows You?'
    print('print The string inside a function: ', str)
string1 = 'Hi Im There'
lst(string1)


#required argument
def funct(name):
    message = 'Hi ' + name
    return message 
name = input('Eneter your name: ')
print(funct(name))

#keyword argument
#we can pass random order in it
def funct(name,message):
    print('maro bhai: ',name,'Ek dum',message,'che')
funct(name='Papdi',message='Pro')
#funct('Papdi','Pro')

#default arguments
def greet(name, msg = 'Good morning'):
    print('Hello ',name +','+ msg)

greet('papdi')
greet('sev','kem 6')

#variable length of arument
#writing * is mandatory
def len (*vari):
    print('The Output is: ')
    for i in vari:
        print(i)
    return
print('Calling With single Value')
len(50)
print('Calling With Multiple Value')
len(47,50,45,55,74)


#passing a list as arguments
def func(x):
    for i in x:
        print(i)

fruit = ['apple','bnana','orange','cherry']
func(fruit)

def cal(x):
    return 5 * x
print(cal(3))
print(cal(4))
print(cal(5))
print(cal(6))

#recursion using function calling again and again
def tri(k):
    if k > 0:
        result = k + tri(k - 1)
        print(result)
    else:
        result = 0
    return result

print('Recursion Example: ')
tri(6)

'''
