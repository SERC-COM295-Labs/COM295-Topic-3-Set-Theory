# Exercise 3 - Set compare

def set_compare(set1: list, set2: list):
    """Return a dictionary with boolean keys indicating if set1 is a subset, superset, disjoint or equal to set2, and a list of common elements."""

    # write your code here



# Test cases
print(set_compare([1, 2, 3], [2, 3, 4])) # {'subset': False, 'superset': False, 'disjoint': False, 'equal': False, 'common_elements': [2, 3]}
print(set_compare([1, 2], [1, 2, 3, 4])) # {'subset': True, 'superset': False, 'disjoint': False, 'equal': False, 'common_elements': [1, 2]}
print(set_compare([1, 2, 3], [4, 5, 6])) # {'subset': False, 'superset': False, 'disjoint': True, 'equal': False, 'common_elements': []}
print(set_compare([1, 2, 3], [1, 2, 3])) # {'subset': True, 'superset': True, 'disjoint': False, 'equal': True, 'common_elements': [1, 2, 3]}
print(set_compare(['cat', 'dog', 'hamster'], ['cat', 'dog', 'elephant'])) # {'subset': False, 'superset': False, 'disjoint': False, 'equal': False, 'common_elements': ['cat', 'dog']}
print(set_compare([], [])) # {'subset': True, 'superset': True, 'disjoint': True, 'equal': True, 'common_elements': []}