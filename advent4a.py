file = open("input4.txt")
content = file.read()
lines = content.splitlines()

number1 = 0
index = 0
for line in lines:
    index = 0
    number1 = int(line[index])
    index +=1
    if line[index] != "-" and line[index] != ",": #  pokud je to číslo
        number1 = number1 * 10 + int(line[index])
        index +=1
    else:
        index +=1

    number2 = int(line[index])
    index +=1
    if line[index] != "-" and line[index] != ",": #  pokud je to číslo
        number2 = number2 * 10 + int(line[index])
    else:
        index +=1

    number3 = int(line[index])
    index += 1
    if line[index] != "-" and line[index] != ",":  # pokud je to číslo
        number3 = number3 * 10 + int(line[index])
    else:
        index += 1

    number4 = int(line[index])
    index += 1
    if line[index] != "-" and line[index] != ",":  # pokud je to číslo
        number4 = number4 * 10 + int(line[index])
    else:
        index += 1

    index = 0

print(number1)
print(number2)
print(number3)
print(number4)