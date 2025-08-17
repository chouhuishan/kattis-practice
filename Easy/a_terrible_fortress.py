length_of_hallway = int(input())
list_blazers = []

for _ in range(length_of_hallway):
    number_of_blazers = int(input())
    list_blazers.append(number_of_blazers)
    total_blazers = sum(list_blazers)
print(total_blazers)
