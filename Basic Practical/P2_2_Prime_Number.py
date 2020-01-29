number = int(input('Enter a Number: '))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'Number is a Prime ')
            break
        else:
            print(number,'Number is not a Prime ')
else:
    print(number, 'Number is Not a Prime Number ')