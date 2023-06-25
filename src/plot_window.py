from typing import Tuple
import customtkinter as ctk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from rungekutta import rungekutta

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class Plot(ctk.CTk):
    '''
    Окно, в котором производится отрисовка фазовой траектории
    дифференциального уравнения с заданными начальными условиями
    '''

    def __init__(self, y0: np.ndarray, func: callable, t: np.ndarray, a: float,
                 fg_color: str | Tuple[str, str] | None = None, **kwargs):
        '''
        Конструктор класса

        :param: y0 начальные условия для фазовой траектории
        :param func: функция, задающая дифференциальное уравнение
        :param t: значения переменной t
        :param a: параметр a дифференциального уравнения
        '''
        super().__init__(fg_color, **kwargs)
       
        # Настраиваем окно 
        self.title("Фазовые траектория")
        self.resizable(False, False)
        self.bind('<Button-1>', self.on_click)
        
        # Инициализируем параметры
        self.mode = True
        self.t = np.linspace(0, 0.1, 10)
        self.a = a
        self.func = func

        # Вычисляем фазовую траекторию дифференциального уравнения
        self.sol = rungekutta(y0, func, t, a)
        
        # Отображаем фазовую траекторию на графике
        #with plt.style.context('dark_background'):
        self.figure = Figure(figsize=(7, 7), dpi=100)
        self.plot = self.figure.add_subplot()
        self.plot.plot(self.sol[:, 0], self.sol[:, 1], color='green', linewidth=3)

        # Создаем виджет и размещаем в окне
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.animation = FuncAnimation(self.figure, self.animate, interval=100)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        # Запускаем приложение
        self.mainloop()

    def animate(self, i):
        '''Метод дорисовки графика графика'''
        if self.mode:
            # Запоминаем последнюю точку
            y0 = self.sol[-1]

            # Получаем продолжение траектории
            self.sol = rungekutta(y0, self.func, self.t, self.a)

            # Отображаем продолжение траектории
            self.plot.plot(self.sol[:, 0], self.sol[:, 1], color='green', linewidth=3)

    def on_click(self, event):
        '''Триггер на нажатие левой кнопки мыши'''
        self.mode = not self.mode