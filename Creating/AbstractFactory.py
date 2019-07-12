# === Abstract Classes ===
class Shape2DInterface:

    def draw(self): pass
    def getSides(self): pass
    def getVertices(self): pass


class Shape3DInterface:

    def build(self): pass
    def getFaces(self): pass
    def getVertices(self): pass


# === Concrete Classes ===
class Circle(Shape2DInterface):

    def draw(self):
        print("Circle")

    def getSides(self):
        return print("1")

    def getVertices(self):
        return print("0")


class Triangle(Shape2DInterface):

    def draw(self):
        print("Triangle")

    def getSides(self):
        return print("3")

    def getVertices(self):
        return print("3")


class Square(Shape2DInterface):

    def draw(self):
        print("Square")

    def getSides(self):
        return print("4")

    def getVertices(self):
        return print("4")


class Pentagram(Shape2DInterface):

    def draw(self):
        print("Pentagram")

    def getSides(self):
        return print("5")

    def getVertices(self):
        return print("5")


class Sphere(Shape3DInterface):

    def build(self):
        print("Sphere")

    def getFaces(self):
        return print("1")

    def getVertices(self):
        return print("0")


class Pyramid(Shape3DInterface):

    def build(self):
        print("Pyramid")

    def getFaces(self):
        return print("4")

    def getVertices(self):
        return print("4")


class Cube(Shape3DInterface):

    def build(self):
        print("Cube")

    def getFaces(self):
        return print("6")

    def getVertices(self):
        return print("8")


class PentagrammicPrism(Shape3DInterface):

    def build(self):
        print("Pentagrammic Prism")

    def getFaces(self):
        return print("7")

    def getVertices(self):
        return print("10")


# === Abstract Factory ===
class ShapeFactoryInterface:
    def getShape(sides): pass


# === Concrete shape factories ===
class Shape2DFactory(ShapeFactoryInterface):

    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 3:
            return Triangle()
        if sides == 4:
            return Square()
        if sides == 5:
            return Pentagram()
        
        assert 0, "Bad 2D shape creation: shape not defined for " + sides + "sides"


class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        """here, sides refers to the number of faces"""
        if sides == 1:
            return Sphere()
        if sides == 4:
            return Pyramid()
        if sides == 6:
            return Cube()
        if sides == 10:
            return PentagrammicPrism()

        assert 0, "Bad 3D shape creation: shape not defined for " + sides + "faces"
