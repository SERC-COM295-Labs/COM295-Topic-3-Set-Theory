# Exercise 4 - Set filter

def set_filter(data: list):
    """Return a list with unique elements from data that are greater than 15"""
    
    # write your code here




# Test cases
print(set_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # []
print(set_filter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # [20, 30, 40, 50, 60, 70, 80, 90, 100]
print(set_filter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # [20, 30, 40, 50, 60, 70, 80, 90, 100]
print(set_filter([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])) # [16, 18, 20]
print(set_filter([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])) # [17, 19]