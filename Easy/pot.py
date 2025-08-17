def original_input():
    n = int(input())

    numbers = []

    for _ in range(n):
        wrong_number = int(input())
        exponentiation = wrong_number % 10
        # print(exponentiation)
        original_number = wrong_number // 10
        # print(original_number)

        correct_number = original_number**exponentiation

        numbers.append(correct_number)
    print(sum(numbers))


original_input()


# wrong_number = int(input())
# exponentiation = wrong_number % 10
# original_number = wrong_number // 10

# print(exponentiation)
# print(original_number)
