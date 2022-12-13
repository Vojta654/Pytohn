message = input()
index = 0
while index < len(message):
    code = ord(message[index])
    if code >= 65 and code <=90:
        print(code -64, end=" ")

    if code >= 97 and code <= 1220:
        print(code -96, end=" ")

    if code == 32:
        print(end="   ")
    index += 1
