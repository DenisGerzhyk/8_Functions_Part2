# 1).

def count_elements(lst, s):
    counts = {}
    for element in lst:
        counts[element] = s.count(element)
    return counts


print(count_elements(['i', 'was'], "Hey , i was in market"))


# 2).

def func(n):
    result = round(max(n) - min(n), 2)
    return result


print(func((10.2, -2.2, 0, 1.1, 0.5)))


# 3).

def generate_odd_numbers(n):
    for i in range(1, n + 1):
        yield i ** 3


for odd_number in generate_odd_numbers(5):
    print(odd_number)


# 4).

def func(string):
    for i in string:
        if 'A' in i:
            yield i


for i in func(["Hey Im Ann", "I look good", "Yea,i know"]):
    print(i)


# 5).

def func(word):
    num = 1
    for i in word:
        if num == len(word):
            break
        else:
            yield i + word[num]
            num += 1


def func2(word):
    yield word[0] + word[len(word) - 1]


for i in func("allerg"):
    print(i)
for i in func2("allerg"):
    print(i)


# 6).

def func(number):
    a, b = 0, 1
    while a <= number:
        yield a
        a, b = b, a + b


for i in func(100):
    print(i)
