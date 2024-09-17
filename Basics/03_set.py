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
print("----------- Adding elements -----------")
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)


my_set.update([5, 6, 7])
print(my_set)



print()
print("----------- Removing elements -----------")
my_set = {1, 2, 3}
my_set.remove(3)
print(my_set)

my_set.discard(5)
print(my_set)



print()
print("----------- Removing and returning an arbitrary element -----------")
my_set = {1, 2, 3}
item = my_set.pop()
print(my_set, item)



print()
print("----------- Set operations -----------")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # {1, 2, 3, 4, 5}
print(union_set)


intersection_set = set1.intersection(set2) # {3}
print(intersection_set)


difference_set = set1.difference(set2) # {1, 2}
print(difference_set)

symmetric_deff_set = set1.symmetric_difference(set2) # {1, 2, 4, 5}
print(symmetric_deff_set)


print()
print("----------- Set methods -----------")
set1 = {1, 2, 3}
set2 = {4, 5}

print(set1.isdisjoint(set2))

set2 = {1, 2, 3, 4}
print(set1.issubset(set2))

print(set2.issuperset(set1))


print()
print("----------- Frozen set -----------")
frozen_set = frozenset([1, 2, 3])
print(frozen_set)