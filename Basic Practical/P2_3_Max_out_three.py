one = int(input('Enter a First Number: '))
two = int(input('Enter a Second Number: '))
three = int(input('Enter a third number: '))

if one > two and one > three:
    print(one, 'is a Largest Number')
elif two > three:
    print(two, 'is a Largest Number')
else:
    print(three, 'is a Largest Number')

if one < two and one < three:
    print(one, 'is a Smallest Number')
elif two < three:
    print(two, 'is a Smallest Number')
else:
    print(three, 'is a Smallest Number')
    