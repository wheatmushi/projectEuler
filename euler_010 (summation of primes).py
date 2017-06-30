from math import sqrt, ceil

def isSimple(p):
    for i in range(2,ceil(sqrt(p))+1):
        if p%i == 0:
            return False
    return True

simple = [2,]

for p in range(2,2000000):
    if isSimple(p):
        simple.append(p)

print(sum(simple))
