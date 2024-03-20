def sum_of_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example usage:
result = sum_of_all(1, 2, 3, 4, 5)
print("Sum:", result)  # Output: Sum: 15


def sum_of_values(dictionary):
    total = sum(dictionary.values())
    return total

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = sum_of_values(my_dict)
print("Sum of values:", result)  # Output: Sum of values: 6


def sum_of_values(**kwargs):
    total = sum(kwargs.values())
    return total

# Example usage:
result = sum_of_values(a=1, b=2, c=3)
print("Sum of values:", result)  # Output: Sum of values: 6
