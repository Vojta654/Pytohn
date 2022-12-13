pocet = 0
i = 1
souZnam = 0
souVah = 0
j = 0
while True:
    pocet = input("Kolik máš známek? ")
    try:
        pocet = int(pocet)

        if pocet > 0:
            break
    except ValueError:
        continue


while i <= pocet:
    try:
        znamka = int(input("Zadej " + str(i) + ". známku: "))

    except ValueError:
        continue

    if znamka < 0 or znamka > 5:
        continue

    while True:
        vaha = input("Zadej váhu " + str(i) + ". známky: ")
        try:
            vaha = int(vaha)

        except ValueError:
            continue

        if vaha > 0 and vaha <= 3:
            break
    souZnam += vaha * znamka
    souVah += vaha
    i += 1
vysZnam = souZnam/souVah
print("Vechny znamky zadany")
print("Vážený průměr: " + str(round(vysZnam, 2)))
print("Známka na vysvědčení: " + str(round(vysZnam)))





while True:
    NovaVaha = int(input("Zadejte váhu příští známky: "))
    try:
        NovaVaha = int(NovaVaha)

        if NovaVaha <= 3:
            break
    except ValueError:
        continue

souVah += NovaVaha
while j <= 5:
    x = j*NovaVaha + souZnam
    print("Pro znamku " + str(j) + " je průměr: " + str(round(x/souVah, 2)))
    j += 1
