length_of_song = int(input())
number_of_revolution = length_of_song / 4
# print(round(number_of_revolution, 2))

# formatted_2dp = "{:.2f}".format(number_of_revolution)
# print(formatted_2dp)

formatted_two_dp = f"{number_of_revolution:.2f}"
print(formatted_two_dp)
