n = int(input('Enter the number :'))
for i in range(1, n+1):
    fact = n % i
    if fact == 0:
        print(i)
