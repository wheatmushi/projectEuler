from time import time

f = open('p022_names.txt','r')
names = f.read()
names = names.replace('"','').split(',')
names.sort()

def nameToValue(name):
    return sum([ord(i)-64 for i in name])

total=0

for i in range(0,len(names)):
    total += (i+1)*nameToValue(names[i])

print(total)

