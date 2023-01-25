names = [50, 48, 49]
count = 0
for j in range(0, len(names) - 1):
    m = j
    for i in range(j+1, len(names)):
        if names[i] < names[m]:
            m = i
    #t = numbers[m]
    #numbers[m] = numbers[j]
    #numbers[j] = t
    names[m], names[j] = names[j], names[m]


print(names)
print(count)