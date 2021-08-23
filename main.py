a = [3, 6, 5, 7, 8, 2, 1]
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i - 1]:
        print(i)
