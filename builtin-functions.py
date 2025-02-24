from functools import reduce

# 1. Multiply all numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)

# 2. Count uppercase and lowercase letters
def count_case(string):
    return sum(1 for char in string if char.isupper()), sum(1 for char in string if char.islower())

# 3. Check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# 4. Invoke square root after a delay
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    print(f"Square root of {number} after {delay_ms} milliseconds is {math.sqrt(number)}")

# 5. Return True if all elements in a tuple are true
def all_true(tup):
    return all(tup)