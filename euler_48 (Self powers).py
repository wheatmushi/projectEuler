def power (n):
    res = 1
    for i in range(0,n):
        res = res%10000000000
        res *= n
    return res

summa = 0

def summm (summa, res):
    return (summa+res)%10000000000

for n in range(1,1001):
    res = power(n)
    summa = summm(summa, res)

print(summa)
