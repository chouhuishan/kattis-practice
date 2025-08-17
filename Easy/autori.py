name = input().split("-")
initials = []

for word in name:
    letter = word[0].upper()
    initials.append(letter)

result = "".join(initials)
print(result)
