from math import prod

import lambdas as lambdas


def add(a: int, b: int) -> int:
    """ADDS two numbers"""
    return a + b


print(add.__name__)
print(add.__name__)
print(add.__annotations__)


def operate(x, y, func):
    return func(x, y)


print(operate(2, 3, add))


def multiply(a):
    def by(b):
        return a * b

    return by


multiply_by_five = multiply(5)(6)
print(multiply_by_five)

add = lambda x, z: x + z
print(add(10, 9))

print(operate(2, 3, lambda a, b: a + b))
print(operate(2, 3, lambda a, b: a // b))
print(operate(2, 3, lambda a, b: b - a))
print(operate(2, 3, lambda w, y: w * y))
print(operate(2, 3, lambda w, y: w * y))

# import builtins

# sum = 67
# print(sum)
# builtins.
# print(abs(-1))
# print(round(56.67854, -1))
arr = [1, 2, 3, 5, 4, 7]
# print(sum(arr, 100))

letters = [['a'], ['b', 'c'], ['d'], ['e', 'f']]

# print(max([1,2,3,4,5,6]))

# fruits = "apple cucumber pear mango grape corn melon".split()
# print(min(fruits, key=len))
# print(max(fruits, key=len))
# print(max(fruits, key=lambda x: x[-3:]))

# print(max(key=lambda x: len(x['tweets'])))

iterable1 = (1, 2, 4, 3)
iterable2 = ('hello', 'how', 'are', 'you')
# print(list(zip(iterable2, iterable1)))
# print(sorted('helloAZX', reverse=True))
# print(sorted(iterable1, key=len))
# print(any())

# print(list(map(lambda x: x ** 2, [1, 2, 3, 4,5])))
# print([x**2 for x in list])
# print(list(map(str.upper,fruits)))

# print([x.upper()for x in fruits if not x.istitle()])
from functools import reduce


def max_func(acc, item):
    print(f"acc -> {acc} <> item -> {item}")
    return acc + item


print("###################### reduce ################")


def reduce_func(acc, item):
    print(lst)


print(reduce(reduce_func, lst, 100))
print(prod(lst, start=100))

print(reduce(lambda acc, item: acc if acc > item else item, fruits))

print(reduce(max_func, lst, fruits))
