from math import sqrt, ceil

def isSimple(p):
    for i in range(2,ceil(sqrt(p))+1):
        if p%i == 0:
            return False
    return True

simple=[2,]
p=2

while len(simple)<10001:
    if isSimple(p):
        simple.append(p)
    p+=1

print(simple[10000])
