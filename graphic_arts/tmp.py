from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Вычисление квадратного корня из числа."""
    if your_number <= 0:
        return None
    print('Мы вычислили квадратный корень из'
          + 'введённого вами числа. Это будет: '
          + f'{CalculateSquareRoot(your_number)}')


if __name__ == '__main__':
    print(message)
    calc(25.5)