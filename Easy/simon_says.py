def simon_says():
    n = int(input())

    for _ in range(n):
        s = input()
        if "Simon says" in s:
            print(s[11:])


simon_says()
