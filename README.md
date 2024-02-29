# COM295 Topic 3 - Set Theory

Coding exercises covering Topic 3: Set Theory

## Exercise 1 - Unique Values

In the `1-unique.py` file, write a function called `unique_values()` that removes all duplicates from an arbitrary list and returns a new list.

> **Note:** Do not use the `set` data type or any built-in functions that remove duplicates.

## Exercise 2 - Set Operations

In the `2-set_operations.py` file, write a function called `set_operations()` that takes two arbitrary lists and returns a dictionary with the
following keys:

- `union`: a list of the union of the two lists
- `intersection`: a list of the intersection of the two lists
- `difference`: a list of the difference of the two lists
- `symmetric_difference`: a list of the symmetric difference of the two lists (i.e. A and B minus the intersection of A and B, i.e. the elements that are in one list but not both)

Duplicate values should be removed from the lists.

> **Note:** Do not use the `set` data type or any built-in set methods.

## Exercise 3 - Set Compare

In the `3-set_compare.py` file, write a function called `set_compare()` that takes two arbitrary lists and returns a dictionary with the following keys:

- `subset`: `True` if the first list is a subset of the second list, `False` otherwise
- `superset`: `True` if the first list is a superset of the second list, `False` otherwise
- `disjoint`: `True` if the two lists are disjoint, `False` otherwise
- `equal`: `True` if the two lists are equal, `False` otherwise
- `common`: a list of the common elements between the two lists

> **Note:** Do not use the `set` data type or any built-in set methods.

## Exercise 4 - Set Filter

In the `4-set_filter.py` file, write a function called `set_filter()` that takes an arbitrary list of numbers and returns a new list with only unique numbers that are greater than 15.

> **Note:** Do not use the `set` data type or any built-in set methods.

## Exercise 5 - Cartesian Product

In the `5-cartesian_product.py` file, write a function called `cartesian_product()` that takes two arbitrary lists and returns a list of tuples representing the Cartesian product of the two lists.

> **Note:** Do not use the `set` data type or any built-in set methods.
