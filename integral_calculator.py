"""
Программа для вычисления площади фигуры через определенный интеграл
"""

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math

class IntegralCalculator:
    """Класс для вычисления определенных интегралов"""
    
    @staticmethod
    def evaluate_function(func_str, x):
        """
        Вычисление значения функции по строке
        
        Args:
            func_str (str): строка функции, например "x**2", "sin(x)"
            x (float): значение аргумента
            
        Returns:
            float: значение функции
        """
        try:
            # Создаем безопасное пространство имен для eval
            safe_dict = {
                'x': x,
                '__builtins__': None,
                'abs': abs, 'round': round,
                'min': min, 'max': max,
                'math': math,
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
                'exp': math.exp, 'log': math.log, 'log10': math.log10,
                'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e
            }
            return eval(func_str, {'__builtins__': None}, safe_dict)
        except Exception as e:
            raise ValueError(f"Ошибка вычисления функции: {e}")
    
    @staticmethod
    def method_rectangles(func_str, a, b, n):
        """
        Метод прямоугольников (средних)
        
        Args:
            func_str (str): строка функции
            a (float): нижний предел
            b (float): верхний предел
            n (int): количество разбиений
            
        Returns:
            float: значение интеграла
        """
        if n <= 0:
            raise ValueError("Количество разбиений должно быть положительным")
        
        h = (b - a) / n
        integral = 0.0
        
        for i in range(n):
            x_i = a + (i + 0.5) * h  # средняя точка
            y_i = IntegralCalculator.evaluate_function(func_str, x_i)
            integral += y_i * h
        
        return integral
    
    @staticmethod
    def method_trapezoids(func_str, a, b, n):
        """
        Метод трапеций
        
        Args:
            func_str (str): строка функции
            a (float): нижний предел
            b (float): верхний предел
            n (int): количество разбиений
            
        Returns:
            float: значение интеграла
        """
        if n <= 0:
            raise ValueError("Количество разбиений должно быть положительным")
        
        h = (b - a) / n
        integral = 0.0
        
        # Первый и последний члены
        y0 = IntegralCalculator.evaluate_function(func_str, a)
        yn = IntegralCalculator.evaluate_function(func_str, b)
        integral = (y0 + yn) / 2.0
        
        # Средние члены
        for i in range(1, n):
            x_i = a + i * h
            y_i = IntegralCalculator.evaluate_function(func_str, x_i)
            integral += y_i
        
        integral *= h
        return integral
    
    @staticmethod
    def method_simpson(func_str, a, b, n):
        """
        Метод Симпсона (для нечетного n)
        
        Args:
            func_str (str): строка функции
            a (float): нижний предел
            b (float): верхний предел
            n (int): количество разбиений (должно быть нечетным)
            
        Returns:
            float: значение интеграла
        """
        if n <= 0:
            raise ValueError("Количество разбиений должно быть положительным")
        if n % 2 == 0:
            raise ValueError("Для метода Симпсона n должно быть нечетным")
        
        h = (b - a) / n
        integral = 0.0
        
        # Первый член
        y0 = IntegralCalculator.evaluate_function(func_str, a)
        integral = y0
        
        # Средние члены
        for i in range(1, n):
            x_i = a + i * h
            y_i = IntegralCalculator.evaluate_function(func_str, x_i)
            if i % 2 == 0:
                integral += 2 * y_i
            else:
                integral += 4 * y_i
        
        # Последний член
        yn = IntegralCalculator.evaluate_function(func_str, b)
        integral += yn
        
        integral *= h / 3.0
        return integral

