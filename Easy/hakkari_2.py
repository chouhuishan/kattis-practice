def form_the_mine():
    row, column = map(int, input().split())

    final_mine = []

    for _ in range(row):
        mine = input()
        final_mine.append(mine)
    # print(final_mine)
    return final_mine


mine = form_the_mine()


def mine_positions():
    mine_locations = []

    for r in range(len(mine)):
        for c in range(len(mine[0])):
            if mine[r][c] == "*":
                mine_locations.append((r + 1, c + 1))
    return mine_locations


coordinates = mine_positions()

print(len(coordinates))
for r, c in coordinates:
    print(r, c)
