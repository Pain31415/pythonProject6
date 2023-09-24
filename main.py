a = int(input("Введіть початок діапазону: "))
b = int(input("Введіть кінець діапазону: "))
sum = 0
number_of_numbers = 0
for number in range(a, b + 1):
    sum += number
    number_of_numbers += 1
average = sum / number_of_numbers
print("Сума чисел у діапазоні:", sum)
print("Середнє арифметичне:", average)
