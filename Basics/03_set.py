print()
print("----------- Empty -----------")
empty_set = set()
print(empty_set)

print()
print("----------- With elements -----------")
my_set = {1, 2, 3, 4, 5}
print(my_set)

print()
print("----------- Set from list -----------")
my_set = set([1, 2, 3, 4])
print(my_set)


print()
print("----------- Set automatic remove duplicates -----------")
my_set = {1, 2, 3, 4, 1, 2, 8}
print(my_set)


print()
print("----------- Accessing elements -----------")
my_set = {1, 2, 3}
for i in my_set:
    print(i)



print()
print("----------- Adding and removing elements -----------")
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)


my_set.update([5, 6, 7])
print(my_set)