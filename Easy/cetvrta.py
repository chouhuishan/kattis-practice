a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

if a == c:
    x_coordinate = e
elif a == e:
    x_coordinate = c
else:
    x_coordinate = a

if b == d:
    y_coordinate = f
elif b == f:
    y_coordinate = d
else:
    y_coordinate = b

print(x_coordinate, y_coordinate)
