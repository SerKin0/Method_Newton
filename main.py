from matplotlib import pyplot as plt
from visual import Graph


# Главная функция
def f(x: float) -> float:
    return x ** 2 - 2 * x - 3


# Функция нахождения коэффициентов уравнения касательной к функции f(x) в точке x0
def df(x0: float):
    # Коэффициент k равен производной функции f(x)
    k = (f(x0 + eps) - f(x0)) / eps
    # Находим коэффициент b из уравнения прямой
    b = f(x0) - k * x0
    return k, b


# Границы графика
left, right = -2, 5
# Погрешность нахождения
eps = 1e-6


# Метод Ньютона
def tangent(x0: float, step: int, max_step: int):
    # Находим коэффициенты касательной к функции
    k, b = df(x0)
    # Находим точку пересечения касательной с осью x (y=0)
    x_on_0 = (-b / k)
    # Выводим данные
    print(f"x0 = {x0}\t"
          f"b = {right}\t"
          f"k = {k}\t"
          f"x_on_0 = {x_on_0}")
    # Если мы не перешли количество шагов и точка пересечения не вне отрезка
    if step <= max_step and (left <= x_on_0 <= right):
        # Добавляем на график касательную, точки и координаты
        graph_builder.create_tangent(x0, k, b, x_on_0, step)

        # Если вероятный корень не находится в погрешности, то запрашиваем функцию снова (рекурсия), иначе выводим
        # вероятный корень
        if abs(x_on_0 - x0) >= eps:
            return tangent(x_on_0, step + 1, max_step)
        else:
            return x0
    else:
        # В противном случае, выводим не удовлетворяющий ответ и ничего не выводим
        print("Ответ не был найден")
        return None


# Создаем объект класса GraphBuilder
graph_builder = Graph(f, df, left, right)
print(tangent(right, 0, 1000))

# Отображаем график
plt.show()
