from math import ceil,sqrt
from itertools import combinations_with_replacement

def divisors(n):
    div = [1,]
    for i in range(2,ceil(sqrt(n))):
        if n%i == 0:
            div.append(i)
            div.append(int(n/i))
    return sum(set(div))

abundants=[]

for n in range(1,28124):
    if n<divisors(n):
        abundants.append(n)

abundants_sums=[]

for i in combinations_with_replacement(abundants,2):
    s=sum(i)
    abundants_sums.append(s)

ab=set(abundants_sums)
total=0

for i in range(1,28124):
    if i not in ab:
        total+=i

'''
for n in range(1,28124):
    for m in abundants:
        if n<2*m:
            break
        if n-m in abundants:
            total-=n
            break
            '''
print(total)
