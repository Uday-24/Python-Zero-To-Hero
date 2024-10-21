def is_palindrome(n):
    temp = n
    palindrome = 0

    while temp != 0:
        rem = temp%10
        palindrome = palindrome + rem**3
        temp //= 10

    if palindrome == n:
        return True
    else:
        return False


n = int(input("Enter number :"))
if is_palindrome(n):
    print(f"{n} is a Palindrome number")
else:
    print(f"{n} is Not a Palindrome number")