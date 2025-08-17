n = int(input())
binary_n = bin(n)[2:]
reverse_binary_n = str(binary_n)[::-1]
reverse_binary_n_base10 = int(reverse_binary_n, 2)
print(reverse_binary_n_base10)
