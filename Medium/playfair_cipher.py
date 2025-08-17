import string
from collections import OrderedDict
from pprint import pprint

keyphrase = input().upper()
keyphrase = "".join(OrderedDict.fromkeys(keyphrase))


def alphabets_to_be_in_matrix():
    result = []
    for character in keyphrase:
        if character != " ":
            result.append(character.upper())

    alphabets = string.ascii_uppercase

    for character in alphabets:
        if character == "Q":
            continue
        else:
            result.append(character)
    #     # print(result)
    #     # print(len(result))

    remaining_alphabets = list(OrderedDict.fromkeys(result))

    return remaining_alphabets


# print(alphabets_to_be_in_matrix())
# print(len(alphabets_to_be_in_matrix()))

alphabets = alphabets_to_be_in_matrix()

# pprint(alphabets)


def matrix(alphabets):
    output = []
    row = []
    for i in range(len(alphabets)):
        if (i + 1) % 5 == 0:
            row.append(alphabets[i])
            output.append(row)
            row = []
        else:
            row.append(alphabets[i])
    return output


# pprint(matrix(alphabets))


def plain_text_without_spaces():
    plain_text = input().upper()
    plain_text_final_no_space = ""

    for character in plain_text:
        if character.isalpha():
            plain_text_final_no_space += character
    return plain_text_final_no_space


def two_letters():
    final_plain_text = plain_text_without_spaces()
    list_two_letters = []

    for i in range(len(final_plain_text) - 1):
        two_letters = final_plain_text[i : i + 2]
        list_two_letters.append(two_letters)
    return list_two_letters
    # print(len(list_two_letters))
    # print(list_two_letters[0][1])

paired_alphabets = two_letters()

def final_matrix(paired_alphabets, alphabets)
    for i in range(len(paired_alphabets)):
        one_pair = paired_alphabets[i]
        
