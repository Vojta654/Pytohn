total = 0
count = 0
minimum = None
maximum = None
while True:
    enter = input()
    if enter == "":
        break

    try:
        number = int(enter)
    except ValueError:
        continue
    number = int(enter)
    total += number
    count += 1
    if minimum is None or number < minimum:
        minimum = number

    if maximum is None or number > maximum:
        maximum = number

print("Sum: " + str(total))
print("Count: " + str(count))
print(minimum)
print(maximum)
