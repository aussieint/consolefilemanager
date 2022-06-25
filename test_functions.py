from func_for_test import map_func, filter_func, sorted_func, sqrt_func, pow_func, hypot_func


def test_map_test():
    assert map_func([1, 2, 3]) == [1, 4, 9]

def test_filter_func():
    assert filter_func([1, 2, 3, 4]) == [3, 4]

def test_sorted_func():
    assert sorted_func('dog') == ['d', 'g', 'o']

def test_sqrt_func():
    assert sqrt_func(16) == 4

def test_pow_func():
    assert pow_func(4, 2) == 16

def test_hypot_func():
    assert hypot_func(6, 8) == 10