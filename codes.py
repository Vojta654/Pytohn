sentence = input("Napište větu: ")

while True:
    try:
        key = int(input("Napište klíč "))
        if key >= 0 and key <= 25:
            break
    except ValueError:
        continue


letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

letters_num = [
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
]

index = 0
letter_index = 0
while letter_index < len(sentence):
    index = 0
    num_znak = ord(sentence[letter_index])
    if num_znak < 96:
        num_znak += 32
        up = 1
    else:
        up = 0
    while index < len(letters):
        if num_znak == 64:
            print(" ", end="")
            break
        if num_znak == letters_num[index]:
            # num_znak = 97 + index
            if key + num_znak > 122:
                if up == 1:
                    print(
                        (chr(num_znak - 26 + key)).upper(),
                        end="",
                    )
                else:
                    print(
                        chr(num_znak - 26 + key),
                        end="",
                    )
            else:
                if up == 1:
                    print((chr(num_znak + key)).upper(), end="")
                else:
                    print(chr(num_znak + key), end="")
        index += 1
    letter_index += 1
