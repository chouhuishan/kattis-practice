# n = int(input())
# guests = {}

# for _ in range(n):
#     name = input()
#     present_score = int(input())
#     one_line = f"{name}\t{present_score}"
#     guests[name] = present_score

# guest_most_fun_gift = max(guests, key=guests.get)
# print(guest_most_fun_gift)

n = int(input())
guests = {}

for _ in range(n):
    name, present_score = input().split()
    present_score = int(present_score)
    guests[name] = present_score

guest_most_fun_gift = max(guests, key=guests.get)
print(guest_most_fun_gift)
