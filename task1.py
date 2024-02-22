n = int(input("Введите значение интервала n="))
m = int(input("Введите значение интервала m="))
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()