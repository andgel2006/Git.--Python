# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import os


file_old = os.path.join('4.txt')
file_new = os.path.join('4_new.txt')

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(file_old, 'r', encoding='utf-8') as file_old:
    lines = file_old.readlines()

with open(file_new, 'w', encoding='utf-8') as file_new:
    for line in lines:
        row = line.split()
        row[0] = dictionary[row[0]]
        print(' '.join(row), file=file_new)