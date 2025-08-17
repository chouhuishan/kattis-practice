number_classroom, number_sanitizer_available = map(int, input().split())
# list_sanitizer = []

# for _ in range(number_classroom):
#     sanitizer_given_per_classroom = int(input())
#     list_sanitizer.append(sanitizer_given_per_classroom)
#     # total_sanitizer = sum(list_sanitizer) do not put this inside the loop, it will increase the overall running time

# total_sanitizer = sum(list_sanitizer)

# if total_sanitizer <= number_sanitizer_available:
#     print("Jebb")
# else:
#     print("Neibb")

total_sanitizer = 0

for sanitizer in range(number_classroom):
    sanitizer_given_per_classroom = int(input())
    total_sanitizer += sanitizer_given_per_classroom

if total_sanitizer <= number_sanitizer_available:
    print("Jebb")
else:
    print("Neibb")
