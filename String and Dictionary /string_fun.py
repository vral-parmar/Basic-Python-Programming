'''
#capitalize
string = "hello world what are you DoiNg"
new = string.capitalize()
print(new)

#count method
stra = "python is a cool is't it?"
sub = "is"
count = stra.count(sub)
print(count)

#find method 
quote = "let it be let it be let it be"
result = quote.find("let it")
print("let it = ",result)

quote = "let it be let it be let it be"
result = quote.find("small")
print("Small = ",result)

quote = "let it be let it be let it be"
result = quote.find("o small",10,-1)
print("o small = 10 nd -1",result)

quote = "let it be let it be let it be"
result = quote.find("things",6,20)
print(result)

#format method
# default argument
print("Hello {}, Your balance is {}".format("prince",12000))
#keyword argument
print("Hello {name}, Your balance is {bal}".format(name="prince",bal=12000))
#positional argument
print("Hello {0}, Your balance is {1}".format("prince",12000))
#mixed arguments
print("Hello {0}, Your balance is {bal}".format("prince",bal=12000))
'''