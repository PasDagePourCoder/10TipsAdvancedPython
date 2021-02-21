import time
import sys


def factorial(n: int) -> int:
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result


sys.setrecursionlimit(100000)


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


# Comparison of time
start = time.time()
factorial(20000)
end = time.time()
print("Time factorial classic = %s" % (end - start))

start = time.time()
factorial_recursive(20000)
end = time.time()
print("Time factorial recursive = %s" % (end - start))


