# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum = sum + current
            current, next = next%10, (current + next)%10

    return sum % 10


from_, to = map(int, input().split())
print(fibonacci_partial_sum_naive(from_, to))
