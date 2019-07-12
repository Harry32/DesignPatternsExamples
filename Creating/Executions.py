from .Factory import ShapeFactory
from .AbstractFactory import Shape2DFactory, Shape3DFactory


class FactoryExecution:

    @staticmethod
    def execute():

        print("Initializing Factory execution")
        print()

        print("factory = ShapeFactory()")
        factory = ShapeFactory()

        print("shape1 = factory.getShape('Circle')")
        shape1 = factory.getShape('Circle')

        print("shape1.draw()")
        shape1.draw()
        print("shape1.getSides()")
        shape1.getSides()
        print("shape1.getVertices()")
        shape1.getVertices()

        print("shape2 = factory.getShape('Triangle')")
        shape2 = factory.getShape('Triangle')

        print("shape2.draw()")
        shape2.draw()
        print("shape2.getSides()")
        shape2.getSides()
        print("shape2.getVertices()")
        shape2.getVertices()

        print("shape3 = factory.getShape('Hexagon')")
        shape3 = factory.getShape('Hexagon')


class AbstractFactoryExecution:

    @staticmethod
    def execute():

        print("Initializing Abstract Factory execution")
        print()

        print("factory2D = Shape2DFactory()")
        factory2D = Shape2DFactory()
        print("factory3D = Shape3DFactory()")
        factory3D = Shape3DFactory()

        print("shape1 = factory.getShape(1)")
        shape1 = factory2D.getShape(1)

        print("shape1.draw()")
        shape1.draw()
        print("shape1.getSides()")
        shape1.getSides()
        print("shape1.getVertices()")
        shape1.getVertices()

        print("shape2 = factory2D.getShape(3)")
        shape2 = factory2D.getShape(3)

        print("shape2.draw()")
        shape2.draw()
        print("shape2.getSides()")
        shape2.getSides()
        print("shape2.getVertices()")
        shape2.getVertices()

        print("shape3 = factory2D.getShape(6)")
        shape3 = factory2D.getShape(6)

        print("shape4 = factory.getShape(4)")
        shape4 = factory3D.getShape(4)

        print("shape4.build()")
        shape4.build()
        print("shape4.getFaces()")
        shape4.getFaces()
        print("shape4.getVertices()")
        shape4.getVertices()

        print("shape5 = factory3D.getShape(10)")
        shape5 = factory3D.getShape(10)

        print("shape5.build()")
        shape5.build()
        print("shape5.getFaces()")
        shape5.getFaces()
        print("shape5.getVertices()")
        shape5.getVertices()

        print("shape6 = factory3D.getShape(12)")
        shape6 = factory3D.getShape(12)
