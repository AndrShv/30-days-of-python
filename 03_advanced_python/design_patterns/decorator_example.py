class Coffee:
    price: float = 100
    def coffee_price(self) -> float:
        return self.price

class MilkCoffee(Coffee):
    def coffee_price(self) -> float:
        return super().coffee_price()*1.2

class ChocolateCoffee(Coffee):
    def coffee_price(self) -> float:
        return super().coffee_price()*1.5



my_def_coffee = Coffee()
print(my_def_coffee.coffee_price())

my_milk_coffee = MilkCoffee()
print(my_milk_coffee.coffee_price())

my_chocolate_coffee = ChocolateCoffee()
print(my_chocolate_coffee.coffee_price())

