a = int(input('Введите целое положительное число: '))

max_a = a % 10

while a >= 1:
    a = a // 10
    if a % 10 > max_a:
        max_a = a % 10
    elif a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max_a)
        break
