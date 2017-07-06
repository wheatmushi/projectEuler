s='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

tr = [[int(n) for n in i.split()] for i in s.split('\n')]
tr.reverse()
top_string = [tr.pop(),]

def summation(top,bottom):
    left,right = [],[bottom[0]]
    for i in range(len(top)):
        left.append (top[i] + bottom[i])
        right.append(top[i] + bottom[i+1])
    left.append(bottom[-1])
    return left,right


for i in range(len(tr)):
    new_top = []
    bottom = tr.pop()
    for top in top_string:
        new_top += summation(top,bottom)
    top_string = new_top

maximum = max([max(s) for s in top_string])
print(maximum)
