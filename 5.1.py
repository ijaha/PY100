# Гипотеза Сиракуз гласит, что любое натуральное число сводимо к единице при следующих действиях над ним:
# а) если число четное, то разделить его пополам,
# б) если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
#
# Над вновь полученным числом вновь повторить действия a) или б) в зависимости от его четности.
# Рано или поздно число станет равным 1.

a = int(input('Введите натуральное число: '))

while a != 1:
    a = a / (a / 2)
    print(a)