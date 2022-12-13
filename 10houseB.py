
house_count = input("Zadjete počet domů ")
floor_count = input("Zadjete počet pater ")
window_count = input("Zadjete počet oken ")
try:
    house_count = int(house_count)
    floor_count = int(floor_count)
    window_count = int(window_count)
    if house_count < 1 or window_count < 1 or floor_count < 1:
        print("hodnoty musí být větší než nula")
        exit()
except ValueError:
    print("Hodnoty musí být čísla")
    exit()


windows_int = 0
j = window_count // 2
house_int = 0
n = window_count

if window_count % 2 == 0:
    k = window_count //2 +1
    n -= 1
# střecha
while house_int < house_count:
    print((j + 1) * " " + (n + 2) * "=" + (j + 1) * " ", end=" ")
    house_int += 1
house_int = 0

print()
while windows_int < (window_count // 2 + 1):
    while house_int < house_count:
        print((j) * " " + "/" + " " + (n) * "u" + " \\" + (j) * " ", end=" ")
        house_int += 1
    j -= 1
    windows_int += 1
    n += 2

    print()




house_int = house_count -1
n = window_count
j = window_count // 2
floor_int = 0
i = -1
k=0


while i <= floor_count:
    while k < house_count:
        print(k * ("|" + window_count * " #" + " | "), end="")
        k+= 1
        if k == house_count:
            print()
            break
        print((window_count * 2 + 3) * "=", end=" ")
        print()
    i += 1

house_int =0
while house_int < house_count-1:
    print((window_count * 2 + 3) * "=", end="")
    print(" ", end="")
    house_int += 1