while True:

    print("When were you born?")
    year = int(input())
    age = 2022-int(year)
    if age < -1:
        print("you are from future")
    elif age<15:
        print("you are child")
    elif age<18:
        print("you are junior")
    elif age<27:
        print("you are student")
    elif age<65:
        print("you are adult")
    elif age < 100:
        print("you are senior")
    else:
        print("you are old")
