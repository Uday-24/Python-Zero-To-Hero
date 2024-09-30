# 21 Loops are completed
size = 5
for i in range(1, size+1):
    for j in range(1, size-1):
        print("{} {}".format(j, i), end=" ")
    print()

size = 5
for i in range(1, size+1):
    for j in range(1, size-1):
        print("{} {}".format(i, j), end=" ")
    print()

print()
print()
size = 5
for i in range(1, size+1):
    p = i
    for j in range(1, size+1):
        print("{:2d}".format(p), end=" ")
        p += size
    print()

print()
print()
size = 5
for i in range(size,0, -1):
    for j in range(1, size+1):
        print("{:2d}".format(i), end=" ")
        i = i+5
    print()

print()
print()
size = 5
for i in range(1, size+1):
    for j in range(1, size+1):
        print(i, end=" ")
        i+=1
    print()


print()
print()
size = 5
for i in range(1, size*2+1, 2):
    for j in range(1, size+1):
        print("{:2d}".format(i), end=" ")
        i+=2
    print()

print()
print()
size = 5
for i in range(1, size+1):
    for j in range(1, size+1):
        print(0 if i%2==1 else 1, end=" ")
        i += 1
    print()

print()
print()

size = 5
for i in range(1, size+1):
    for j in range(1, size+1):
        print(i%2, end=" ")
        i+=1
    print()


print()
print()
size = 5
for i in range(1, size+1):
    for j in range(0, size):
        print(i*j%2, end=" ")
    print()