# Задание 2
# Создайте класс TriangleChecker в котором можно проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. На вход приниматются только положительные числа. С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):

# Ура, можно построить треугольник!;
# С отрицательными числами ничего не выйдет!;
# Нужно вводить только числа!;
# Жаль, но из этого треугольник не сделать.

from typing import Sequence

class TriangleChecker:
    sides: list[float] 
    def __init__(self, sides: list[float]):
        self.sides = sides

    def is_triangle(self):
        # Проверка, что все стороны являются положительными числами
        if any(type(side) not in [int, float] for side in self.sides) or any(side <= 0 for side in self.sides):
            return "Нужно вводить только числа!" if any(type(side) not in [int, float] for side in self.sides) else "С отрицательными числами ничего не выйдет!"

        # Проверка условия существования треугольника
        a, b, c = sorted(self.sides)
        if a + b > c:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."

if __name__ == '__main__':
    # Демонстрация работы класса
    # Возможный треугольник
    checker1 = TriangleChecker([3, 4, 5])
    print(checker1.is_triangle())

    # Отрицательные числа
    checker2 = TriangleChecker([-1, 2, 3])
    print(checker2.is_triangle())

    # Не числа
    checker3 = TriangleChecker(["a", "b", "c"])
    print(checker3.is_triangle())

    # Невозможный треугольник
    checker4 = TriangleChecker([1, 2, 3])
    print(checker4.is_triangle())