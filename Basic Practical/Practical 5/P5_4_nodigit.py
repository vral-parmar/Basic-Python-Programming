n=int(input("Enter a number:"))
c=0
while(n>0):
    c=c+1
    n=n//10
print("Number of digits:",c)