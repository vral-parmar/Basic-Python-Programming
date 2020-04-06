def intrest(p,t,r):
    return (p*t*r)/100
p=float(input('Enter Principal: ')) 
t=float(input('Enter Year: '))
r=float(input('Enter The interest: '))
print('Simple Interest is: ',intrest(p,t,r))