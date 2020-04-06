list1 = [10, 21, 4, 45, 66, 93] 
only_odd = [num for num in list1 if num % 2 == 1] 
only_even = [num for num in list1 if num % 2 == 0] 
list1.sort()
print("odd is: ",only_odd[-1]," and Even: ",only_even[-1]) 
