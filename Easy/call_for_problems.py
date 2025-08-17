number_candiates = int(input())
odd_numbers = 0

for _ in range(number_candiates):
    difficulty_rating = int(input())
    if difficulty_rating % 2 != 0:
        odd_numbers += 1

print(odd_numbers)

# number_candiates = int(input())
# total_difficulty_rating = []
# odd_numbers = 0

# for _ in range(number_candiates):
#     difficulty_rating = int(input())
#     total_difficulty_rating.append(difficulty_rating)

# for i in range(len(total_difficulty_rating)):
#     if total_difficulty_rating[i] % 2 != 0:
#         odd_numbers += 1
# print(odd_numbers)
