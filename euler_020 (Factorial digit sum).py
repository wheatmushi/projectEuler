def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(sum(int(i) for i in str(factorial(100))))
