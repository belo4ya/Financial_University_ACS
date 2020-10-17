# 8. Дана последовательность натуральных чисел (одно число в строке),
# завершающаяся числом 0. Определите значение второго по величине
# элемента в этой последовательности, то есть элемента, который будет
# наибольшим, если из последовательности удалить наибольший элемент.
# В этой задаче нельзя использовать глобальные переменные. Функция
# получает данные, считывая их с клавиатуры, а не получая их в виде параметра.
# В программе функция возвращает результат в виде кортежа из нескольких
# чисел и функция вообще не получает никаких параметров. Гарантируется,
#что последовательность содержит хотя бы два числа (кроме нуля)


def pre_max():
    n = int(input())
    if n == 0:
        return (0, 0)
    t = pre_max()
    if n > t[1]:
        return (t[1], n)
    elif n > t[0]:
        return (n, t[1])
    else:
        return t

if __name__ == "__main__":
    t = pre_max()
    print(t[0])