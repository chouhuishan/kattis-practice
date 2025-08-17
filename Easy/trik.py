moves = input().strip()

cups = [1, 0, 0]  # 1 represents where the ball is

for move in moves:
    if move == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif move == "B":
        cups[1], cups[2] = cups[2], cups[1]
    else:
        cups[0], cups[2] = cups[2], cups[0]
print(cups.index(1) + 1)
