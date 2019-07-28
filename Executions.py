from Creating.Factory import ShapeFactory
from Creating.AbstractFactory import Shape2DFactory, Shape3DFactory
from Creating.Builder import Director as DirectorBuilder, JeepBuilder, NissanBuilder
from Creating.Prototype import Director as DirectorPrototype, JeepBuilder as JeepBuilderPrototype, NissanBuilder as NissanBuilderPrototype
from Creating.Singleton import Singleton
from Creating.Borg import Borg
from Structuring.Facade import Car
from Structuring.Proxy import Blog, AnonUserBlogProxy
from Structuring.Decorator import Window, BorderDecorator, VerticalSBDecorator, HorizontalSBDecorator
from Structuring.Adapter import EuropeanSocket, AmericanKettle, Adapter
from Behaving.Command import Screen, ScreenInvoker, CutCommand, PasteCommand
from Behaving.Interpreter import TerminalExpression, AndExpression, OrExpression
from Behaving.State import Computer, On, Off, Suspend, Hibernate
from Behaving.ChainOfResponsibility import Car as CarChain, WaterHandler, FuelHandler, OilHandler
from Behaving.Observer import Observable, AmericanStockMarket, EuropeanStockMarket
from Behaving.Strategy import PrimeFinderClient
from Behaving.Memento import Data
from Behaving.Template import MakePizza, MakeCake


# region Factory
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

        print()

        print("shape2 = factory.getShape('Triangle')")
        shape2 = factory.getShape('Triangle')

        print("shape2.draw()")
        shape2.draw()
        print("shape2.getSides()")
        shape2.getSides()
        print("shape2.getVertices()")
        shape2.getVertices()

        print()

        print("shape3 = factory.getShape('Hexagon')")
        shape3 = factory.getShape('Hexagon')
# endregion


# region AbstractFactory
class AbstractFactoryExecution:

    @staticmethod
    def execute():

        print("Initializing Abstract Factory execution")
        print()

        print("factory2D = Shape2DFactory()")
        factory2D = Shape2DFactory()
        print("factory3D = Shape3DFactory()")
        factory3D = Shape3DFactory()

        print()

        print("shape1 = factory.getShape(1)")
        shape1 = factory2D.getShape(1)

        print("shape1.draw()")
        shape1.draw()
        print("shape1.getSides()")
        shape1.getSides()
        print("shape1.getVertices()")
        shape1.getVertices()

        print()

        print("shape2 = factory2D.getShape(3)")
        shape2 = factory2D.getShape(3)

        print("shape2.draw()")
        shape2.draw()
        print("shape2.getSides()")
        shape2.getSides()
        print("shape2.getVertices()")
        shape2.getVertices()

        print()

        print("shape3 = factory2D.getShape(6)")
        shape3 = factory2D.getShape(6)

        print()
        print("-----------------------------------------")
        print()

        print("shape4 = factory.getShape(4)")
        shape4 = factory3D.getShape(4)

        print("shape4.build()")
        shape4.build()
        print("shape4.getFaces()")
        shape4.getFaces()
        print("shape4.getVertices()")
        shape4.getVertices()

        print()

        print("shape5 = factory3D.getShape(10)")
        shape5 = factory3D.getShape(10)

        print("shape5.build()")
        shape5.build()
        print("shape5.getFaces()")
        shape5.getFaces()
        print("shape5.getVertices()")
        shape5.getVertices()

        print()

        print("shape6 = factory3D.getShape(12)")
        shape6 = factory3D.getShape(12)
# endregion


# region Builder
class BuilderExecution:

    @staticmethod
    def execute():

        print("Initializing Builder execution")
        print()

        print("director = Director()")
        director = DirectorBuilder()

        print("director.setBuilder(JeepBuilder())")
        director.setBuilder(JeepBuilder())

        print("car1 = director.getCar()")
        car1 = director.getCar()

        print("car1.getSpecifications()")
        car1.getSpecifications()

        print()
        print("-----------------------------------------")
        print()

        print("director.setBuilder(NissanBuilder())")
        director.setBuilder(NissanBuilder())

        print("car2 = director.getCar()")
        car2 = director.getCar()

        print("car2.getSpecifications()")
        car2.getSpecifications()
