C = float(input())
L = int(input())
total_cost = []

for _ in range(L):
    width, length = map(float, input().split())
    cost = width * length
    total_cost.append(cost)
sum_total_cost = C * sum(total_cost)
sum_total_cost_8dp = f"{sum_total_cost:.8f}"

print(sum_total_cost_8dp)
