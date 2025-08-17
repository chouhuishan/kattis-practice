def grid_formulation():
    row, column = map(int, input().split())

    # for _ in range(row): # causes never ending rows due to input()
    #     row_output = ""
    #     for _ in range(column):
    #         character = input()
    #         row_output += character
    #     print(row_output)

    grid = []

    for _ in range(row):
        row_output = input()
        grid.append(row_output)

    return grid


grid = grid_formulation()


def mine_position(grid):
    mine_locations = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "*":
                mine_locations.append((r + 1, c + 1))
    print(len(mine_locations))
    # print(*mine_locations)
    for r, c in mine_locations:
        print(r, c)


mine_position(grid)
