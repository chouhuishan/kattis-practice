W = int(input())
N = int(input())
total_area = 0

for _ in range(N):
    width, length = map(int, input().split())
    total_area += width * length

print(total_area // W)
