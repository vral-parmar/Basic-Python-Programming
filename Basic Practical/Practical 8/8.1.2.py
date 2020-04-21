#2.WAP using list having two members character, integer and use exc_info() function to get type of exception.
import sys
a=input("Enter character: ")
b=int(input("Enter number: "))
try: c=a/b
except Exception: print(sys.exc_info())
