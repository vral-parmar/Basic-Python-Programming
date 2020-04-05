double = lambda x : x * 2
print(double(10))


#filter  function using lambda expression
my_list = [1,200,3,7,8,99]
new_list =list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

#map() function using lambda expression
my_list = [1,5,4,6,8,11,3,12]
new_list =list(map(lambda x: x * 2, my_list)) #multiply every item 
print(new_list)

