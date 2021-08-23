import random
n = int(input("Введите размер списка:"))
mas = []
for i in range(n):
    k = random.randint(0, 99)
    mas.append(k)

print("Элементы списка: ", mas)
for i in range(n):
    if (i % 7) == 0:
        mas.pop(i)
print("Элементы списка кратных на 7: ", mas)