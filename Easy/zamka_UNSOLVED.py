def number():
    L = int(input())
    D = int(input())
    X = int(input())

    N = 0
    M = 0
    digits = []

    if X < 10:
        N = X
        M = X * D
        if M > D:
            M = M // 10

    while X >= 9:
        digits.append(9)
        X -= 9
    if X > 0:
        digits.append(X)

    print(digits)


number()
