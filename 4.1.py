# Даны два целых числа A и B (A < B). Найти все целые числа,
# расположенные между данными числами (включая сами эти числа),
# в порядке их возрастания, а также количество N этих чисел.

A = int(input('Введите целое число: '))
B = int(input('Введите целое число, больше предыдущего: '))

list_ = range(A, B + 1)
print('Количество чисел ', len(list_))

print('Все числа, расположенные между данными числами: ')
for value in list_:
    print(value, end = ', ')


