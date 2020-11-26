class Area:
    def __get__(self, instance, owner):
        if owner == Rectangle or owner == Squer:
            return instance.height * instance.width
        if owner == Circle:
            return instance.radius * instance.radius * 3.14

class Perimeter:
    def __get__(self, instance, owner):
        if owner == Rectangle or owner == Squer:
            return (instance.height + instance.width) * 2
        if owner == Circle:
            return 2 * instance.radius * 3.14

class Geometry:
    area = Area()
    perimeter = Perimeter()

class Rectangle(Geometry):
    def __init__(self, width, height):
        self.height = height
        self.width = width

class Squer(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

class Circle(Geometry):
    def __init__(self,radius):
        self.radius = radius


req = Rectangle(15, 10)
squ = Squer(10)
cir = Circle(5)
print(req.area, req.perimeter)
print(squ.area, squ.perimeter)
print(cir.area, cir.perimeter)