# === Abstract Classes ===
class ShapeInterface:

    def draw(self): pass
    def getSides(self): pass
    def getVertices(self): pass


# === Concrete Classes ===
class Circle(ShapeInterface):

    def draw(self):
        print("Circle")

    def getSides(self):
        return print("1")

    def getVertices(self):
        return print("0")


class Triangle(ShapeInterface):

    def draw(self):
        print("Triangle")

    def getSides(self):
        return print("3")

    def getVertices(self):
        return print("3")


class Square(ShapeInterface):

    def draw(self):
        print("Square")

    def getSides(self):
        return print("4")

    def getVertices(self):
        return print("4")


class Pentagram(ShapeInterface):

    def draw(self):
        print("Pentagram")

    def getSides(self):
        return print("5")

    def getVertices(self):
        return print("5")


# === Factory ===
class ShapeFactory:

    @staticmethod
    def getShape(shapeType):

        if shapeType == 'Circle':
            return Circle()
        if shapeType == 'Triangle':
            return Triangle()
        if shapeType == 'Square':
            return Square()
        if shapeType == 'Pentagram':
            return Pentagram()

        assert 0, "Could not find shape " + shapeType
