import numpy as np


def rungekutta(y0: np.ndarray, f: callable, t, args=(0.5)) -> np.ndarray:
    '''
    Функция численно находит решение для краевой задачи
    дифференциального уравнения методом Рунге Кутты

    :param y0: массив начальных условий y(0) и y'(0)
    :param f: функция, задающая дифференциальное уравнение
    :param t: массив значений переменной t
    :param args: параметры дифференциального уравнения

    :result: массив, содержащий значения y и y'
    '''
    # Вычисляем количество точек
    n = len(t)

    # Задаем массив, в котором будет храниться результат
    sol = np.zeros((n, len(y0)))

    # Кладем первые значения в массив результата
    sol[0] = y0

    # Запускаем основной цикл
    for i in range(n - 1):
        # Вычисляем шаг
        hop = t[i + 1] - t[i]

        # Вычисляем значения k1, k2, k3, k4
        k1 = f(sol[i], t[i], *args)
        k2 = f(sol[i] + k1 * hop / 2., t[i] + hop / 2., *args)
        k3 = f(sol[i] + k2 * hop / 2., t[i] + hop / 2., *args)
        k4 = f(sol[i] + k3 * hop, t[i] + hop, *args)

        # Находим значения y и y' на текущем шаге
        sol[i + 1] = sol[i] + (hop / 6.) * (k1 + 2 * k2 + 2 * k3 + k4)

        if sol[i + 1, 0] == np.nan or sol[i + 1, 1] == np.nan:
            return sol[:i + 1]
    return sol
