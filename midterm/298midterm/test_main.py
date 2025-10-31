import unittest
from unittest import TestCase
from main import pizza
class Testpizza(TestCase):
    def test_add_topping_none(self):
        one = pizza(size="mini", toppings=[], base_cost=7, cost_per_topping = 1, number_of_toppings_included = 2)
        #no toppings so just 7
        self.assertEqual(one.get_total_cost(), 7)

    def test_topping_under_includedtops(self):
        one = pizza(size="mini", toppings=[], base_cost=7, cost_per_topping=1, number_of_toppings_included=2)
        one.add_topping("PINAPPLE")
        # allowed 2 toppings for free so still 7
        self.assertEqual(one.get_total_cost(), 7)

    def test_top_eql_includedtops(self):
        one = pizza(size="mini", toppings=[], base_cost=7, cost_per_topping=1, number_of_toppings_included=2)
        one.add_topping("PINAPPLE")
        one.add_topping("Plants")
        # allowed 2 toppings for free so still 7
        self.assertEqual(one.get_total_cost(), 7)
    def test_over_includedtops(self):
        one = pizza(size="mini", toppings=[], base_cost=7, cost_per_topping=1, number_of_toppings_included=2)
        one.add_topping("PINAPPLE")
        one.add_topping("Plants")
        one.add_topping("Pepper")

        # should be 8 because each topping worth 1 currency
        self.assertEqual(one.get_total_cost(), 8)

if __name__ == "__main__":
    unittest.main()