number1, number2 = map(int, input().split())


def which_button():
    button1 = sum(list(map(int, input().split())))
    # print(button1)

    button2 = sum(list(map(int, input().split())))
    # print(button2)

    if button1 > button2:
        print("Button 1")
    elif button1 < button2:
        print("Button 2")
    else:
        print("Oh no")


which_button()
