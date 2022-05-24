class Figure:
    init = 'cm'
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    def calculate_area(self):
        self.area = 3.14 * self.__radius ** 2
        return self.area
    def info(self):
        print(f'Circle radius: {self.__radius} {self.init}, area: {self.area}')


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b
    def calculate_area(self):
        self.area = (1/2) * self.__side_a * self.__side_b
        return self.area
    def info(self):
        print(f'RightTriangle side a: {self.__side_a} {self.init}, side b: {self.__side_b} {self.init}, area: {self.area}')


one = Circle(6)
two = Circle(15)
three = RightTriangle(4, 9)
four = RightTriangle(2, 6)
five = RightTriangle(7, 4)
one.calculate_area()
two.calculate_area()
three.calculate_area()
four.calculate_area()
five.calculate_area()


lst = [one, two, three, four, five]
for i in lst:
    i.info()
