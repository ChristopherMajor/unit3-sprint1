#acme.py/products.py
import random

class product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, 
                 indentifier=(random.randint(1000000, 9999999))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.indentifier = indentifier

    def stealability(self):
        stealability = self.price/self.weight
        if stealability < .5:
            print('not so stealable.')
        elif stealability >= .5 and stealability < 1:
            print('kinda stealable.')
        else:
            print('very stealable!')
            
    def explode(self):
        explodability = self.flammability * self.weight
        if explodability < 10:
            print('fizzle...')
        elif explodability >= 10 and explodability < 50:
            print('...boom!')
        else:
            print('...BABOOM!')

class BoxingGlove(product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, 
                 indentifier=(random.randint(1000000, 9999999))):
        super().__init__(name, price, weight, flammability, indentifier)

    def explode(self):
        print('...its a glove.')
    
    def punch(self):
        punchy = self.weight
        if punchy < 5:
            print('that tickles.')
        elif punchy >= 5 and punchy < 15:
            print('hey that hurt!')
        else:
            print('OUCH!')



# if __name__ == '__main__':
#     toy = product('A Cool Toy')
#     print(toy.name)
#     print(toy.indentifier)


    
