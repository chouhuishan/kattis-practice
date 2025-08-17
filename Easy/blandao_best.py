n = int(input())
meat_list = []

for _ in range(n):
    meat_types = input()
    meat_list.append(meat_types)

if len(meat_list) == 1:
    print(meat_list[0])
else:
    print("blandad best")

# n = int(input())
# meat_list = set()

# for _ in range(n):
#     meat_types = input()
#     meat_list.add(meat_types)

# if len(meat_list) == 1:
#     print(next(iter(meat_list)))
# else:
#     print("blandad best")
