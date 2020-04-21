#WAP to illustrate exception handling for two integers division for Divide by Zero error.
try:  
    a = int(input("Enter a:"))  
    b = int(input("Enter b:"))  
    c = a/b;  
    print("a/b = %d"%c)  
except Exception: print("can't divide by zero")  
else: print("Hi I am else block")  
