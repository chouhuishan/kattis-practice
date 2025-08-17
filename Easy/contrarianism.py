import random
import string

input_line = input()

characters = string.ascii_letters + string.digits
length = random.randint(1, 10)
random_output = "".join(random.choices(characters.lower(), k=length))

while random_output == input_line:
    random_output = "".join(random.choices(characters.lower(), k=length))
print(random_output)
