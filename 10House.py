
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
    house_int = 0

i = 0

# dům
while house_int < house_count:
    print((window_count * 2 + 3) * "=", end="")
    print(" ", end="")
    house_int += 1

print()
house_int = 0
floor_int = 0
while floor_int < floor_count:
    print(house_count*("|" + window_count * " #" + " | "))
    floor_int +=1

house_int = 0

while house_int < house_count:
    print((window_count * 2 + 3) * "=", end="")
    print(" ", end="")
    house_int += 1