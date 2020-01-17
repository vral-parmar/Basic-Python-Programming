Dict = {1:'hello',2:'world',3:'john',4:'pagal'} # create dictionary
print(Dict.keys())  #priting Keys Only
print(Dict.values()) #printing Values Only
print(Dict) # Printing Both keys and Vlaues

#with Strings
thsdict = {
    'brand':'ford',
    'model':'mustang',
    'year':1966
}

thsdict['year']=2018
print(thsdict['year'])

#length Of items
print(len(thsdict))

#add Items
thsdict['color'] = 'Red'
print(len(thsdict))

#deleting Items using pop function
thsdict.pop('model')
print(thsdict.values())

#delete Using Del Keyword
del thsdict['color']
print(thsdict.values())

thisset = {'apple','bnana','orange','cherry','fruits'}
print(thisset)

#set Data type it is unordered its not modify onece is addeded

#declare set 
thisset = {"apple", "banana", "charry"}

#add items in Sets
thisset.add("orange")
print(thisset)

#add multiple item in set
thisset.update(['blackberry','mango','graps'])
print(thisset)

#check weather item in Set or not
print('apple' in thisset)

#print length of set
print(len(thisset))

#remove items frorm set will raise an error if item to remove then discarb will not raise any error
thisset.remove('banana')
print(thisset)

#delete last item using pop()
x = thisset.pop()
print(x)

#clear is used to delete all the element from the set 
thisset.clear()
print(thisset)

#join two sets both union() and update() will exclude the duplication
set1 = {'a','b','c','d'}
set2 = {1,2,3,4}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)
#python Operator (-arithmatic -assignment -coparison -logical -identitiy -membership -Bitwise)