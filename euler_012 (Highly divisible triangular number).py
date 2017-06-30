from math import ceil, sqrt
from time import time

cur_time = time()

def divisors(n):
    div = [1,]
    for i in range(2,ceil(sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            div.append(int(n/i))
    div.append(n)
    return div

def triangular(count):
    tri=1
    i = 2
    while len(divisors(tri))<count:
        tri += i
        i += 1
    return tri

print(triangular(500))
print('counting time =',time()-cur_time)
