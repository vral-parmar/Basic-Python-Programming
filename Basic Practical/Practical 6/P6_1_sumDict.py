def returnSum(myDict): 	
	sum = 0
	for i in myDict: 
		sum = sum + myDict[i] 
	return sum
dict = {'a': 10, 'b':20, 'c':300} 
print("Sum :", returnSum(dict)) 
