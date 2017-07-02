def letters_counter(num):
    if num==0: return 0
    elif num<10:
        if num in (1,2,6): return 3
        elif num in (4,5,9): return 4
        else: return 5
    elif 10<=num<20:
        if num in (11,12): return 6
        elif num in (13,14,18,19): return 8
        elif num in (15,16): return 7
        elif num == 17: return 9
        else: return 3
    elif 20<=num<100:
        if num//10 in (2,3,8,9): return 6 + letters_counter(num%10)
        elif num//10 in (4,5,6): return 5 + letters_counter(num%10)
        else: return 7 + letters_counter(num%10)
    elif 100<=num<1000:
        if num%100 == 0: return letters_counter(num//100) + 7
        else: return letters_counter(num//100) + 10 + letters_counter(num%100)
    elif num==1000: return 11

counter=0

for i in range(1,1001):
    counter += letters_counter(i)

print(counter)
