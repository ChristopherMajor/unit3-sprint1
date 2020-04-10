# acme.py/products.py
import random


class product():
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.indentifier = random.randint(1000000, 9999999)

    def stealability(self):
        stealability = self.price/self.weight
        if stealability < .5:
            return 'not so stealable.'
        elif stealability >= .5 and stealability < 1:
            return 'kinda stealable.'
        else:
            return 'very stealable!'

    def explode(self):
        explodability = self.flammability * self.weight
        if explodability < 10:
            return 'fizzle...'
        elif explodability >= 10 and explodability < 50:
            return '...boom!'
        else:
            return '...BABOOM!'


class BoxingGlove(product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 indentifier=(random.randint(1000000, 9999999))):
        super().__init__(name, price, weight, flammability, indentifier)

    def explode(self):
        print('...its a glove.')

    def punch(self):
        punchy = self.weight
        if punchy < 5:
            return 'that tickles.'
        elif punchy >= 5 and punchy < 15:
            return 'hey that hurt!'
        else:
            return 'OUCH!'
