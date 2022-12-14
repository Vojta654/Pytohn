file = open("input.txt")
content = file.read()
lines = content.splitlines()
index = 0
count = 0
maximum1 = 0
maximum2 = 0
maximum3 = 0
for line in lines:
    if line != "":
        number = int(line)
        count += number
    if line == "":
        if count > maximum1 :
            maximum3 = maximum2
            maximum2 = maximum1
            maximum1 = count
        if count < maximum1 and count >maximum2:
            maximum3 = maximum2
            maximum2 = count
        if count < maximum2 and count >maximum3:
            maximum3 = count
        count = 0

print(maximum1 + maximum2 + maximum3)
print(maximum1)
print(maximum2)
print(maximum3)

