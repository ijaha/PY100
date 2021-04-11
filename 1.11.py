# Записать условие, которое является истинным, когда только одно из чисел А и В четное.

a = float(input('Введите число A: '))
b = float(input('Введите число B: '))

if a % 2 == 0 and b % 2 != 0:
    print('True')
elif b % 2 == 0 and a % 2 != 0:
    print('True')
else:
    print('False')
