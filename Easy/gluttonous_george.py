line = input().split()
n = int(line[0])
m = int(line[2])

if n == m:
    print("Goggi svangur!")
elif n < m:
    print("<")
else:
    print(">")
