print("----------- Using parentheses -----------")
my_tuple = (1, 2, 3)
print(my_tuple)


print()
print("----------- Without parentheses -----------")
my_tuple = 1, 2, 3
print(my_tuple)


print()
print("----------- Empty tuple -----------")
empty_tuple = ()
print(empty_tuple)


print()
print("----------- With one element -----------")
one_element_tuple = (1,)
print(one_element_tuple)



print()
print("----------- Accessing the elemets -----------")
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])
print(my_tuple[-1])

print()
print("----------- Slicing -----------")
print(my_tuple[1:3])
print(my_tuple[-3:-1])
print(my_tuple[-2:])
print(my_tuple[:-1])


print()
print("----------- Concatenation -----------")
tpl1 = (1, 2)
tpl2 = (2, 3, 4)
tpl3 = tpl1 + tpl2
print(tpl3)


print()
print("----------- Repetition -----------")
tpl1 = (1, 2) * 3
print(tpl1)
print("Length = ", len(tpl1))
print(3 in tpl1)



print()
print("----------- Iterating -----------")
my_tuple = (10, 20, 30, 40, 50)
for i in my_tuple:
    print(i, end=" ")
print()



print()
print("----------- Tuple unpacking -----------")
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)



print()
print("----------- Methods -----------")
my_tuple = (1, 2, 3, 4, 5, 3)
print(my_tuple.count(3))
print(my_tuple.index(2))



print()
print("----------- Tuple to list -----------")
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print(my_list)


print()
print("----------- List to tuple -----------")
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print(my_tuple)