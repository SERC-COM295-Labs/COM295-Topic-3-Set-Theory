# Exercise 2 - Set operations

def set_operations(set1: list, set2: list):
    """Return a dictionary with the intersection, union, difference and symmetric difference of two sets."""
    
    # write your code here



# Test cases
print(set_operations([1, 2, 3], [2, 3, 4])) # {'intersection': [2, 3], 'union': [1, 2, 3, 4], 'difference': [1], 'symmetric_difference': [1, 4]}
print(set_operations([1, 2, 3], [4, 5, 6])) # {'intersection': [], 'union': [1, 2, 3, 4, 5, 6], 'difference': [1, 2, 3], 'symmetric_difference': [1, 2, 3, 4, 5, 6]}
print(set_operations([1, 2, 3], [1, 2, 3])) # {'intersection': [1, 2, 3], 'union': [1, 2, 3], 'difference': [], 'symmetric_difference': []}
print(set_operations(['cat', 'dog', 'hamster',] ['cat', 'dog', 'elephant'])) # {'intersection': ['cat', 'dog'], 'union': ['cat', 'dog', 'hamster', 'elephant'], 'difference': ['hamster'], 'symmetric_difference': ['hamster', 'elephant']}
print(set_operations([], [])) # {'intersection': [], 'union': [], 'difference': [], 'symmetric_difference': []}