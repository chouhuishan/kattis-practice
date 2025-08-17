word = input()
# number_of_b = 0
# number_of_k = 0

# for character in word:
#     if character == "b":
#         number_of_b += 1
#     if character == "k":
#         number_of_k += 1

number_of_b = word.count("b")
number_of_k = word.count("k")

if number_of_b > number_of_k:
    print("boba")
elif number_of_k > number_of_b:
    print("kiki")
elif number_of_b == 0 and number_of_k == 0:
    print("none")
else:
    print("boki")
