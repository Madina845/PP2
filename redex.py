import re

# 1. Match 'a' followed by zero or more 'b's
def match_a_b(string):
    return bool(re.fullmatch(r'ab*', string))

# 2. Match 'a' followed by two to three 'b's
def match_a_b_limited(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

# 3. Find sequences of lowercase letters joined with an underscore
def find_lowercase_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

# 4. Find sequences of one uppercase letter followed by lowercase letters
def find_uppercase_lowercase(string):
    return re.findall(r'\b[A-Z][a-z]+\b', string)

# 5. Match 'a' followed by anything, ending in 'b'
def match_a_any_b(string):
    return bool(re.fullmatch(r'a.*b', string))

# 6. Replace all spaces, commas, or dots with a colon
def replace_special_chars(string):
    return re.sub(r'[ ,.]', ':', string)

# 7. Convert snake_case to camelCase
def snake_to_camel(string):
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# 8. Split a string at uppercase letters
def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

# 9. Insert spaces between words starting with capital letters
def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

# 10. Convert camelCase to snake_case
def camel_to_snake(string):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', string).lower()

# Testing examples
if __name__ == "__main__":
    print(match_a_b("abbb"))  # True
    print(match_a_b_limited("abb"))  # True
    print(find_lowercase_underscore("hello_world this_is a_test"))  # ['hello_world', 'this_is']
    print(find_uppercase_lowercase("Hello World Test example"))  # ['Hello', 'World', 'Test']
    print(match_a_any_b("axb"))  # True
    print(replace_special_chars("Hello, world. This is a test"))  # "Hello:world:This:is:a:test"
    print(snake_to_camel("hello_world_test"))  # "helloWorldTest"
    print(split_at_uppercase("HelloWorldTest"))  # ['', 'Hello', 'World', 'Test']
    print(insert_spaces("HelloWorldTest"))  # "Hello World Test"
    print(camel_to_snake("helloWorldTest"))  # "hello_world_test"