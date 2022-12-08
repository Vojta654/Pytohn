# šifrování
# sifrovani = input("Chcete šifrovat(E), nebo dešifrovat(D)?")
sentence = input("Zadjte větu: ")
key = input("Napište klíč: ")
key_index = 0
index = 0
while index < len(sentence):
    num_znak = ord(sentence[index])

    if num_znak == 32:
        num_znak = 0  # mezera
        print(" ", end="")
        index += 1

        continue
    # print(index)
    if num_znak > 96:  # malé píseno
        num_klic = ord(key[key_index]) - 97
        if num_klic + num_znak > 122:
            print(chr(num_znak - 26 + num_klic), end="")
        else:
            print(chr(num_znak + num_klic), end="")

    if num_znak < 96:  # velké píseno
        num_klic = ord(key[key_index]) - 65
        if num_klic + num_znak > 90:
            print(chr(num_znak - 26 + num_klic), end="")
        else:
            print(chr(num_znak + num_klic), end="")
    index += 1
    key_index += 1
    if key_index == len(key):
        key_index = 0
