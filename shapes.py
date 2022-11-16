while True:
    house_count = input("Zadjete počet domů ")
    floor_count = input("Zadjete počet pater ")
    window_count = input("Zadjete počet oken ")

    if not house_count or not floor_count:
        print("hodnoty musí být větší než nula")
        exit()
    try:
        house_count = int(house_count)    
        floor_count = int(floor_count)
        window_count = int(window_count)
        break
    except:
        print("Hodnoty musí být čísla")
        exit()


M =0
i = window_count//2
j = window_count //2 
k = 0
n = window_count
if window_count%2 == 0:
    n -=1 
    
while k < house_count:
    print((j+1) * " " + (n+2)*"=" + (j+1)*" ", end=" " )
    k += 1
k=0

print()
while M < (window_count//2 +1 ):
    while k < house_count:
        print((j) * " "+ "/" + " " + (n) * "u"  +  " \\" + (j)*" ", end=" ")
        k +=1
    i += 1
    j -= 1
    M += 1
    n +=2
        
    print()
    k =0

i =0
j =0

while k < house_count:
    print((window_count*2+3) * "=", end="")
    print(" ", end="")
    k += 1

print()

k =0

while j < floor_count:
    
    k = 0
    while k < house_count:
        print("|", end="")
        while i < window_count:
            print(" #", end="")
            i += 1
        print(" | ", end="")
        i = 0
        k += 1
    j += 1
    print()
k = 0

while k < house_count:
    print((window_count*2+3) * "=", end="")
    print(" ", end="")
    k += 1