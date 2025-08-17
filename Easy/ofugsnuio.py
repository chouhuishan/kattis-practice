n = int(input())
list_of_integer = []

for _ in range(n):
    number = int(input())
    list_of_integer.append(number)
print(*list_of_integer[::-1])

# for number in reversed(list_of_integer):
#     print(number)
