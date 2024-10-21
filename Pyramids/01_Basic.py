size = 5
for i in range(1, size+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()
size = 5
for i in range(size, 0, -1):
    for j in range(5, i-1, -1):
        print(j, end=" ")
    print()

print()
size = 5
for i in range(1, size+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()
size = 5
for i in range(size, 0, -1):
    for j in range(i, size+1):
        print(j ,end=" ")
    print()

print()
s = "abcde"
size = len(s)
for i in range(1, size+1):
    for j in range(1, i+1):
        print(s[j-1], end=" ")
    print()

print()
s = "ABCDE"
size = len(s)
for i in range(1, size+1):
    for j in range(1, i+1):
        print(s[j-1], end=" ")
    print()

print()
s = "abcde"
size = len(s)
for i in range(1, size+1):
    for j in range(i, 0, -1):
        print(s[j-1], end=" ")
    print()

print()
s = "ABCDE"
size = len(s)
for i in range(1, size+1):
    for j in range(i, 0, -1):
        print(s[j-1], end=" ")
    print()

print()
size = 5
for i in range(1, size+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print()
size = 5
for i in range(size, 0, -1):
    for j in range(i, size+1):
        print(i, end=" ")
    print()

print()
s = "abcde"
size = len(s)
for i in range(1, size+1):
    for j in range(1, i+1):
        print(s[i-1], end=" ")
    print()

print()
for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(i), end=" ")
    print()

print()
for i in range(101, 96, -1):
    for j in range(i, 102):
        print(chr(i), end=" ")
    print()

print()
s = "ABCDE"
size = len(s)
for i in range(size, 0, -1):
    for j in range(i, size+1):
        print(s[i-1], end=" ")
    print()

print()
size = 5
c = 1
for i in range(1, size+1):
    for j in range(1, i+1):
        print(c, end=" ")
        c+=1
    print()


# 15 Loops are completed
size = 5
print()
for i in range(1, size+1):
    for j in range(i, 0, -1):
        print(j%2, end=" ")
    print()

print()
for i in range(1, size+1):
    for j in range(i, 0, -1):
        print(0 if j%2==1 else 1, end=" ")
    print()

print()
for i in range(1, size+1):
    for j in range(1, i+1):
        print(i%2, end=" ")
    print()

print()
for i in range(1, size+1):
    for j in range(1, i+1):
        print(0 if i%2 == 1 else 1, end=" ")
    print()

print()
for i in range(size, 0, -1):
    for j in range(i, size+1):
        print(i, end=" ")
    print()

# 20 Loops are completed