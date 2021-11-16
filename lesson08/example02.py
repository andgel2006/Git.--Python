# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.



class DivisionByNull(Exception):
    def __init__(self, txt):
        self.txt = txt


def divide_by_null():
    try:
        делимое = int(input('Введите делимое: >>>'))
        делитель = int(input('Введите делитель: >>>'))
        if делитель == 0:
            raise DivisionByNull("Деление на ноль недопустимо")
        else:
            res = делимое / делитель
            return res
    except ValueError:
        return "Вы ввели не число"
    except DivisionByNull as err:
        return err


print(f"Результат: {divide_by_null()}")
