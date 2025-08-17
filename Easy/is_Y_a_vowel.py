s = input()
total = 0
total_y = 0

for character in s:
    if character.lower() in "aeiou":
        total += 1

for character in s:
    if character.lower() in "aeiouy":
        total_y += 1

print(total, total_y)
