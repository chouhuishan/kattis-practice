N = int(input())
QALY = []

for _ in range(N):
    q, y = map(float, input().split())
    QOL_years = q * y
    QALY.append(QOL_years)
res = sum(QALY)

res_3dp = f"{res:.3f}"  # use f string when want to show exactly 3dp
print(res_3dp)

# res_3dp = round(res, 3)
# print(res_3dp)
# use round() for numeric rounding, not for formatted output
