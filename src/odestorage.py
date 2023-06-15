import numpy as np


def van_der_pol(y0: np.ndarray, t: np.ndarray, *args) -> np.ndarray:
    '''
    Функция задает дифференциальное уравнение

    u'' - a * u' * (1 - u ^ 2) + u = 0

    в виде системы

    u' = y
    y' = a * y * (1 - u ^ 2) - u

    :param y0: массив начальных условий u(0) и u'(0)
    :param t: массив значений t
    :param args: параметры дифференциального уравнения

    :result: значения u' и u'' при заданных условиях
    '''

    u, y = y0
    a = args[0]

    return np.array([y, a * y * (1 - u ** 2) - u])

def second_ode(y0: np.ndarray, t: np.ndarray, *args) -> np.ndarray:
    '''
    Функция задает дифференциальное уравнение

    u'' = ((1 + u') ^ 3 / u') * ((a * u') / (1 + u') * (1 + u' ^ 2) + u)

    в виде системы

    u' = y
    y' = ((1 + y) ^ 3 / y) * ((a * y) / (1 + y) * (1 + y ^ 2) + u)

    :param y0: массив начальных условий u(0) и u'(0)
    :param t: массив значений t
    :param args: параметры дифференциального уравнения

    :result: значения u' и u'' при заданных условиях
    '''

    u, y = y0
    a = args[0]

    return np.array([y, 
                    (1 + y) ** 3 / y * ((a * y) / (1 + y) * (1 + y ** 2) + u)])
