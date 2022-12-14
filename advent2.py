file = open("input2.txt")
content = file.read()
lines = content.splitlines()

points = 0
for line in lines:
    if line[2] == "X":
        points += 1
        if line[0] == "A":
            points +=3
        if line[0] == "B":
            points +=6
        if line[0] == "C":
            points +=0
    if line[2] == "Y":
        points += 2
        if line[0] == "A":
            points +=0
        if line[0] == "B":
            points +=3
        if line[0] == "C":
            points +=6
    if line[2] == "Z":
        points += 3
        if line[0] == "A":
            points +=6
        if line[0] == "B":
            points +=0
        if line[0] == "C":
            points +=3

print(points)