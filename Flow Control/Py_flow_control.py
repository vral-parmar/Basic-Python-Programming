'''
#if statement 
stntax: 
if test expression:
    statement(s)

#if else statement
if test statement:
    statement(s)
else
    statement(s)

#else if statement its also called chaind condition
if test statement:
    statement(s)
elif
    statement(s)

#netsted if else statement
if test statement:
    if test statement:
        statement(s)
    else:
        statement(s)
else:
    statement(s)

'''

#if Condition 
inp = int(input('enter a number: '))
if inp<=10:         #if statement
    print(inp)

#if else statement
num = int(input('Enter the number: '))
if num % 2 == 0:
    print('Even')
else:
    print('Odd')

#else if statement
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))
if a > b and a > c:
    print('A is Great')
elif b > c:
    print('B is Great')
else:
    print('C is Great')

#nested If else Statement
n = int(input('Enter Number: '))
if n <= 15 :
    if n == 10 :
        print('Play Cricket')
    else:
        print('Play Kabbadi')
else:
    print('Dont Play Game')
