def num_letters():
    line = input()
    total_letters = 0

    for character in line:
        if character.isalpha():
            total_letters += 1
    print(total_letters)


num_letters()
