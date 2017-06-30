counted={1:1}

def path_length(n,length):
    if n in counted:
        return length + counted[n]
    elif n%2 == 0:
        return path_length(int(n/2),length+1)
    else:
        return path_length(int(3*n+1),length+1)

for n in range(2,1000000):
    counted[n] = path_length(n,0)

sort = sorted(counted.items(), key = lambda x: x[1], reverse = True)
print(sort[0])
