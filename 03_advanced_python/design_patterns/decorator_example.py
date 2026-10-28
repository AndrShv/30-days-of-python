class Coffee:
    price: float = 100
    def coffee_price(self) -> float:
        return self.price


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee


class Milk(CoffeeDecorator):
    def coffee_price(self) -> float:
        return self.coffee.coffee_price() * 1.2


class Chocolate(CoffeeDecorator):
    def coffee_price(self) -> float:
        return self.coffee.coffee_price() * 1.5

class Caramel(CoffeeDecorator):
    def coffee_price(self) -> float:
        return self.coffee.coffee_price() * 1.6


# --- Проверяем работу ---

# 1. Обычный черный кофе
my_def_coffee = Coffee()
print(f"Черный кофе: {my_def_coffee.coffee_price()}")  # 100

# 2. Кофе с молоком (оборачиваем черный кофе в Milk)
my_milk_coffee = Milk(my_def_coffee)
print(f"Кофе с молоком: {my_milk_coffee.coffee_price()}")  # 120.0

# 3. Кофе с шоколадом (оборачиваем черный кофе в Chocolate)
my_chocolate_coffee = Chocolate(my_def_coffee)
print(f"Кофе с шоколадом: {my_chocolate_coffee.coffee_price()}")  # 150.0


# 4. Кофе с карамелью (оборачиваем черный кофе в Chocolate)
my_caramel_coffee = Caramel(my_def_coffee)
print(f"Кофе с карамелью: {my_caramel_coffee.coffee_price()}")
