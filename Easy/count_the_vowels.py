s = input()

vowels = 0

# for character in s:
#     if character == "a" or character == "A":
#         vowels += 1
#     elif character == "e" or character == "E":
#         vowels += 1
#     elif character == "i" or character == "I":
#         vowels += 1
#     elif character == "o" or character == "O":
#         vowels += 1
#     elif character == "u" or character == "U":
#         vowels += 1
# print(vowels)

for character in s:
    if character.lower() in "aeiou":
        vowels += 1
print(vowels)
