import random
n = int(input("Введите размер списка:"))
mas = []
for i in range(n):
    k = random.randint(-10, 10)
    mas.append(k)
print("Элементы списка: ", mas)
summa = 0
for i in range(n):
    if mas[i] < 0:
        summa += mas[i]
print("Сумма отрицательных элементов списка: ", summa)