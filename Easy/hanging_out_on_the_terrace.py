def groups_not_allowed():
    fire_safety_limit, number_events = map(int, input().split())

    total_groups_entering_leaving = []
    current_count = 0
    groups_declined_entry = 0

    for _ in range(number_events):
        groups_enter_or_leave = input().split()
        if groups_enter_or_leave[0] == "enter":
            groups_enter_or_leave_integer = int(groups_enter_or_leave[1])
            total_groups_entering_leaving.append(groups_enter_or_leave_integer)
        else:
            groups_enter_or_leave_integer = -int(groups_enter_or_leave[1])
            total_groups_entering_leaving.append(groups_enter_or_leave_integer)
    # print(total_groups_entering_leaving)

    for i in total_groups_entering_leaving:
        if current_count + i <= fire_safety_limit:
            current_count += i
        else:
            groups_declined_entry += 1
    print(groups_declined_entry)


groups_not_allowed()
