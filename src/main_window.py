from typing import Optional, Tuple, Union
import numpy as np
import tkinter as tk
import customtkinter as ctk
from plot_window import Plot
from odestorage import van_der_pol, second_ode

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
        self.length = 900
        self.height = 400
        self.geometry(f"{self.length}x{self.height}")
        
        # Настраиваем сетку
        self.rowconfigure([i for i in range(6)], weight=1)
        self.columnconfigure([i for i in range(4)], weight=1)
        
        # Задаем переменные привязанные к полям ввода
        self.g = tk.DoubleVar(self, value=0)
        self.g_prime = tk.DoubleVar(self, value=0.01)
        self.first_a = tk.DoubleVar(self, value=0.5)
        
        self.f = tk.DoubleVar(self, value=0)
        self.f_prime = tk.DoubleVar(self, value=0.01)
        self.second_a = tk.DoubleVar(self, value=0.5)
        
        # Задаем команду для валидации вещественных чисел
        self.cmd = (self.register(self.validate_float_input), '%P')

        # Заголовок зоны уравнения Ван-Дер Поля
        self.first_ode_label = ctk.CTkLabel(self, text='Уравнение Ван дер Поля',
                                            font=('Colibri', 25))
        self.first_ode_label.grid(row=0, column=0, columnspan=4)

        # Поле ввода g(0)
        self.g_label = ctk.CTkLabel(self, text='g(0):', font=('Colibri', 25))
        self.g_label.grid(row=1, column=0)
        self.g_entry = ctk.CTkEntry(self, textvariable=self.g, validate='key',
                                    validatecommand=self.cmd)
        self.g_entry.grid(row=2, column=0)

        # Поле ввода g'(0)
        self.g_prime_label = ctk.CTkLabel(self, text='g\'(0):', 
                                          font=('Colibri', 25))
        self.g_prime_label.grid(row=1, column=1)
        self.g_prime_entry = ctk.CTkEntry(self, textvariable=self.g_prime, 
                                          validate='key',
                                          validatecommand=self.cmd)
        self.g_prime_entry.grid(row=2, column=1)

        # Поле ввожа паоаметра a для уравнения Ван-Дер Поля
        self.first_ode_a_label = ctk.CTkLabel(self, text='a:', 
                                              font=('Colibri', 25))
        self.first_ode_a_label.grid(row=1, column=2)
        self.g_a_entry = ctk.CTkEntry(self, textvariable=self.first_a,
                                      validate='key', 
                                      validatecommand=self.cmd)
        self.g_a_entry.grid(row=2, column=2)

        # Кнопка отображения фазовой траектории уравнения Ван-Дер Поля
        self.g_button = ctk.CTkButton(self, text='Отобразить',
                                      command=self.on_first_button_click)
        self.g_button.grid(row=2, column=3)
        
        # Заголовок зоны второго уравнения
        self.second_ode_label = ctk.CTkLabel(self, text='Второе уравнение', 
                                             font=('Colibri', 25))
        self.second_ode_label.grid(row=3, column=0, columnspan=4)
        
        # Поле ввода f(0) для второго уравнения
        self.f_label = ctk.CTkLabel(self, text='f(0)', font=('Colibri', 25))
        self.f_label.grid(row=4, column=0)
        self.f_entry = ctk.CTkEntry(self, textvariable=self.f, validate='key',
                                    validatecommand=self.cmd)
        self.f_entry.grid(row=5, column=0)

        # Поле ввода f'(0) для второго уравнения
        self.f_prime_label = ctk.CTkLabel(self, text='f\'(0):', 
                                          font=('Colibri', 25))
        self.f_prime_label.grid(row=4, column=1)
        self.f_prime_entry = ctk.CTkEntry(self, textvariable=self.f_prime,
                                          validate='key',
                                          validatecommand=self.cmd)
        self.f_prime_entry.grid(row=5, column=1)

        # Поле ввода a для второго уравнения
        self.second_ode_a_label = ctk.CTkLabel(self, text='a:', 
                                               font=('Colibri', 25))
        self.second_ode_a_label.grid(row=4, column=2)
        self.f_a_entry = ctk.CTkEntry(self, textvariable=self.second_a,
                                      validate='key',
                                      validatecommand=self.cmd)
        self.f_a_entry.grid(row=5, column=2)

        # Кнопка отображения фазовой траектории второго уравнения
        self.f_button = ctk.CTkButton(self, text='Отобразить',
                                      command = self.on_second_button_click)
        self.f_button.grid(row=5, column=3)
        
        # запускаем приложение
        self.mainloop()
        
    def on_first_button_click(self):
        '''
        Триггер на нажатие кнопки отобразить
        для уравнения Ван-Дер Поля
        '''

        y0 = np.array([self.g.get(), self.g_prime.get()])
        func = van_der_pol
        t = np.linspace(0, 1, 100)
        a = (self.first_a.get(),)
        Plot(y0, func, t, a)
    
    def on_second_button_click(self):
        '''
        Триггер на нажатие кнопки отобразить
        для второго уравнения
        '''

        y0 = np.array([self.f.get(), self.f_prime.get()])
        func = second_ode
        t = np.linspace(0, 0.0001, 10)
        a = (self.second_a.get(),)
        Plot(y0, func, t, a)

    def validate_float_input(self, val):
        '''
        Функция проверяет возможность конвертирования
        строки в число с плавающей точкой
        '''
        if val != None and val != '' and val != '-':
            try:
                float(val)
            except ValueError:
                return False
        return True
