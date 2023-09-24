symbol = input("Введіть символ для заповнення лінії: ")
length = int(input("Введіть довжину лінії: "))
if length < 1:
    print("Довжина лінії повинна бути більше або дорівнювати 1.")
else:
    line = symbol * length
    print(line)
