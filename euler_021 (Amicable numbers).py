from math import ceil, sqrt

def d(n):
    div = [1,]
    for i in range(2,ceil(sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            div.append(int(n/i))
    return sum(div)

maximum=10000
amicables=[]
n_div={}

for n in range(1,maximum):
    n_div[n] = d(n)

for n in range(1,maximum):
    if n_div[n]<maximum and n_div[n_div[n]]==n and n_div[n] != n:
        amicables.append(n)
    
print(sum(amicables))
