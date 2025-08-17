def sum_problem():
    single_integer_P = int(input())

    for _ in range(single_integer_P):
        data_set_number_K, N = map(int, input().split())

        s1 = N * (N + 1) // 2
        s2 = N**2
        s3 = N * (N + 1)

        print(data_set_number_K, s1, s2, s3)

    # positive_integer = []
    # odd_integer = []
    # even_integer = []

    # for i in range(integer_N + 1):
    #     positive_integer.append(i)

    # for i in range(integer_N * 2 + 1):
    #     if i % 2 != 0:
    #         odd_integer.append(i)
    #     else:
    #         even_integer.append(i)

    # s1 = sum(positive_integer)
    # s2 = sum(odd_integer)
    # s3 = sum(even_integer)

    # print(data_set_number_K, s1, s2, s3)


sum_problem()
