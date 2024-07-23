from abc import ABC, abstractmethod
import unittest
import math
class Figure(ABC): # Базовый абстрактный класс для геометрических фигур.

    __NAME = ''
    __slots__ = ()

    @abstractmethod
    def square_figure(self): # Aбстрактный метод. Должен быть переопределен в дочерних классах для расчета площади фигуры.
        pass


    def check_value(self, x):

        """Проверяет, является ли значение x положительным числом.
        Вызывает исключение TypeError, если значение некорректно."""

        if type(x) not in (int, float) or not x > 0:
            raise TypeError('Введите положительные числа больше 0')




class Circle(Figure): # Класс, представляющий круг.

    __NAME = 'круга'
    __slots__ = ('__radius')


    def __init__(self, *args):

        """Конструктор, принимающий радиус круга в качестве аргумента.
        Выполняет проверку введенных значений."""

        if len(args) != 1:
            raise Exception('Введите одно число')
        self.check_value(args[0])
        self.__radius = args[0]


    @property
    def radius(self): #  Предоставляет доступ к радиусу круга.
        return self.__radius

    @radius.setter
    def radius(self, val): # Возвращает площадь круга.
        self.check_value(val)
        self.__radius = val

    @property
    def square_figure(self):
        return self.__square_figure()

    def __square_figure(self): # Частный метод, вычисляющий площадь круга.
        return self.__radius**2 * 3.14


    def __str__(self): # Возвращает строковое представление объекта круга, содержащее информацию о площади.
        return f"Площадь {self.__NAME}: {self.__square_figure()}"


class Triangle(Figure): # Класс, представляющий треугольник.

    __NAME = 'треугольника'
    __slots__ = ('__a', '__b', '__c')

    def __init__(self, *args):

        """Конструктор, принимающий длины сторон треугольника в качестве аргументов.
        Выполняет проверку введенных значений и проверяет, являются ли стороны треугольника корректными
        (сумма длин двух сторон должна быть больше длины третьей стороны).
        """

        if len(args) != 3:
            raise Exception('Введите три числа')

        all([self.check_value(val) for val in (args[0], args[1], args[2])])
        self.__check_triangle(args[0], args[1], args[2])
        self.__a = args[0]
        self.__b = args[1]
        self.__c = args[2]



    def __check_triangle(self, a, b, c): # проверяет существование треугольника
        if not a + b > c or not b + c > a or not a + c > b:
            raise Exception('Введите длинну существующего треугольника')


    # a, b, c (свойства): Предоставляют доступ к длинам сторон треугольника
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        self.check_value(val)
        self.__a = val

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        self.check_value(val)
        self.__b = val

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        self.check_value(val)
        self.__c = val

    @property
    def square_figure(self):
        return self.__square_figure()

    def __is_right_triangle(self, a, b, c): # Частный метод, определяющий, является ли треугольник прямоугольным.
        sides = sorted([a, b, c])
        a, b, c = sides
        return math.isclose(a ** 2 + b ** 2, c ** 2)

    def __square_figure(self): # Частный метод, вычисляющий площадь треугольника по формуле Герона.
        a = self.__a
        b = self.__b
        c = self.__c
        p = (a + b + c) / 2
        if self.__is_right_triangle(a, b, c):
            print('Треугольник прямоугольний')
            return (p*(p - a)*(p - b)*(p - c))**0.5
        else:
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5


    def __str__(self): #  Возвращает строковое представление объекта треугольника, содержащее информацию о площади.
        return f"Площадь {self.__NAME}: {self.__square_figure()}"



# Вычисление площади фигуры без знания типа фигуры
figure = {
    "круг": Circle,
    "треугольник": Triangle,
}

type_figure= input("Введите тип фигуры: ")
values = input("Введите параметры (через пробел): ")


values = [float(x) for x in values.split()]

figure_class = figure[type_figure]
figure = figure[type_figure](*values)

print(figure)



class TestFigure(unittest.TestCase): #  Класс для тестирования функций, связанных с расчетом площади.

    # Тестирует расчет площади круга.
    def test_circle(self):
        circle = Circle(5)
        self.assertEqual(circle.square_figure, 78.5)

    # Тестирует расчет площади прямоугольного треугольника.
    def test_triangle_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.square_figure, 6.0)

    # Тестирует расчет площади не прямоугольного треугольника.
    def test_triangle_not_right(self):
        triangle = Triangle(3, 4, 6)
        self.assertEqual(triangle.square_figure, 5.332682251925386)

    # Тестирует проверку значения на корректность (положительное число).
    def test_check_value(self):
        circle = Circle(5)
        with self.assertRaises(TypeError):
            circle.check_value(-1)

    # Тестирует проверку корректности сторон треугольника.
    def test_check_triangle(self):
        with self.assertRaises(Exception):
            Triangle(1, 2, 5)

if __name__ == '__main__':
    unittest.main()

