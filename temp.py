from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')


def сalculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычисляет квадратный корень, если число положительное."""
    answer = сalculate_square_root(your_number)
    if your_number >= 0:
        print(f'Мы вычислили квадратный корень из введённого '
              f'вами числа. Это будет: {answer}')


print(message)
calc(25.5)