# endregion


# region Prototype
class PrototypeExecution:

    @staticmethod
    def execute():

        print("Initializing Prototype execution")
        print()

        print("director = Director()")
        director = DirectorPrototype()

        print("director.setBuilder(JeepBuilder())")
        director.setBuilder(JeepBuilderPrototype())

        print("car1 = director.getCar()")
        car1 = director.getCar()

        print("car1.getSpecifications()")
        car1.getSpecifications()

        print()

        print("car2 = car1.clone()")
        car2 = car1.clone()

        print("car2.getSpecifications()")
        car2.getSpecifications()

        print()
        print("-----------------------------------------")
        print()

        print("director.setBuilder(NissanBuilder())")
        director.setBuilder(NissanBuilderPrototype())

        print("car3 = director.getCar()")
        car3 = director.getCar()

        print("car3.getSpecifications()")
        car3.getSpecifications()

        print("car4 = car3.clone(\"White\")")
        car4 = car1.clone("White")

        print("car4.getSpecifications()")
        car4.getSpecifications()
# endregion


# region Singleton
class SingletonExecution:

    @staticmethod
    def execute():

        print("Initializing Singleton execution")
        print()

        print("x = Singleton()")
        x = Singleton()

        print("x.val = \"Burger\"")
        x.val = "Burger"

        print("print(x.val)")
        print(x.val)

        print()

        print("y = Singleton()")
        y = Singleton()

        print("y.val = \"Chips\"")
        y.val = "Chips"

        print("print(y.val)")
        print(y.val)

        print()

        print("print(x.val)")
        print(x.val)

        print()

        print("print(x == y)")
        print(x == y)
# endregion


# region Borg
class BorgExecution:

    @staticmethod
    def execute():
        print("Initializing Borg execution")
        print()

        print("x = Borg()")
        x = Borg()

        print("x.val = \"Burger\"")
        x.val = "Burger"

        print("print(x.val)")
        print(x.val)

        print()

        print("y = Borg()")
        y = Borg()

        print("y.val = \"Chips\"")
        y.val = "Chips"

        print("print(y.val)")
        print(y.val)

        print()

        print("print(x.val)")
        print(x.val)

        print()

        print("print(x == y)")
        print(x == y)
# endregion


# region Facade
class FacadeExecution:

    @staticmethod
    def execute():
        print("Initializing Facade execution")
        print()

        print("car = Car()")
        car = Car()

        print("car.turn_key()")
        car.turn_key()

        print("car.jump()")
        car.jump()

        print("car.turn_key()")
        car.turn_key()
# endregion


# region Proxy
class ProxyExecution:

    @staticmethod
    def execute():
        print("Initializing Proxy execution")
        print()

        print(">>> blog = Blog()")
        blog = Blog()

        print(">>> blog.read()")
        blog.read()

        print(">>> blog.write()")
        blog.write()

        print()

        print(">>> proxy = AnonUserBlogProxy(blog)")
        proxy = AnonUserBlogProxy(blog)

        print(">>> proxy.read()")
        proxy.read()

        print(">>> proxy.write()")
        proxy.write()
# endregion


# region Decorator
class DecoratorExecution:

    @staticmethod
    def execute():
        print("Initializing Decorator execution")
        print()

        print(">>> w = Window()")
        w = Window()

        print(">>> w.build()")
        w.build()

        print(">>> wb = BorderDecorator(w)")
        wb = BorderDecorator(w)

        print(">>> wb.build()")
        wb.build()

        print(">>> wbv = VerticalSBDecorator(wb)")
        wbv = VerticalSBDecorator(wb)

        print(">>> wbv.build()")
        wbv.build()

        print(">>> wbvh = HorizontalSBDecorator(wbv)")
        wbvh = HorizontalSBDecorator(wbv)

        print(">>> wbvh.build()")
        wbvh.build()
