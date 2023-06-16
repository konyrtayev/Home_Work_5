number = int(input("Введите число: "))
extent = int(input("Введите степень: "))

def pow(number, extent):
    if (extent == 1):
        return (number)
    if (extent != 1):
        return ( number * pow(number, extent - 1))
print('Число =',number, 'Степень числа =',extent, "->", pow(number, extent))