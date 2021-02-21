import time
from functools import lru_cache


@lru_cache(maxsize=256)
def function_long(a: int, b: int):
    print('Parameters are: {} and {}'.format(a, b))
    print('Waiting 5 seconds for the computation')
    time.sleep(5)

    return a + b


first_result = function_long(3, 3)
second_result = function_long(3, 3)
third = function_long(3, 4)
