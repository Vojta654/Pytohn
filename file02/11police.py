file = open("data/prestupky.csv")
data = file.read()
file.close()
rows = data.split("\n")
#ukol 1
print("Ukol 1")
count = len(rows)-2
print("Přestupků bylo : " + str(count)) # odečtení prvního a posledního řádku

#ukol 2
print("Ukol 2")
cityP = 0
stateP = 0
rows.pop()
for row in rows:
    line = row.split(";")

    if line[3] == "PČR":
        cityP +=1
    if line[3] == "MPP":
        stateP +=1

print("Městská policie nahlásila : "+str(cityP)+" přestupků, a to je: " + str(cityP/count *100) + " %")
print("Státní policie nahlásila : " +str(stateP)+" přestupků, a to je: " + str(stateP/count *100) + " %")

#ukol 3
print("Ukol 3")
FO = 0
PO = 0
for row in rows:
    lines = row.split(";")

    if lines[6] == "ANO":
        FO += 1
    if lines[7] == "ANO":
        PO += 1
print("Právnická osoba provozovala : " + str(PO/count*100)+ " %")
print("Fyzická osoba provozovala : " + str(FO/count*100)+ " %")

#ukol 4
print("Ukol 4a")
months = {}
for row in rows[1:]:
    lines = row.split(".")

    month = lines[1]
    if month not in months:
        months[month]= 0
    months[month] +=1

#řazení
listik = list(months.items())
for mesic in listik: # vypše měsíce s alespoň 60 00
    if int(mesic[1])> 60000:
        print(str(mesic[0])+ " : " + str(mesic[1]))
print("Ukol 4b")
i = 1
while i < len((listik)) -1: # seřad měsíce podle počtu přestupků

    j = i-1
    while j>= 0 and listik[i][1] < listik[j][1]:
        a = listik[j]
        j -= 1
    region = listik.pop(i)
    listik.insert(j + 1, region)
    i +=1
print("Seřazené měsíce od nejmenšího")
print(listik)



#ukol 5
print("Ukol 5a")
regions = {}
for row in rows[1:]:
    lines = row.split(";")

    region = lines[2].upper()
    if region not in regions:
        regions[region]= 0
    regions[region] +=1

#tříděni

listik = list(regions.items())
i = 1
print("Regiony s alespoň 40 000 přestupky")
for region in listik: # vypše region s alespoň 40 00
    if int(region[1])> 40000:
        print(str(region[0])+ " : " + str(region[1]))
print("Ukol 5b, seřazení všech regionů podle počtu přestuků sestuně")

while i < len((listik)) -1:

    j = i-1
    while j>= 0 and listik[i][1] > listik[j][1]:
        a = listik[j]
        j -= 1
    region = listik.pop(i)
    listik.insert(j + 1, region)
    i +=1

#print(region_sorted)
for region in listik:
    print(str(region[0])+ " : " + str(region[1]))

#ukol 6
print("Ukol 6, vozidlo s nejvice přesupky")

brands = {}
for row in rows[1:]:
    lines = row.split(";")

    brand = lines[5]
    if brand not in brands:
        brands[brand]= 0
    brands[brand] +=1
#print(brands)

max_brand = max(brands)
print(max_brand + " : " + str(brands[max_brand]))

#ukol 7
print("Ukol 7, státy s nejvice přesupky")

states = {}
for row in rows[1:]:
    lines = row.split(";")

    state = lines[4]
    if state not in states:
        states[state]= 0
    states[state] +=1


listik = list(states.items())

i = 1
while i < len((listik)) -1:

    j = i-1
    while j>= 0 and listik[i][1] > listik[j][1]:
        a = listik[j]
        j -= 1
    state = listik.pop(i)
    listik.insert(j + 1, state)
    i +=1
print(listik)
print(listik[0])
print(listik[1])
