def Sum(Dict): 	
	sum = 0
	for i in Dict: 
		sum = sum + Dict[i] 
	return sum

dict = {'aa': 1100, 'bb':1200, 'cc':1300} 
print("Sum :", Sum(dict)) 