# endregion


# region Adapter
class AdapterExecution:

    @staticmethod
    def execute():
        print("Initializing Adapter execution")
        print()

        print(">>> socket = EuropeanSocket()")
        socket = EuropeanSocket()

        print(">>> kettle = AmericanKettle(socket)")
        kettle = AmericanKettle(socket)

        print(">>> kettle.boil()")
        kettle.boil()

        print(">>> adapter = Adapter(socket)")
        adapter = Adapter(socket)

        print(">>> kettle = AmericanKettle(adapter)")
        kettle = AmericanKettle(adapter)

        print(">>> kettle.boil()")
        kettle.boil()
# endregion


# region Command
class CommandExecution:

    @staticmethod
    def execute():
        print("Initializing Command execution")
        print()

        print(">>> screen = Screen(\"Hello World\")")
        screen = Screen("Hello World")

        print(">>> screen.__str__()")
        print(screen.__str__())

        print(">>> cut = CutCommand(screen, start=5, end=11)")
        cut = CutCommand(screen, start=5, end=11)

        print(">>> client = ScreenInvoker()")
        client = ScreenInvoker()

        print(">>> client.store_and_execute(cut)")
        client.store_and_execute(cut)

        print(">>> screen.__str__()")
        print(screen.__str__())

        print(">>> paste = PasteCommand(screen, offset=0)")
        paste = PasteCommand(screen, offset=0)

        print(">>> client.store_and_execute(paste)")
        client.store_and_execute(paste)

        print(">>> screen.__str__()")
        print(screen.__str__())

        print(">>> client.undo_last()")
        client.undo_last()

        print(">>> screen.__str__()")
        print(screen.__str__())

        print(">>> client.undo_last()")
        client.undo_last()

        print(">>> screen.__str__()")
        print(screen.__str__())
# endregion


# region Interpreter
class InterpreterExecution:

    @staticmethod
    def execute():
        print("Initializing Interpreter execution")
        print()

        print(">>> john = TerminalExpression(\"John\")")
        john = TerminalExpression("John")
        print(">>> henry = TerminalExpression(\"Henry\")")
        henry = TerminalExpression("Henry")
        print(">>> mary = TerminalExpression(\"Mary\")")
        mary = TerminalExpression("Mary")
        print(">>> sarah = TerminalExpression(\"Sarah\")")
        sarah = TerminalExpression("Sarah")

        print(">>> # Construct the rule sarah and (mary or (john and henry))")
        # Construct the rule sarah and (mary or (john and henry))

        print(">>> rule1 = AndExpression(john, henry)")
        rule1 = AndExpression(john, henry)
        print(">>> rule2 = OrExpression(mary, rule1)")
        rule2 = OrExpression(mary, rule1)
        print(">>> rule3 = AndExpression(sarah, rule2)")
        rule3 = AndExpression(sarah, rule2)

        print(">>> rule3.interpret(\"Sarah\")")
        print(rule3.interpret("Sarah"))
        print(">>> rule3.interpret(\"Sarah Mary\")")
        print(rule3.interpret("Sarah Mary"))
        print(">>> rule3.interpret(\"Sarah John\")")
        print(rule3.interpret("Sarah John"))
        print(">>> rule3.interpret(\"Sarah John Henry\")")
        print(rule3.interpret("Sarah John Henry"))
# endregion


# region State
class StateExecution:

    @staticmethod
    def execute():
        print("Initializing State execution")
        print()

        print(">>> computer = Computer()")
        computer = Computer()
        print(">>> computer.state.__str__()")
        print(computer.state.__str__())

        print(">>> computer.change(On)")
        computer.change(On)
        print(">>> computer.change(Suspend)")
        computer.change(Suspend)
        print(">>> computer.change(Hibernate)")
        computer.change(Hibernate)
        print(">>> computer.change(On)")
        computer.change(On)
        print(">>> computer.change(Off)")
        computer.change(Off)
