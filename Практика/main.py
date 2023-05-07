# 1).
# Input:
# 1) Бананы
# 2) Яблоки
# 3) Макароны
# 4) Кофе

def printGroceries(*args):
    counter = 0
    for i in args:
        if type(i) == str and len(i) >= 2:
            counter += 1
            print(f"{counter})", i, end="\n")


printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)


# 2).
# Input:
# age: 28
# first_name: John
# last_name: Doe
# position: Python developer

def personalData(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f"{k}: {v}")


personalData(first_name='John', last_name='Doe', age=28, position='Python developer')


# 3).

# Напишите функцию evaluate(coefficients, x), которая принимает список коэффициентов и значение аргумента x.
# При реализации можно использовать анонимные lambda-функции, а также встроенные функции map() и reduce().

# Ввод:
# 2 4 3
# 10

# Вывод:
# 243

def evaluate(coefficients, x):
    s = 0
    for i in coefficients:
        s = s * x + i
    print(s)


evaluate([2, 4, 3], 10)


# 4).

def sogl(strin, vowels):
    result = list(map(lambda x: "glasn" if x in vowels else "soglas", strin))
    return result


print(sogl("яжертыуиопшщасдфгчйклзхцвбнм", 'аиеёоуыэюя'))

# 5).
# Например
# 30 / 3 = 10

def func(lst, three):
    result = list(map(lambda x: x if x / three in list(range(0, 100, 2)) and x % 2 == 0 else "no", lst))
    return result


print(func([1, 8, 12, 17, 5, 19, 14, 7, 20, 3, 9, 2, 16, 4, 11, 18, 6, 10, 15, 13], 3))


# 6).

def positive(num):
    return num >= 0


def main(numbers):
    result = list(map(lambda x: x ** 2, filter(positive, numbers)))
    return result


print(main([-4, 2, 5, 2, -6, -3, 2, -3, -1, 0, 3]))


# 7).

def kratno(num):
    return num % 3 == 0


def main1(numbers):
    result1 = list(map(lambda x: x ** 3, filter(kratno, numbers)))
    return result1


def main2(numbers):
    result2 = list(map(lambda x: x, filter(kratno, numbers)))
    return result2


print(main1([-4, 2, 5, 2, -6, -3, 2, -3, -1, 0, 3]))
print(main2([-4, 2, 5, 2, -6, -3, 2, -3, -1, 0, 3]))


# 8).

def zipper(spis1, spis2):
    dir = {}
    for key, value in zip(spis1, spis2):
        dir[key] = value
    return dir


print(zipper([1, 2, 3, 4], ["Nadia", "Petia", "Leha", "Vania"]))

# 9).

from functools import reduce


def redu(num):
    if num % 2 == 0:
        return num


def main(numbers):
    result = reduce(lambda a, b: a * b, filter(redu, numbers))
    return result


print(main([1, 2, 3, 4, 5]))
