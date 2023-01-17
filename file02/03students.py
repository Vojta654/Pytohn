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
            print("Student deleted")

        except ValueError:
            print("Student not found")
    if command == "l":
        # print(names)
        # print(heights)
        for index in range(0, len(names)):
            print(names[index] + " měří " + str(heights[index]) + " cm")

    if command == "max":
        maximum = 0
        for ind, height in enumerate(heights):
            if maximum < height:
                maximum = height
                text = names[ind] + " - " + str(maximum) + " cm"

            elif maximum == height:
                text += " ," + names[ind] + " - " + str(maximum) + " cm "

        print("Nejvyšší je " + text + ".")

    if command == "min":
        minimun = heights[0] + 1
        text = ""
        for ind, height in enumerate(heights):
            if height < minimun:
                minimun = height
                text = names[ind] + " - " + str(minimun) + " cm"

            elif minimun == height:
                text += " ," + names[ind] + " - " + str(minimun) + " cm "

        print("Nejnižší je " + text + ".")
    if command == "q":
        ...
    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list student")
        print("end = exi program")
        print("max = print maximum height")
        print("min = print minimum height")
    if command == "end":
        exit()
