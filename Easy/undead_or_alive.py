text = input()

if ":(" in text and ":)" in text:
    print("double agent")
elif ":(" in text:
    print("undead")
elif ":)" in text:
    print("alive")
else:
    print("machine")
