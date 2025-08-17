def contestant_location():
    total_contestants = int(input())
    contestants_respective_location = {}

    for _ in range(total_contestants):
        name = input()
        location = input()
        contestants_respective_location[name] = location
    return contestants_respective_location
    # print(contestants_respective_location)


contestants_respective_location = contestant_location()


def number_shirts_per_country(contestants_respective_location):
    counts_per_country = {}
    for location in contestants_respective_location.values():
        if location in counts_per_country:
            counts_per_country[location] += 1
        else:
            counts_per_country[location] = 1
    # return counts_per_country
    # print(counts_per_country)
    return dict(sorted(counts_per_country.items()))
    # print(dict(sorted(counts_per_country.items())))


for location, counts in number_shirts_per_country(
    contestants_respective_location
).items():
    print(f"{location} {counts}")

# n = number_shirts_per_country(contestants_respective_location)

# def final_output(n):
#     for location, counts in n.items():
#         print(f"{location} {counts}")
