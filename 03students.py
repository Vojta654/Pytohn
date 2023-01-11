print("? for help")
names = []
heights = []

while True:
    command = input("> ")
    if command == "a":
        name = input("name: ")
        height = int(input("height: "))
        if height > 0:
            heights.append(height)
            names.append(name)
    if command == "d":
        name = input("name :")
        try:
            names.remove(name)

        except ValueError:
            print("Student not found")
    if command == "l":
        print(names)
        print(heights)
        for index in range(0, len(names)):
            print(names[index] + " měří "+ str(heights[index]))

    if command == "max":
        maximum = heights[0]
        order = 0
        for ind in range(0, len(heights)):
            if maximum < heights[ind]:
                maximum = heights[ind]
                order = ind


        print( "Nejvyšší je " + names[order] +" a má "+str(maximum) + " cm")

    if command == "min":
        minimum = heights[0]
        for height in heights:
            if height < minimum:
                minimum = height
            print(str(minimum) + "cm")
        ...
    if command == "q":
        ...
    if command =="?":
        print("a = add new student")
        print("d = delete student")
        print("l = list student")
        print("end = exi program")
    if command == "end":
        exit()