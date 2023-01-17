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
        delete_name = input("name :")
        try:
            for ind, name in enumerate(names):
                if name == delete_name:
                    names.remove(name)
                    heights.pop(ind)
                    # break

        except ValueError:
            print("Student not found")
    if command == "l":
        print(names)
        print(heights)
        for index in range(0, len(names)):
            print(names[index] + " měří " + str(heights[index]))
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list student")
        print("end = exi program")
        print("max = print maximum height")
        print("min = print minimum height")
    if command == "end":
        exit()

    if command == "min":
        minimum = heights[0]
        for height in heights:
            if height < minimum:
                minimum = height
            print(str(minimum) + "cm")
        ...