# endregion


# region ChainOfResponsibility
class ChainOfResponsibilityExecution:

    @staticmethod
    def execute():
        print("Initializing Chain Of Responsibility execution")
        print()

        print(">>> garage_handler = OilHandler(FuelHandler(WaterHandler))")
        garage_handler = OilHandler(FuelHandler(WaterHandler()))

        print(">>> car1 = Car(\"My Car 1\", 1, 1, 1)")
        car1 = CarChain("My Car 1", 1, 1, 1)
        print(">>> garage_handler.handle_request(car1)")
        garage_handler.handle_request(car1)

        print(">>> car2 = Car(\"My Car 2\", 5, 5, 5)")
        car2 = CarChain("My Car 2", 5, 5, 5)
        print(">>> garage_handler.handle_request(car2)")
        garage_handler.handle_request(car2)

        print(">>> car3 = Car(\"My Car 3\", 10, 10, 10)")
        car3 = CarChain("My Car 3", 10, 10, 10)
        print(">>> garage_handler.handle_request(car3)")
        garage_handler.handle_request(car3)
# endregion


# region Observer
class ObserverExecution:

    @staticmethod
    def execute():
        print("Initializing Observer execution")
        print()

        print(">>> really_big_company = Observable()")
        really_big_company = Observable()

        print(">>> american_observer = AmericanStockMarket()")
        american_observer = AmericanStockMarket()
        print(">>> european_observer = EuropeanStockMarket()")
        european_observer = EuropeanStockMarket()

        print(">>> really_big_company.register(american_observer)")
        really_big_company.register(american_observer)
        print(">>> really_big_company.register(european_observer)")
        really_big_company.register(european_observer)

        print(">>> really_big_company.update_observers(\"important_update\", msg=\"CEO unexpectedly resigns\")")
        really_big_company.update_observers("important_update", msg="CEO unexpectedly resigns")
# endregion


# region Strategy
class StrategyExecution:

    @staticmethod
    def execute():
        print("Initializing Strategy execution")
        print()

        print(">>> prime_finder = PrimeFinderClient(50)")
        prime_finder = PrimeFinderClient(50)
        print(">>> prime_finder.get_primes()")
        prime_finder.get_primes()

        print(">>> prime_finder = PrimeFinderClient(100)")
        prime_finder = PrimeFinderClient(100)
        print(">>> prime_finder.get_primes()")
        prime_finder.get_primes()
# endregion


# region Memento
class MementoExecution:

    @staticmethod
    def execute():
        print("Initializing Memento execution")
        print()
        # Test Memento and Command
        print(">>> data = Data()")
        data = Data()
        print(">>> repeats = 10")
        repeats = 10

        print(">>> for i in range(repeats)")
        print("...     data.save()")
        print("...     data.numbers.append(i)")
        print("...")
        for i in range(repeats):
            data.save()
            data.numbers.append(i)

        print(">>> data.save()")
        data.save()
        print(">>> data.numbers")
        print(data.numbers)

        print(">>> for i in range(repeats)")
        print("...     data.undo())")
        print("...     print(data.numbers)")
        print("...")
        for i in range(repeats):
            data.undo()
            print(data.numbers)
# endregion


# region Template
class TemplateExecution:

    @staticmethod
    def execute():
        print("Initializing Template execution")
        print()

        print(">>> pizza = MakePizza()")
        pizza = MakePizza()
        print(">>> pizza.go(5)")
        pizza.go(5)
        print(">>> pizza.go(2)")
        try:
            pizza.go(2)
        except Exception as e:
            print(str(e))

        print(">>> cake = MakeCake()")
        cake = MakeCake()
        print(">>> cake.go(3)")
        cake.go(3)
        print(">>> cake.go(1)")
        try:
            cake.go(1)
        except Exception as e:
            print(str(e))
# endregion
