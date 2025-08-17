def number_turtle():
    n = int(input())

    turtles = []

    for _ in range(n):
        number_turtles = list(map(int, input().split()))
        number_turtles = number_turtles[:-1]
        turtles.append(number_turtles)
    return turtles
    # print(turtles)


# number_turtle()

total_number_turtles = number_turtle()


def number_imports(total_number_turtles):
    for i in range(len(total_number_turtles)):
        number_of_imported_turtles = 0
        for j in range(len(total_number_turtles[i]) - 1):
            last_year = total_number_turtles[i][j]
            current_year = total_number_turtles[i][j + 1]

            if current_year <= last_year * 2:
                number_of_imported_turtles += 0
            elif current_year > last_year * 2:
                number_of_imported_turtles += current_year - last_year * 2
        print(number_of_imported_turtles)


number_imports(total_number_turtles)
