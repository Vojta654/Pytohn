import math

print("? for help")
names = ["Vojta", "David", "Dan", "Kryšto", "Tob"]
heights = [180, 180, 130, 179, 200]

while True:
    command = input("> ")
    if command == "a":
        name = input("name: ")
        height = int(input("height: "))
        if height > 0:
            heights.append(height)
            names.append(name)
    if command == "d":
        try:
            delete_name = input("name :")
            index = names.index(delete_name)
            names.pop(index)
            heights.pop(index)
            print("The student was deleted")
        except ValueError:
            print("Error 404")

    if command == "find":
        name = input("name: ")
        for i in range(0, len(names)):
            if names[i]== name:
                print("The student was found")

    if command == "l":
        # print(names)
        # print(heights)
        for index in range(0, len(names)):
            print(names[index] + " \t" + " měří " + str(heights[index]) + " cm")

    if command == "max":
        maximum = 0
        text = None
        for ind, height in enumerate(heights):
            if maximum < height:
                maximum = height
                text = names[ind] + " - " + str(maximum) + " cm"

            elif maximum == height:
                text += " ," + names[ind] + " - " + str(maximum) + " cm "

        print("Nejvyšší je " + text + ".")

    if command == "min":
        minimun = heights[0] + 1
        text = None
        for ind, height in enumerate(heights):
            if height < minimun:
                minimun = height
                text = names[ind] + " - " + str(minimun) + " cm"

            elif minimun == height:
                text += " ," + names[ind] + " - " + str(minimun) + " cm "

        print("Nejnižší je " + text + ".")
    if command == "avg":
        soucet_height = 0
        for height in heights:
            soucet_height += height
        avg = round(soucet_height / len(heights), 1)
        print("Průměr je: " + str(avg) + " cm")
    if command == "var":
        soucet_height = 0
        for height in heights:
            soucet_height += height
        avg = soucet_height / len(heights)
        odchylka = 0
        for height in heights:
            odchylka += (height - avg) ** 2
        var = round(math.sqrt(odchylka / len(heights)), 2)
        rozptyl = round(odchylka / len(heights), 2)
        print("Rozptyl je: " + str(rozptyl))
        print("Směrodatná odchylka je " + str(var))

    if command == "?":
        print("a = add new student")
        print("d = delete student")
        print("l = list student")
        print("end = exi program")
        print("max = print maximum height")
        print("min = print minimum height")
        print("avg = print average height")
    if command == "end":
        exit()
