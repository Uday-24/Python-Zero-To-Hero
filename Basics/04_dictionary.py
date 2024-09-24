print()
print("----------- Basic -----------")
student = {
    'name' : 'Uday',
    'age' : 20,
    'course' : 'BCA'
}
print(student)
print(student['name'])
print(student['age'])
print(student['course'])

print()
print("----------- Empty -----------")
my_dict = {}
print(my_dict)

my_dict['name'] = 'Uday'
my_dict['age'] = 20
print(my_dict)


print()
print("----------- Access -----------")
# print(my_dict['course']) Error
print(my_dict.get('course', 'Not availabe'))


print()
print("----------- Removing elements -----------")
del my_dict['age']
print(my_dict)

name = my_dict.pop('name')
print(name, my_dict)



print()
print("----------- Methods -----------")
student = {
    'name' : 'Uday',
    'age' : 20,
    'course' : 'BCA'
}

print(student.keys())
print(student.values())
print(student.items())


print()
print("----------- Iterating -----------")

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key} : {value}")


