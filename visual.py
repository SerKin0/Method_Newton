import numpy as np
import matplotlib.pyplot as plt


def create_line(x, b, k):
    return k * x + b


class Graph:
    def __init__(self, f, df, a, b):
        # Подключаем переменные
        self.f = f
        self.df = df
        self.a = a
        self.b = b
        # Задаем отрезок для отображения функций
        x = np.linspace(a, b, 100)
        # Рисуем главную функцию
        plt.plot(x, f(x), label='f(x)')
        # Именуем оси
        plt.xlabel('x')
        plt.ylabel('y')
        # Рисуем оси x и y
        ax = plt.gca()
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        # Именуем график
        plt.title('График функции f(x)')
        # Показываем легенду
        plt.legend()
        # Делаем сетку на графике
        plt.grid(True)

    def create_tangent(self, x0: float, k: float, b: float, x_on_0: float, step: int):
        # Находим точку пересечения главной функции и перпендикуляра проведенного из точки лежащей на оси (y=0)
        y_on_0 = self.f(x_on_0)
        # Задаем отрезок для отображения касательной
        x = np.linspace(min(x_on_0, x0) - 1, max(x_on_0, x0) + 1, 100)
        # Рисуем касательную
        plt.plot(x, create_line(x, b, k), label=f"Касательная {step}", linewidth=.5, linestyle='dashed')

        # Ставим точки пересечения с главной функцией и осью (y=0) и пишем их координаты
        plt.scatter(x_on_0, 0, color="red")
        plt.text(x_on_0, 0, f'({x_on_0:.2f}, {0})', fontsize=9, ha='right')

        plt.scatter(x_on_0, y_on_0, color="green")
        plt.text(x_on_0, y_on_0, f'({x_on_0:.2f}, {y_on_0:.2f})', fontsize=9, ha='right')

        # Обновляем легенду
        plt.legend()
