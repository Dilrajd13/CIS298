class pizza:
    def __init__(self, size="",toppings = [], base_cost = float, cost_per_topping = float, number_of_toppings_included = 0):
        self.size = size
        self.toppings = toppings
        self.base_cost = base_cost
        self.cost_per_topping = cost_per_topping
        self.number_of_topping_included= number_of_toppings_included

    def add_topping(self, topping : str):
        self.toppings.append(topping)

    def get_total_cost(self):
        if len(self.toppings) > self.number_of_topping_included:
            one = (len(self.toppings) - self.number_of_topping_included)

            return self.base_cost + (one * self.cost_per_topping)

        else:
            return self.base_cost
