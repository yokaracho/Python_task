a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = int(input("Введите число c:"))

if (a and b and c) != 0:
    sredne_geom = (a * b * c) ** (1 / 3)
    print("Среднее геометрическое: " + str(sredne_geom))
else:
    srednee_arifmeticheskoe = (a + b + c) / 3
    print("Среднее арифметическое : " + str(srednee_arifmeticheskoe))