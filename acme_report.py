from products import product
import random

def generate_products(num_products=30):
    adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap']
    products = []
    name= (random.sample(adjectives, 1) + random.sample(nouns, 1))

    return name
