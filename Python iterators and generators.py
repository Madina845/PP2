#Create a generator that generates the squares of numbers up to some number N.
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2
N = 10 
print("Квадраты чисел до", N)
for square in square_generator(N):
    print(square)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Введите число n: "))
even_numbers = ', '.join(map(str, even_generator(n)))
print("Чётные числа от 0 до", n, ":", even_numbers)

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Введите число n: "))
print("Числа, кратные 3 и 4, от 0 до", n, ":")
for num in divisible_by_3_and_4(n):
    print(num)

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Введите начальное число a: "))
b = int(input("Введите конечное число b: "))
print("Квадраты чисел от", a, "до", b, ":")
for sq in squares(a, b):
    print(sq)

#Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Введите число n: "))
print("Обратный отсчет от", n, "до 0:")
for num in countdown(n):
    print(num)
