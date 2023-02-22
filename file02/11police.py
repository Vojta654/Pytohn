file = open("data/prestupky.csv")
data = file.read()
file.close()
rows = data.split("\n")
#ukol 1
count = len(rows)-2
print("Přestupků bylo : " + str(count)) # odečtení prvního a posledního řádku

#ukol 2
cityP = 0
stateP = 0
rows.pop()
for row in rows:
    line = row.split(";")

    if line[3] == "PČR":
        cityP +=1
    if line[3] == "MPP":
        stateP +=1

print(cityP)
print(stateP)
print("Městská policie nahlásila : " + str(cityP/count *100) + " %")
print("Státní policie nahlásila : " + str(stateP/count *100) + " %")

#ukol 3
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
months = {}
for row in rows[1:]:
    lines = row.split(".")

    month = lines[1]
    if month not in months:
        months[month]= 0
    months[month] +=1

print(months)

#ukol 5
regions = {}
for row in rows[1:]:
    lines = row.split(";")

    region = lines[2].upper()
    if region not in regions:
        regions[region]= 0
    regions[region] +=1

print(regions)


#ukol 6
brands = {}
for row in rows[1:]:
    lines = row.split(";")

    brand = lines[5]
    if brand not in brands:
        brands[brand]= 0
    brands[brand] +=1

max = 0



print(brands)
i = 1
while i < len((regions)) -1:

    j = i-1
    while j>= 0 and regions[i][1] > regions[j][1]:
        a = regions[j]
        j -= 1
    region = regions.pop(i)
    regions.insert(j + 1, region)
    i +=1
print(regions)
