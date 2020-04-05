string printing using diffrent string operations
str = "HelloWorld"
print("string = ", str)

print("String[0]=", str[0])
print("String[-1]=", str[-1])
print("String[1:5]=", str[1:5])
print("String[5:-2]=", str[5:-2])

#Multi line 
my_string = """Hello, Welcome to 
the World of python"""
print(my_string)

#find number of charecter in the given string 
count = 0
for letter in 'HelloWorld':
    if letter == 'l':
        count += 1
print(count,'Letter found')

#string escape sequence
#using quotes
print('He said, "What's there?"''')
#ecaping single quotes
print('He said, "What\'s there?"')
#using escaping double quote
print("He said, \"What's there?\"")


