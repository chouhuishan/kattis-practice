current_wind_speed = int(input())
number_of_roads = int(input())
data = {}

for _ in range(number_of_roads):
    road_name, max_wind_speed = input().split()
    max_wind_speed = int(max_wind_speed)
    data[road_name] = max_wind_speed

for key, value in data.items():
    road_name = key
    max_wind_speed = value

    if current_wind_speed <= value:
        print(f"{key} opin")
    else:
        print(f"{key} lokud")
