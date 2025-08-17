def number_points():
    cards = input().upper()

    number_T = cards.count("T")
    number_C = cards.count("C")
    number_G = cards.count("G")

    one_set = min(number_T, number_C, number_G)

    total_points = (number_T**2) + (number_C**2) + (number_G**2) + (one_set * 7)

    print(total_points)


number_points()
