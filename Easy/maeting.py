mon_class, tues_class = map(int, input().split())
attendance_mon = list(map(int, input().split()))
attendance_tues = list(map(int, input().split()))

common_attendance = []

for i in attendance_mon:
    if i in attendance_tues:
        common_attendance.append(i)

print(*common_attendance)
