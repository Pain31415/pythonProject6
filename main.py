a = int(input('Початок діапазону'))
b = int(input('Кінець діапазону'))
while число in range(початок, кінець + 1):
    if число % 7 == 0:
        print(число)