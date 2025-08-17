# shot_A, shot_B = map(int, input().split())
# total_alcohol_content_A = 0

# for _ in range(shot_A):
#     num_ingredient, alcohol_content = map(int, input().split())
#     total_alcohol_content_A += num_ingredient * alcohol_content
# # print(total_alcohol_content_A)

# total_alcohol_content_B = 0

# for _ in range(shot_B):
#     num_ingredient, alcohol_content = map(int, input().split())
#     total_alcohol_content_B += num_ingredient * alcohol_content
# # print(total_alcohol_content_B)

# if total_alcohol_content_A == total_alcohol_content_B:
#     print("same")
# else:
#     print("different")


def total_alcohol_content(n):
    total = 0

    for _ in range(n):
        num_ingredient, alcohol_content = map(int, input().split())
        total += num_ingredient * alcohol_content
    return total


shot_A, shot_B = map(int, input().split())

total_A = total_alcohol_content(shot_A)
total_B = total_alcohol_content(shot_B)

if total_A == total_B:
    print("same")
else:
    print("different")
