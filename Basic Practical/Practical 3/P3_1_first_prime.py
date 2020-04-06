le = 10
he = 20
print('Prime Number from 10 to 20 is', le,'are',he)
for n in range(1, he + 1):
    if n > 1:
        for i in range(2,n):
            if n % 2 == 0:
                break
            else:
                print(n)
            