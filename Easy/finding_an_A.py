# def finding_a():
#     single_line = input()

#     for i in range(len(single_line)):
#         if single_line[i] == "a":
#             print(single_line[i:])
#             break


# finding_a()


def finding_a():
    single_line = input()
    index = single_line.find("a")

    if index != -1:
        print(single_line[index:])


finding_a()
