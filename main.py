a = int(input("Введіть початок діапазону: "))
b = int(input("Введіть кінець діапазону: "))
for number in range(a, b + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)