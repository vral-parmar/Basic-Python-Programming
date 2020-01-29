PI = 3.14
r = float(input('Enter the radius of the circle :'))
def area(PI,r):
    ret = PI * r * r
    return ret

print("Area of the circle is : %.2f" ,area(PI,r))