class IntegralGUI:
    """Класс графического интерфейса"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Оценка площади через определенный интеграл")
        self.root.geometry("900x700")
        
        # Создание элементов интерфейса
        self.create_widgets()
    
    def create_widgets(self):
        """Создание всех элементов интерфейса"""
        
        # Заголовок
        title_label = tk.Label(self.root, text="Оценка площади по функции", 
                              font=("Arial", 16, "bold"), pady=10)
        title_label.pack()
        
        # Фрейм для ввода данных
        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.pack(fill=tk.X, expand=True)
        
        # Поле для ввода функции
        func_label = ttk.Label(input_frame, text="Функция f(x):", anchor="e")
        func_label.grid(row=0, column=0, sticky="e", pady=5)
        
        self.func_entry = ttk.Entry(input_frame, width=30)
        self.func_entry.grid(row=0, column=1, sticky="w", pady=5)
        self.func_entry.insert(0, "x**2")
        
        # Подсказка
        hint_label = ttk.Label(input_frame, text="Например: x**2, sin(x), exp(x), 2*x+3", 
                              foreground="gray")
        hint_label.grid(row=0, column=2, sticky="w", pady=5)
        
        # Поля для пределов интегрирования
        a_label = ttk.Label(input_frame, text="Нижний предел (a):", anchor="e")
        a_label.grid(row=1, column=0, sticky="e", pady=5)
        
        self.a_entry = ttk.Entry(input_frame, width=15)
        self.a_entry.grid(row=1, column=1, sticky="w", pady=5)
        self.a_entry.insert(0, "0")
        
        b_label = ttk.Label(input_frame, text="Верхний предел (b):", anchor="e")
        b_label.grid(row=1, column=2, sticky="e", pady=5)
        
        self.b_entry = ttk.Entry(input_frame, width=15)
        self.b_entry.grid(row=1, column=3, sticky="w", pady=5)
        self.b_entry.insert(0, "2")
        
        # Поле для количества разбиений
        n_label = ttk.Label(input_frame, text="Количество разбиений (n):", anchor="e")
        n_label.grid(row=2, column=0, sticky="e", pady=5)
        
        self.n_entry = ttk.Entry(input_frame, width=15)
        self.n_entry.grid(row=2, column=1, sticky="w", pady=5)
        self.n_entry.insert(0, "1000")
        
        # Выпадающий список для метода интегрирования
        method_label = ttk.Label(input_frame, text="Метод интегрирования:", anchor="e")
        method_label.grid(row=3, column=0, sticky="e", pady=5)
        
        self.method_var = tk.StringVar()
        self.method_combobox = ttk.Combobox(input_frame, textvariable=self.method_var, width=25)
        self.method_combobox['values'] = (
            "Метод прямоугольников",
            "Метод трапеций",
            "Метод Симпсона"
        )
        self.method_combobox.grid(row=3, column=1, sticky="w", pady=5)
        self.method_combobox.current(0)
        
        # Кнопка "Вычислить"
        self.calc_button = ttk.Button(input_frame, text="Вычислить", 
                                     command=self.calculate)
        self.calc_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Область для вывода результата
        result_frame = ttk.LabelFrame(self.root, text="Результат", padding=10)
        result_frame.pack(fill=tk.X, expand=True, pady=10)
        
        self.result_label = ttk.Label(result_frame, text="", font=("Arial", 12))
        self.result_label.pack()
        
        # Область для графика
        self.plot_frame = ttk.LabelFrame(self.root, text="График", padding=10)
        self.plot_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Создаем фигуру matplotlib
        self.figure = plt.Figure(figsize=(8, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def calculate(self):
        """Обработчик нажатия "Вычислить""" 
        try:
            # Получаем данные из полей
            func_str = self.func_entry.get().strip()
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            n = int(self.n_entry.get())
            
            # Проверка корректности ввода
            if a >= b:
                raise ValueError("Нижний предел должен быть меньше верхнего")
            
            # Выбор метода интегрирования
            method = self.method_var.get()
            
            if method == "Метод прямоугольников":
                result = IntegralCalculator.method_rectangles(func_str, a, b, n)
            elif method == "Метод трапеций":
                result = IntegralCalculator.method_trapezoids(func_str, a, b, n)
            elif method == "Метод Симпсона":
                result = IntegralCalculator.method_simpson(func_str, a, b, n)
            else:
                raise ValueError("Неизвестный метод интегрирования")
            
            # Отображение результата
            result_text = f"Площадь под кривой: {result:.6f}"
            self.result_label.config(text=result_text, foreground="green")
            
            # Построение графика
            self.plot_function(func_str, a, b, n, result)
            
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Непредвиденная ошибка: {e}")
    
    def plot_function(self, func_str, a, b, n, result):
        """Построение графика функции"""
        
        # Очищаем предыдущий график
        self.figure.clear()
        
        # Создаем подмножество для графика
        ax = self.figure.add_subplot(111)
        
        # Генерируем данные для графика
        x = np.linspace(a, b, 1000)
        y = np.array([IntegralCalculator.evaluate_function(func_str, xi) for xi in x])
        
        # Построение графика функции
        ax.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {func_str}')
        
        # Заливка области под кривой
        ax.fill_between(x, y, 0, color='skyblue', alpha=0.4)
        
        # Вертикальные линии x = a и x = b
        ax.axvline(x=a, color='red', linestyle='--', linewidth=1, label=f'x = {a}')
        ax.axvline(x=b, color='red', linestyle='--', linewidth=1, label=f'x = {b}')
        
        # Точки разбиения (опционально)
        if n <= 100:  # не показываем точки для больших n
            h = (b - a) / n
            x_points = [a + i * h for i in range(n+1)]
            y_points = [IntegralCalculator.evaluate_function(func_str, xi) for xi in x_points]
            ax.plot(x_points, y_points, 'ro', markersize=4, label='точки разбиения')
        
        # Настройка графика
        ax.set_title('График функции и площадь', fontsize=12)
        ax.set_xlabel('x', fontsize=10)
        ax.set_ylabel('f(x)', fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc='best')
        ax.set_xlim(min(a, min(x)), max(b, max(x)))
        
        # Добавляем текст с результатом
        ax.text(0.05, 0.95, f'Площадь = {result:.6f}', 
                transform=ax.transAxes, fontsize=10, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        # Обновляем canvas
        self.canvas.draw()

def main():
    """Основная функция"""
    root = tk.Tk()
    app = IntegralGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()