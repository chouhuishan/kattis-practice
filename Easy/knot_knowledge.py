n = int(input())

knots_to_learn = list(map(int, input().split()))
knots_learned = list(map(int, input().split()))

remaining_knot = sum(knots_to_learn) - sum(knots_learned)
print(remaining_knot)
