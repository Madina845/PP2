#1.Convert Grams to Ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Example 
print(grams_to_ounces(100))  # Output: 2834.95

#2. Fahrenheit to Celsius
def fahr_to_cel(fahr):
    return (5 / 9) * (fahr - 32)

# Example
print(fahr_to_cel(100))  # Output: 37.78

#3.  Chicken and Rabbit Puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"

print(solve(35, 94))  # Output: (23, 12)

#4. Prime Numbers from a List
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example 
print(filter_prime([10, 3, 5, 17, 18, 29, 30, 37]))  # Output: [3, 5, 17, 29, 37]

#5. Print All Permutations of a String
from itertools import permutations

def print_permutations(string):
    for perm in permutations(string):
        print("".join(perm))

# Example 
print_permutations("abc") #Output:abc acb bac bca cab cba

#6. Reverse Words in a Sentence
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_sentence("We are ready"))  # Output: "ready are We"

#7. Check if a List Contains Two Consecutive 3s
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))  # Output: True
print(has_33([1, 3, 1, 3]))  # Output: False
print(has_33([3, 1, 3]))  # Output: False

#8. Check if a List Contains 007 in Order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False

#9. Compute the Volume of a Sphere
import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

# Example 
print(sphere_volume(3))  # Output: 113.097

#10. Remove Duplicates from a List 
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

#11.Check if a String is a Palindrome
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

#12. Print a Histogram
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])

#13. Guess the Number Game
import random

def guess_number():
    name = input("Hello! What is your name? ")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses = 0
    
    while True:
        guess = int(input("\nTake a guess: "))
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

#14. Importing Functions
