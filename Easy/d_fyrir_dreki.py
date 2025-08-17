a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4 * a * c

if D > 0:
    print("2")
elif D == 0:
    print("1")
else:
    print("0")
