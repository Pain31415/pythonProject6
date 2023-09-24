begin = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
number_of_multiples_7 = 0
print("1. Всі числа діапазону:")
for number in range(begin, end + 1):
    print(number)
print("\n2. Всі числа діапазону в спадному порядку:")
for number in range(end, begin - 1, -1):
    print(number)
print("\n3. Всі числа, кратні 7:")
for number in range(begin, end + 1):
    if number % 7 == 0:
        print(number)
number_of_multiples_5 = sum(1 for number in range(begin, end + 1) if number % 5 == 0)
print("\n4. Кількість чисел, кратних 5:", number_of_multiples_5)