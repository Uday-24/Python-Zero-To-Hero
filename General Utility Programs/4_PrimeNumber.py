n = int(input("Enter number : "))

count = 0
for i in range(2, n):
    if n%i == 0:
        count += 1
        break

if count == 0:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is Not a Prime Number")