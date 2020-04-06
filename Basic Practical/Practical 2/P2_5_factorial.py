number = int(input('Enter a Number: '))
fact = 1
print('Factorial Series of: ', number, ' is ')
while number > 0:
    fact = fact * number
    number -= 1
    print(fact)