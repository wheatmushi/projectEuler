day=1
month=1
year=1900

def feb(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0: return 29
    else: return 28

days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

counter=0

while year<2001 :
    if day==7 and year>=1901:
        counter+=1
        #print(year,month)

    d=days_in_month[month]%7+day
    if d>7:
        day=d-7
    else:
        day=d

    if month==12:
        month=1
        year+=1
        days_in_month[2]=feb(year)
    else:
        month+=1

print(counter)
