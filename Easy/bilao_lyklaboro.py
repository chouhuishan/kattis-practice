from collections import OrderedDict


def string_without_duplicates():
    s = input()

    word_without_duplicates = []

    for word in s.split():
        without_deuplicates = "".join(OrderedDict.fromkeys(word))
        word_without_duplicates.append(without_deuplicates)

    final_output = " ".join(word_without_duplicates)

    print(final_output)


string_without_duplicates()
