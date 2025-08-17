number_of_rods = int(input())
rods = []

for _ in range(number_of_rods):
    length_of_rods = int(input())
    rods.append(length_of_rods)

final_sum = sum(rods) - (number_of_rods - 1)
print(final_sum)

# sum_two_pairs_list = []
# for i in range(0, len(rods), 2):
#     addition_two_pairs = rods[i] + rods[i + 1] - 1
#     sum_two_pairs_list.append(addition_two_pairs)
# print(sum_two_pairs_list)

# final_sum = sum(sum_two_pairs_list) - 1
# print(final_sum)
