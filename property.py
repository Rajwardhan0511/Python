class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2  # No need for parentheses

c = Circle(5)
print(c.area)  # 78.5
