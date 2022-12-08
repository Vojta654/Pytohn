while True:  # konto
    sifrovani = input("Chcete šifrovat(E), nebo dešifrovat(D)?")
    if sifrovani == "E" or sifrovani == "D":
        break

sentence = input("Zadjte větu: ")


while True:
    key = input("Napište klíč: ")
    key_index = 0
    while key_index < len(key):
        key_znak = ord(key[key_index])
        if key_znak < 123 and key_znak > 64:
            if key_znak > 90 and key_znak < 97:
                print("byl zadán neplatný klíč používejte pouze písemna")
                working = False
                break
            else:
                working = True
                key_index += 1
        else:
            working = False
            break
    if working == False:
        continue
    elif working == True:
        break

key_index = 0
index = 0
while index < len(sentence):
    num_znak = ord(sentence[index])

    if num_znak == 32:
        num_znak = 0  # mezera
        print(" ", end="")
        index += 1
        continue
    num_klic = ord(key[key_index])
    if num_klic > 96 and num_klic < 123:  # převod klíče na pořadí v abecedě
        num_klic -= 97  # pro velké písmeno v klíči
    elif num_klic < 64 and num_klic > 91:
        num_klic -= 65  # pro malé písmeno v klíči

    if sifrovani == "E":  # šifrovování

        if num_znak > 96 and num_znak < 123:  # malé píseno
            if num_klic + num_znak > 122:
                print(chr(num_znak - 26 + num_klic), end="")
            else:
                print(chr(num_znak + num_klic), end="")

        if num_znak > 65 and num_znak < 91:  # velké píseno
            if num_klic + num_znak > 90:
                print(chr(num_znak - 26 + num_klic), end="")
            else:
                print(chr(num_znak + num_klic), end="")
        if num_znak < 65 or num_znak > 122:  # není písmeno
            print(sentence[index], end="")
            index += 1
            continue
        if num_znak > 90 and num_znak < 97:  # není písmeno
            print(sentence[index], end="")
            index += 1
            continue

    if sifrovani == "D":  # dešifrovování

        if num_znak > 96 and num_znak < 123:  # malé píseno
            if num_znak - num_klic < 97:
                print(chr(num_znak + 26 - num_klic), end="")
            else:
                print(chr(num_znak - num_klic), end="")

        if num_znak > 65 and num_znak < 91:  # velké píseno
            if num_znak - num_klic < 65:
                print(chr(num_znak + 26 - num_klic), end="")
            else:
                print(chr(num_znak - num_klic), end="")

        if num_znak < 65 or num_znak > 122:  # není písmeno
            print(sentence[index], end="")
            index += 1
            continue
        if num_znak > 90 and num_znak < 97:  # není písmeno
            print(sentence[index], end="")
            index += 1
            continue
    index += 1
    key_index += 1
    if key_index == len(key):  # když klíč dojde do konce
        key_index = 0
