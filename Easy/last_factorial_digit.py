from math import factorial

T = int(input())

for _ in range(T):
    N = int(input())
    factorial_number = factorial(N)
    last_digit = factorial_number % 10
    print(last_digit)
