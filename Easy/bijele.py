uncorrect_list = list(map(int, input().split()))

correct_list = [1, 1, 2, 2, 2, 8]

add_or_remove = [x - y for x, y in zip(correct_list, uncorrect_list)]

print(*add_or_remove)
