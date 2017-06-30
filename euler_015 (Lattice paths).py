xMax,yMax = 21,21
counter = {}

for i in range(1,xMax+1):
    counter[(i,yMax)]=1
    counter[(xMax,i)]=1

counter[(xMax,yMax)]=0

for x in range(xMax-1,0,-1):
    for y in range(yMax-1,0,-1):
        counter[(x,y)]=counter[(x+1,y)]+counter[(x,y+1)]

print(counter[(1,1)])
