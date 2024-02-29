# Exercise 5 - Cartesian product

def cartesian_product(set1: list, set2: list):
    """Return the cartesian product of two sets."""
    
    # write your code here





# Test cases
print(cartesian_product([1, 2], [3, 4])) # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(cartesian_product([1, 2, 3], [4, 5, 6])) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
print(cartesian_product([1, 2], [1, 2])) # [(1, 1), (1, 2), (2, 1), (2, 2)]
print(cartesian_product(['cat', 'dog'], ['elephant', 'hamster'])) # [('cat', 'elephant'), ('cat', 'hamster'), ('dog', 'elephant'), ('dog', 'hamster')]
print(cartesian_product([], [])) # []