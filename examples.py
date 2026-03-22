"""
Примеры использования программы для вычисления интегралов
"""

from integral_calculator import IntegralCalculator
import math

# Пример 1: Простая функция
print("=== Пример 1: x^2 от 0 до 2 ===")
func = "x**2"
a, b = 0, 2
n = 1000

print(f"Метод прямоугольников: {IntegralCalculator.method_rectangles(func, a, b, n):.6f}")
print(f"Метод трапеций: {IntegralCalculator.method_trapezoids(func, a, b, n):.6f}")
print(f"Метод Симпсона: {IntegralCalculator.method_simpson(func, a, b, n*2+1):.6f}")
print()

# Пример 2: Тригонометрическая функция
print("=== Пример 2: sin(x) от 0 до pi ===")
func = "sin(x)"
a, b = 0, math.pi
n = 101  # для Симпсона нужно нечетное

print(f"Метод прямоугольников: {IntegralCalculator.method_rectangles(func, a, b, n):.6f}")
print(f"Метод трапеций: {IntegralCalculator.method_trapezoids(func, a, b, n):.6f}")
print(f"Метод Симпсона: {IntegralCalculator.method_simpson(func, a, b, n):.6f}")
print()

# Пример 3: Экспоненциальная функция
print("=== Пример 3: exp(x) от 0 до 1 ===")
func = "exp(x)"
a, b = 0, 1
n = 500

print(f"Метод прямоугольников: {IntegralCalculator.method_rectangles(func, a, b, n):.6f}")
print(f"Метод трапеций: {IntegralCalculator.method_trapezoids(func, a, b, n):.6f}")
print(f"Метод Симпсона: {IntegralCalculator.method_simpson(func, a, b, n*2+1):.6f}")
print()

# Пример 4: Сложная функция
print("=== Пример 4: x^3 - 2*x^2 + 5 от 1 до 3 ===")
func = "x**3 - 2*x**2 + 5"
a, b = 1, 3
n = 1000

print(f"Метод прямоугольников: {IntegralCalculator.method_rectangles(func, a, b, n):.6f}")
print(f"Метод трапеций: {IntegralCalculator.method_trapezoids(func, a, b, n):.6f}")
print(f"Метод Симпсона: {IntegralCalculator.method_simpson(func, a, b, n*2+1):.6f}")
print()