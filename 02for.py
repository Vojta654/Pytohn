numbers = [3, 5, 7, 9, 11]
i =0
while i < len(numbers):
    print("number "+ str(i+1) + " is " + str(numbers[i]))
    i +=1
k = 1
print()

indexes = [0, 1, 2, 3, 4]
for index in indexes:
    print("number " + str(index +1 ) + " is " + str(numbers[index]))
    k+=1
print()

for index in range(0,len(numbers)): #[0, 1, 2, 3, 4]
    print("number " + str(index + 1 ) + " is " + str(numbers[index]))
    k+=1

