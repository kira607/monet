from datetime import datetime


class Shop:
    def __init__(self, name):
        pass


class Measure:
    def __init__(self, name):
        pass


class Product:
    def __init__(self):
        self.name = 'Product'
        self.shop = Shop(None)
        self.price = 0.0

        self.make_date = datetime.now()
        self.due_date = None

        self.amount = 0
        self.measure = Measure(None)


class Ingridient:
    def __init__(self):
        self.name = 'Ingridient'


class Dish:
    pass


class Eating:
    def __init__(self):
        self.dishes = []
        self.products = []


def main():
    pass


if __name__ == '__main__':
    main()
