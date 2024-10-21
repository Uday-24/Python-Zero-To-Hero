n = int(input("Enter a year :"))

if n >= 0:
    if n % 4 == 0 and n%100 != 0:
        print("Leap year")
    elif n%400 == 0:
        print("Leap year")
    else:
        print("Not leap year")