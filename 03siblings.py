print("Jak se jmenuješ?")
jm = input()
print("Kolik ti je let?")
vek = int(input())
print("Máš nějakého sourozence?")
sou = input()
print("Jak se jmenu je?")
jmS = input()
if sou == "ANO" or sou == "ano":
    print("Kolik mu je let?")
    vekS = int(input())
    x = abs(vek-vekS)
    if vek>vekS:
        if x == 1:
            print("Takže"+jmS+" je o " + str(x) + " rok mladší než "+jm+".")
        elif x < 5:
            print("Takže "+jmS+"je o " + str(x) + " roky mladší než "+jm+".")
        else:
            print("Takže "+jmS+"je o " + str(x) + " let mladší než "+jm+".")
    elif vek<vekS:
        if x == 1:
            print("Takže "+jmS+"je o " + str(x) + " rok starší než "+jm+".")
        elif x < 5:
            print("Takže "+jmS+"je o " + str(x) + " roky starší než "+jm+".")
        else:
            print("Takže "+jmS+"je o " + str(x) + " let starší než "+jm+".")
    else:
        print("Takže jste stejně staří - nejste náhodou dvojčata?")
elif sou == "NE" or sou == "ne":
    print("Takže jsi jedináček.")
else:
    print("zadaná špatná hodnota, zadávejte: ANO nebo NE")