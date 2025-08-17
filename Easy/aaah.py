def go_nogo_doctor():
    jon_ability = input().lower()
    doctor_requirement = input().lower()

    if len(jon_ability) < len(doctor_requirement):
        print("no")
    else:
        print("go")


go_nogo_doctor()
