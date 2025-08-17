n = int(input())
h = int(input())
x = int(input())
m = int(input())
y = int(input())


def duration():
    total_manhour_total_cubic_metres = n * h
    manhour_per_cubic_metres = total_manhour_total_cubic_metres / x
    total_manhour_total_cubic_metres_team_B = manhour_per_cubic_metres * y
    time_taken = total_manhour_total_cubic_metres_team_B / m
    print(time_taken)


duration()
