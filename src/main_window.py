from typing import Tuple
import numpy as np
import tkinter as tk
import customtkinter as ctk
from plot_window import Plot
from odestorage import van_der_pol

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    '''
    Главное окно приложения
    
    В нем можно задать параметры и начать отображение траекторий
    '''

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        '''Конструктор окна'''
        super().__init__(fg_color, **kwargs)
        
        # Настраиваем окно
        self.title("Фазовые портреты")
        self.LENGTH = 900
        self.HEIGHT = 400
        self.geometry(f"{self.LENGTH}x{self.HEIGHT}")
        
        # Настраиваем сетку
        self.ROWS_COUNT = 3
        self.COLUMNS_COUNT = 4
        self.WEIGHT = 1
        self.rowconfigure([i for i in range(self.ROWS_COUNT)], weight=self.WEIGHT)
        self.columnconfigure([i for i in range(self.COLUMNS_COUNT)], weight=self.WEIGHT)
        
        # Задаем переменные привязанные к полям ввода
        self.DEFAULT_G_VALUE = 0
        self.DEFAULT_G_PRIME_VALUE = 0.01
        self.DEFAULT_A_VALUE = 0.5
        self.g = tk.DoubleVar(self, value=self.DEFAULT_G_VALUE)
        self.g_prime = tk.DoubleVar(self, value=self.DEFAULT_G_PRIME_VALUE)
        self.a = tk.DoubleVar(self, value=self.DEFAULT_A_VALUE)
        
        # Задаем команду для валидации вещественных чисел
        self.cmd = (self.register(self.validate_float_input), '%P')

        # Заголовок зоны уравнения Ван-Дер Поля
        self.DEFAULT_FONT = ('Colibri', 25)
        self.ode_label = ctk.CTkLabel(self, text='Уравнение Ван дер Поля',
                                            font=self.DEFAULT_FONT)
        self.ode_label.grid(row=0, column=0, columnspan=4)

        # Поле ввода g(0)
        self.g_label = ctk.CTkLabel(self, text='g(0):', font=self.DEFAULT_FONT)
        self.g_label.grid(row=1, column=0)
        self.g_entry = ctk.CTkEntry(self, textvariable=self.g, validate='key',
                                    validatecommand=self.cmd)
        self.g_entry.grid(row=2, column=0)

        # Поле ввода g'(0)
        self.g_prime_label = ctk.CTkLabel(self, text='g\'(0):', 
                                          font=self.DEFAULT_FONT)
        self.g_prime_label.grid(row=1, column=1)
        self.g_prime_entry = ctk.CTkEntry(self, textvariable=self.g_prime, 
                                          validate='key',
                                          validatecommand=self.cmd)
        self.g_prime_entry.grid(row=2, column=1)

        # Поле ввожа паоаметра a для уравнения Ван-Дер Поля
        self.a_label = ctk.CTkLabel(self, text='a:', 
                                              font=self.DEFAULT_FONT)
        self.a_label.grid(row=1, column=2)
        self.a_entry = ctk.CTkEntry(self, textvariable=self.a,
                                      validate='key', 
                                      validatecommand=self.cmd)
        self.a_entry.grid(row=2, column=2)

        # Кнопка отображения фазовой траектории уравнения Ван-Дер Поля
        self.button = ctk.CTkButton(self, text='Отобразить',
                                      command=self.on_first_button_click)
        self.button.grid(row=2, column=3)
        
        # запускаем приложение
        self.mainloop()
        
    def on_first_button_click(self):
        '''
        Триггер на нажатие кнопки отобразить
        для уравнения Ван-Дер Поля
        '''

        y0 = np.array([self.g.get(), self.g_prime.get()])
        t = np.linspace(0, 1, 100)
        a = (self.a.get(),)
        Plot(y0, van_der_pol, t, a)
    
    def validate_float_input(self, val):
        '''
        Функция проверяет возможность конвертирования
        строки в число с плавающей точкой
        
        :param val: текстовое значение для валидации
        :result: логическое значение, обозначающее 
                 валидность строки
        '''
        if val != None and val != '' and val != '-':
            try:
                float(val)
            except ValueError:
                return False
        return True
