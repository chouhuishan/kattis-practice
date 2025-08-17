n = int(input())
number_friends = []

for _ in range(n):
    age = int(input())
    number_friends.append(age)
    youngest = min(number_friends)
print(youngest)
