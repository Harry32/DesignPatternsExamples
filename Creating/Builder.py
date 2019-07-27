# === Car ===
class Car:

    def __init__(self):

        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):

        self.__body = body

    def attachWheel(self, wheel):

        self.__wheels.append(wheel)

    def setEngine(self, engine):

        self.__engine = engine

    def getSpecifications(self):

        print("Body: %s" % self.__body.shape)
        print("Engine horsepower: %d" % self.__engine.horsepower)
        print("Tire size: %d\'" % self.__wheels[0].size)


# === Car parts ===
class Wheel:

    size = None


class Engine:

    horsepower = None


class Body:

    shape = None


# === Director ===
class Director:

    __builder = None

    def setBuilder(self, builder):

        self.__builder = builder

    # The algorithm for assembling a car
    def getCar(self):

        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car


# === Abstract Builder ===
class BuilderInterface:

    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass


# === Concrete Builders ===
class JeepBuilder(BuilderInterface):

    def getWheel(self):

        wheel = Wheel()
        wheel.size = 22

        return wheel

    def getEngine(self):

        engine = Engine()
        engine.horsepower = 400

        return engine

    def getBody(self):

        body = Body()
        body.shape = "SUV"

        return body


class NissanBuilder(BuilderInterface):

    def getWheel(self):

        wheel = Wheel()
        wheel.size = 16

        return wheel

    def getEngine(self):

        engine = Engine()
        engine.horsepower = 100

        return engine

    def getBody(self):

        body = Body()
        body.shape = "Hatchback"

        return body
