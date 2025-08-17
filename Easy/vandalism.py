def incorrect():
    incorrect_set = set(input().upper())
    correct = "UAPC"
    result = []

    for character in correct:
        if character not in incorrect_set:
            result.append(character)

    print("".join(result))


incorrect()
