import math


def map_func(numbers):
    res = map(lambda x: x * x, numbers)
    return list(res)


def filter_func(numbers):
    res = filter(lambda x: (x >= 3), numbers)
    return list(res)


def sorted_func(word):
    res = sorted(word)
    return list(res)


def sqrt_func(num):
    return round(math.sqrt(num))

def pow_func(num, power):
    return round(math.pow(num, power))

def hypot_func(x, y):
    return round(math.hypot(x, y))



if __name__ == "__main__":
    print(map_func([1, 2, 3, 4]))
    print(filter_func([1, 2, 3, 4]))
    print(sorted_func('cat'))
    print(sqrt_func(9))
    print(pow_func(2, 3))
    print(hypot_func(3, 4))
