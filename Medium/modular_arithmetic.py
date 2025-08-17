def my_divide(x, y):
    return x * (y**-1)


def number():
    while True:
        n, t = map(int, input().split())
        if n == 0 and t == 0:
            return

        for _ in range(t):
            x, op, y = input().split()
            x, y = int(x), int(y)

            if op == "+":
                print((x + y) % n)
            elif op == "-":
                print((x - y) % n)
            elif op == "*":
                print((x * y) % n)
            elif op == "/":
                if y == 0:
                    print(-1)
                else:
                    try:
                        inverse = pow(y, -1, n)
                        print((x * inverse) % n)
                    except ValueError:
                        print(-1)


number()
