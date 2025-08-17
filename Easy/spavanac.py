def clock_timing():
    h, m = map(int, input().split())
    h += m // 60
    m = m % 60

    h = h % 24

    return h, m


twenty4_hours_timing = clock_timing()


def alarm_timing(twenty4_hours_timing):
    h, m = twenty4_hours_timing
    if m >= 45:
        m -= 45
    else:
        m = m + 60 - 45
        h -= 1
        if h < 0:
            h = 23
    # print(f"{h:02d}", f"{m:02d}") this format makes it 09 25 (more correct imo)
    print(h, m)  # this format makes it 9 25


alarm_timing(twenty4_hours_timing)
