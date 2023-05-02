datum = 230502 #YYMMDD

#typ vstupenky
while True:
    typ_vstupenek = input("jake vstupenky chcete koupit? (D/R)  ")
    
    if typ_vstupenek == "D" or typ_vstupenek =="R":
        break
    else:
        print("špatné zadnání")
        
#počet lidí

while True:
    peope_num = input("Kolik lidí?  ")
    try:
        peope_num = int(peope_num)
        
    except ValueError:
        print("Nebylo zadáno číslo!!")
        continue
        
    if peope_num > 0:
        break
    else:
        print("Počet lidí nemůže být záporný")

#věk+ napsání ceny
ages = []
people_prizes = [] #pole s postupně cenami vstupenek
people_codes = [] #pole s postupně kody vstupenek
prizes = [150, 300, 200, 600, 1800, 900]
codes = [24, 11, 22, 44, 33, 42]
final_price = 0
for customer in range(1, peope_num +1):
    while True:
        people_age = input("Kolik let je "+ str(customer) + ". osobě?  ")
        try:
            people_age = int(people_age)
            
        except ValueError:
            print("Nebylo zadáno číslo!!")
            continue
            
        if people_age > 0:
            break
        else:
            print("Věk nemůže být záporný")
    ages.append(people_age)
    if typ_vstupenek =="R":
        index =3
    else:
        index = 0
    
    if people_age >= 65:
        final_price += prizes[index]
        people_prizes.append(prizes[index])
        people_codes.append(codes[index])
        print("Kategorie: důchodce")
        print("Cena: 150")
    elif people_age >15 and people_age < 65:
        final_price += prizes[index+1]
        people_prizes.append(prizes[index+1])
        people_codes.append(codes[index+1])
        print("Kategorie: dospělí")
        print("Cena: 300")
    elif people_age>= 3 and people_age <= 15:
        final_price +=prizes[index+2]
        people_prizes.append(prizes[index+2])
        people_codes.append(codes[index+2])
        print("Kategorie: dítě")
        print("Cena: 200")


print("Celková cena je: " + str(final_price)  + " Kč")

#platba
money_recieved = 0
money_bills = [10, 20, 50, 100, 200, 500, 1000]
print("teď zaplať pomocí bankovek, 10 Kč, 20 Kč, 50 Kč, 100 Kč, 200 Kč, 500 Kč, 1000 Kč")
while money_recieved < final_price:
    
    print("Ještě chybí: "+ str(final_price-money_recieved)+ " Kč")
    money = input("Vlože bankvku:  ")
    try:
        money = int(money)
    except ValueError:
        continue
    if money not in money_bills:
        print("Zadána špatná bankva")
        print("Zaplať pomocí bankovek, 10 Kč, 20 Kč, 50 Kč, 100 Kč, 200 Kč, 500 Kč, 1000 Kč")
    else:
        money_recieved += money
        
#vracení peněz
returnuju_text = "Vracené peníze: "
if money_recieved > final_price:
    print("Nyní proběhne vrácení peněz")
    give_back = money_recieved - final_price
    while give_back >0:
        if give_back/500>= 1:
            returnuju_text += "500 Kč, "
            give_back -= 500
        if give_back/200>= 1:
            returnuju_text += "200 Kč, "
        if give_back/100>= 1:
            give_back -= 200
            returnuju_text += "100 Kč, "
        if give_back/100>= 1:
            give_back -= 100
        if give_back/50>= 1: 
            returnuju_text += "50 Kč, "
            give_back -= 50
            
print(returnuju_text)# text, který zobrazí co vše bylo vráceno


#tisk vstupenek
print("\u0332".join("TISK VSTUPENEK"))
for index in range(0, peope_num):
    
    #ciferný součet a dopočítání čísla aby součet byl děl 10
    sum = 0
    for digit in str(datum + index + 1 + people_codes[index]):
        sum += int(digit)
    y = 10-sum%10    
    
    if people_prizes[index] == 200:
        kategorie = "| 1 DÍTĚ        |"
    if people_prizes[index] == 300:
        kategorie = "| 1 DOSPĚLÝ     |"
    if people_prizes[index] == 150:
        kategorie = "| 1 DŮCHODCI    |"
        
    ticket_num = str(datum) + str(people_codes[index]) +  (4- len(str(index+1))) * "0" + str(index+1) + str(y)
    print(17* "=")
    print("| ZOO Praha     |")
    print(kategorie)
    print("| " + ticket_num + " |")
    print(17* "=")
