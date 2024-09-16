print("----------------- Empty List -----------------")
my_list = []
print("Empty list : ", my_list)


print()
print("----------------- List with items -----------------")
my_list = [10, 20, 30, 40, 50]
print("List with items : ", my_list)



print()
print("----------------- Mixed List -----------------")
mixed_list = [10, "Hello", 3.14, True]
print("Mixed list : ", mixed_list)



print()
print("----------------- Accessing elements -----------------")
my_list = [10, 20, 30, 40, 50]
first_item = my_list[0]
last_item = my_list[-1]
print(first_item, last_item)



# Slicing a list
print()
print("----------------- Slicing a list -----------------")
my_list = [10, 20, 30, 40, 50]
sub_list = my_list[1:3]
print("Sub list : ", sub_list)

sub_list = my_list[:3]
print("Sub list : ", sub_list)

sub_list = my_list[2:]
print("Sub list : ", sub_list)



# Modifying list
print()
print("----------------- Modifying List -----------------")
my_list = [10, 20, 30, 40, 50]

my_list[2] = 100
print(my_list)

my_list.append(60)
print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.remove(100)
print(my_list)

print("Length of my_list : ", len(my_list))



# Concatenating lists
print()
print("----------------- Concatenating Lists -----------------")
list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print(list3)


# Repeating list
print()
print("----------------- Repeating List -----------------")
list3 = list1 * 3
print(list3)



# Iterating over a list
print()
print("----------------- Iterating over a List -----------------")
my_list = [10, 20, 30, 40, 50]

for item in my_list:
    print(item, end=" ")

print()



# List methods
print()
print("----------------- List Methods -----------------")
my_list = [20, 50, 30, 40, 10]
my_list.sort()
print(my_list)

my_list.pop(1) # Arguement is optional
print(my_list)

my_list.reverse()
print(my_list)

idx = my_list.index(50)
print(idx)

my_list.append(10)
n = my_list.count(10)
print(n)



# List Comprehensions
print()
print("----------------- List Comprehensions -----------------")
numbers = [x for x in range(1, 11)]
print(numbers)

squares = [x**2 for x in range(1, 11)]
print(squares)

evens = [x for x in range(1, 10) if x%2 == 0]
print(evens)