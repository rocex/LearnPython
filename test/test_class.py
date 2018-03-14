class Calculator(object):
    '''docstring for Calculator'''
    name = 'Good'

    def __init__(self, name, width, hight, weight, price):
        print('__init__', 1, self.name)
        super(Calculator, self).__init__()
        self.name = name
        self.width = width
        self.hight = hight
        self.weight = weight
        self.price = price

        print('__init__', 2, self.name)

    def add(self, x, y):
        z = x + y
        print('add', x, y, z)
        return z

    def minus(self, x, y):
        z = x - y
        print('minus', x, y, z)
        return z

    def times(self, x, y):
        z = x * y
        print('times', x, y, z)
        return z

    def divide(self, x, y):
        z = x / y
        print('divide', x, y, z)
        return z


calculator = Calculator("Bad", 10, 9, 8, 100)

calculator.add(1, 2)
calculator.minus(1, 2)
calculator.times(1, 2)
calculator.divide(1, 2)
