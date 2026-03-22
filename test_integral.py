"""
Тестовые сценарии для проверки программы
"""

import unittest
from integral_calculator import IntegralCalculator
import math

class TestIntegralCalculator(unittest.TestCase):
    
    def test_method_rectangles(self):
        """Тестирование метода прямоугольников"""
        # Тест 1: x^2 от 0 до 2
        result = IntegralCalculator.method_rectangles("x**2", 0, 2, 1000)
        self.assertAlmostEqual(result, 8/3, delta=0.01)  # точный интеграл = 8/3
        
        # Тест 2: sin(x) от 0 до pi
        result = IntegralCalculator.method_rectangles("sin(x)", 0, math.pi, 1000)
        self.assertAlmostEqual(result, 2.0, delta=0.01)
        
        # Тест 3: exp(x) от 0 до 1
        result = IntegralCalculator.method_rectangles("exp(x)", 0, 1, 1000)
        self.assertAlmostEqual(result, math.e - 1, delta=0.01)
    
    def test_method_trapezoids(self):
        """Тестирование метода трапеций"""
        # Тест 1: x^2 от 0 до 2
        result = IntegralCalculator.method_trapezoids("x**2", 0, 2, 1000)
        self.assertAlmostEqual(result, 8/3, delta=0.01)
        
        # Тест 2: sin(x) от 0 до pi
        result = IntegralCalculator.method_trapezoids("sin(x)", 0, math.pi, 1000)
        self.assertAlmostEqual(result, 2.0, delta=0.01)
        
        # Тест 3: exp(x) от 0 до 1
        result = IntegralCalculator.method_trapezoids("exp(x)", 0, 1, 1000)
        self.assertAlmostEqual(result, math.e - 1, delta=0.01)
    
    def test_method_simpson(self):
        """Тестирование метода Симпсона"""
        # Тест 1: x^2 от 0 до 2 (n должно быть нечетным)
        result = IntegralCalculator.method_simpson("x**2", 0, 2, 1001)
        self.assertAlmostEqual(result, 8/3, delta=0.001)  # более точная проверка
        
        # Тест 2: sin(x) от 0 до pi
        result = IntegralCalculator.method_simpson("sin(x)", 0, math.pi, 101)
        self.assertAlmostEqual(result, 2.0, delta=0.001)
        
        # Тест 3: exp(x) от 0 до 1
        result = IntegralCalculator.method_simpson("exp(x)", 0, 1, 1001)
        self.assertAlmostEqual(result, math.e - 1, delta=0.001)
    
    def test_evaluate_function(self):
        """Тестирование вычисления функции"""
        # Простые функции
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("x**2", 2), 4)
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("2*x + 3", 1), 5)
        
        # Тригонометрические
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("sin(x)", math.pi/2), 1.0, delta=0.001)
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("cos(x)", 0), 1.0)
        
        # Экспоненциальные
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("exp(x)", 1), math.e, delta=0.001)
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("log(x)", math.e), 1.0)
        
        # С константами
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("pi*x", 1), math.pi)
        self.assertAlmostEqual(IntegralCalculator.evaluate_function("e*x", 1), math.e)
    
    def test_error_handling(self):
        """Тестирование обработки ошибок"""
        # Некорректная функция
        with self.assertRaises(ValueError):
            IntegralCalculator.evaluate_function("x/0", 1)
        
        # Некорректные пределы
        with self.assertRaises(ValueError):
            IntegralCalculator.method_rectangles("x**2", 2, 1, 100)  # a > b
        
        # Некорректное n
        with self.assertRaises(ValueError):
            IntegralCalculator.method_rectangles("x**2", 0, 1, 0)
        
        # Нечетное n для Симпсона
        with self.assertRaises(ValueError):
            IntegralCalculator.method_simpson("x**2", 0, 1, 100)  # четное n

if __name__ == "__main__":
    unittest.main()