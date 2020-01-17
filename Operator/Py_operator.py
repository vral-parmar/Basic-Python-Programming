'''
There are following Arithmatic operator
+ addition
- substraction
* multiphication
/ division 
// round the result
** Exponants

Assignment Operator
 = assign value
 += add and     a = a + b       a+=b
 -= sub and     a = a - b       a-=b
 *= mul and     a = a * b       a*=b
 /= div and     a = a / b       a/=b
 %= per a =     a % b           a%=b
 //= floor and  a = a // b      a//=b
**= Expo and    a = a ** b      a**=b
&= Bitwise and  a = a & b       a&=b
|= Bitwise or           
^= Bitwise Ex-or
>>= Right Shift
<<= Left Shift

#comparision Operator
== Equal to         a == b
!= not eqaul to     a != b
> Greater than      a > b
< Less than         a < b
>= Greater than equal to a >= b
<= Less than Equal to    a <= b

#logical Oerations
and  return True if both are true
or   return True if One of the true
not  Reverae the Op

#identity Operator
Its used to compare the Object 
is ``````x is y     return true if both are same 
is not```x is not y return true 
it's also compare the memory location

#membership Operator
in      return true if a sequence with the value is present
not in  return true if a sequence with the value is not present

#bitwise Operator
&   and     
|   or
^   xor
~   not
<<  zero fill left shift
>>  sign right shift

'''
one = 4
two = 5
#Exponents
print(one ** two)
#Floor division
print(one // two)

#comparison operator
print(one > two)
print(one != two)

#logical Operation
print(one > two and two < one)
print(not(one > two and two < one))

#identitiy Operator
x = ['banana','apple']
y = ['banana','apple']
z = x
print(x is y)
print(x is not y)

#membership Operator
print( 'banana' in x )

#Bitwise Operator
print(one & two)