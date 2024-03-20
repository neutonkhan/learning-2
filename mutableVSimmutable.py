'''
Immutable Variables:
Immutable variables cannot be changed after they are created.
Whenever you perform an operation that seems to modify an immutable object,
Python actually creates a new object with the modified value. Some examples of immutable data types in Python include:

'''

x = 5
print(id(x))
x += 1  # This creates a new integer object with the value 6
print(x)  # Output: 6
print(id(x))

y = 3.14
y += 1.0  # This creates a new float object with the value 4.14
print(y)  # Output: 4.14


s = "Hello"
s += " World"  # This creates a new string object with the value "Hello World"
print(s)  # Output: Hello World

print("tuple start=========================")
my_tuple = (1, 2, 3)
another_tuple = my_tuple
print("my tuple", my_tuple)
print("my tuple id", id(my_tuple))

print("Another tuple", another_tuple)
print("Another tuple id", id(another_tuple))
# Attempting to modify a tuple will result in an error
# my_tuple[0] = 4  # This will raise a TypeError: 'tuple' object does not support item assignment

# You can create a new tuple by concatenating existing tuples
my_tuple = my_tuple + (4, 5)

print ("After addition")

print("my tuple", my_tuple)
print("my tuple id", id(my_tuple))

print("Another tuple", another_tuple)
print("Another tuple id", id(another_tuple))


# Slicing a tuple also creates a new tuple
sliced_tuple = my_tuple[:2]  # Selecting the first two elements
print(sliced_tuple)  # Output: (1, 2)
print(id(sliced_tuple))


print("tuple end=========================")

'''
Mutable Variables:
Mutable variables, on the other hand, can be changed after they are created. 
When you modify a mutable object, you are actually modifying the original object.
Some examples of mutable data types in Python include:
'''
print("list =========================")
my_list = [1, 2, 3]

another_list = my_list
print("my list", my_list)
print("my list id", id(my_list))

print("Another list", another_list)
print("Another list id", id(another_list))

my_list.append(4)  # This modifies the original list by adding 4 to it
print("after append")

print("my list", my_list)
print("my list id", id(my_list))

print("Another list", another_list)
print("Another list id", id(another_list))

print("list =========================")

my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # This modifies the original dictionary by adding a new key-value pair
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}


my_set = {1, 2, 3}
my_set.add(4)  # This modifies the original set by adding 4 to it
print(my_set)  # Output: {1, 2, 3, 4}


