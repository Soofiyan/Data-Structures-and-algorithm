# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current%10, (previous + current)%10
        sum += current * current

    return sum % 10


n = int(input())
print(fibonacci_sum_squares_naive(n))
