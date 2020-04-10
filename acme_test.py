import unittest
from products import product
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)

    def test_func(self):
        prod2 = product('test', price=20, weight=20, flammability=2.5)
        self.assertEqual(prod2.explode(), '...BABOOM!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertTrue(len(products) == 30)

    def test_legal_names(self):
        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap']
        for product in generate_products():
            adjective, noun = product.name.split()
            self.assertIn(adjective, adjectives)
            self.assertIn(noun, nouns)

if __name__ == '__main__':
    unittest.main()
