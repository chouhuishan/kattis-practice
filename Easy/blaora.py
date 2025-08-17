v, a, t = map(int, input().split())

d = (v * t) + (0.5 * a * t**2)
formatted_9dp = f"{d:.9f}"
print(formatted_9dp)

# print(round(d, 9))

# formatted_9dp = "{:.2f}".format(d)
# print(formatted_9dp)
