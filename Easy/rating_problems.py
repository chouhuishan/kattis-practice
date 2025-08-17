total_judges, judges_already_rated = map(int, input().split())
total_rating = 0

for _ in range(judges_already_rated):
    rating = int(input())
    total_rating += rating
# print(total_rating)

max_rating = (total_judges - judges_already_rated) * 3
max_overall = (max_rating + total_rating) / total_judges
# print(max_overall)

min_rating = (total_judges - judges_already_rated) * -3
min_overall = (min_rating + total_rating) / total_judges
# print(min_overall)

print(min_overall, max_overall)
