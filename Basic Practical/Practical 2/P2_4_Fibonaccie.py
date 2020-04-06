number = int(input('Enter a Number: '))
i = 0
fibo = 1
s = 0
print('Series is: ')
while s < number:
    print(i)
    Temp = i + fibo
    i = fibo
    fibo = Temp
    s += 1
    
