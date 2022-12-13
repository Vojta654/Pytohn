# šifrování
sifrovani = input("Chcete šifrovat(E), nebo dešifrovat(D)?")
sentence = input("Zadjte větu ")



while True:
    try:
        key = int(input("Napište klíč"))
        if key > 0 and key <= 25:
            break

    except ValueError:
        continue
if sifrovani == "E":
    key2 = + key
    abeceda = -26
else:
    key2 = - key
    abeceda = 26

index = 0
while index < len(sentence):
    num_znak = ord(sentence[index])
    if num_znak == 32:
        print(" ", end="")
        index +=1
        continue
    if sifrovani == "E":
        if num_znak < 96:       # je to velké píemno
            if (key + num_znak) > 90:
                print(chr(num_znak + abeceda + key2), end="")
            else:
                print(chr(num_znak + key2), end="")

        if num_znak > 96:        # je to malé písmeno
            if (key + num_znak) > 122:
                print(chr(num_znak + abeceda + key2), end="")
            else:
                print(chr(num_znak + key2), end="")


        # teď posunutí a převés zpět na znak
        # šifrivání +klíč -abeceda
        # dešifrování -klíč + abeceda


    if sifrovani == "D":
        if num_znak < 96:  # je to velké píemno
            if (num_znak - key) < 65:
                print(chr(num_znak + abeceda + key2), end="")
            else:
                print(chr(num_znak + key2), end="")

        if num_znak > 96:  # je to malé písmeno
            if (num_znak - key) <97:
                print(chr(num_znak + abeceda + key2), end="")
            else:
                print(chr(num_znak + key2), end="")

        # teď posunutí a převés zpět na znak
        # šifrivání +klíč -abeceda
        # dešifrování -klíč + abeceda

    index += 1