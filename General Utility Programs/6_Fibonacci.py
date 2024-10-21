n = int(input("Enter Limit :"))
t1 = 0
t2 = 1

if n <= 0:
    print("Invalid Number for FIBONACCI Series")
elif n == 1:
    print(f"Fibonacci series is : {t1}")
else:
    print(f"Fibonacci series is : {t1} {t2}", end=" ")
    while(n > 2):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(t3, end=" ")
        n-=1