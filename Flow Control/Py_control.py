'''
#while Loop
While expression:
    statement(s)

#While Else
'''

#while loop
num = int(input('Enetr a Number: '))
sum = 0
while num > 0 :
    sum = sum + num
    num = num - 1
print('The Sum is: ', sum)

#while else
counter = 0
while counter < 5 :
    print('Inside The Loop')
    counter = counter + 1
else:
    print('Outside The Loop')

#while loop using Break statement
num_sum = 0
count = 0
while count < 10:
    num_sum = num_sum + count
    count = count + 1
    if count == 5 :
        break
    print("Sum of First Count: ",count,"Integer is: ",num_sum)

#Continue using While loop
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable are: ',var)
print("Good Bye")

#For Loop
for a in range(3):
    print(a)
print('  ')
for b in range(2,7):
    print(b)
print('  ')
for c in range(2,19,5):
    print(c)

#for usign tuple
number = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for x in number:
    if x % 2:
        count_odd+=1
    else:
        count_even+=1
print("Number of Even: ",count_even)
print("Number of odd: ",count_odd)

#datalist 
datalist = [1234,11.22,1+2j,'Hello',True,(0,-1),[5,12],{'class':'v','Search':'A'}]
for x in datalist:
    print(type(x),x)

#dictionary 
color = {'c1':'red','c2':'white','c3':'black','c4':'cyan','c5':'yellow','c6':'green'}
for value in color.values():
    print(value)
for key in color:
    print(key)

#pass example
number = 0 #(1,2,3,4,5,6,7,8,9)
for number in range(10):
    if number == 5 :
        pass
    print('Number is: ',str(number))
print('out of loop :P ')

#for else
genre = ['rock','pop','jazz']
for i in range(len(genre)):
    print('I like: ',genre[i])
else:
    print('Kai Vadhyu Nathi!!')

