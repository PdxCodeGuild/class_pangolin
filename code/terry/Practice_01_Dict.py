# Given a the two lists below, combine them into a dictionary.

def combine(fruits, prices):
    result = zip(fruits, prices)
    resultSet = dict(result)
    return resultSet


fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]

# combine(fruits, prices)
print(f"{combine(fruits, prices)}")
