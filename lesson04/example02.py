# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random
random_1 = random.sample(range(1, 500), 30)
print(random_1)
random_2 = []
for el in range(len(random_1) - 1):
    if random_1[el] < random_1[el+1]:
        random_2 .append(random_1[el+1])
print(random_2 )


