user_data = ["Andrey", "Odesa", "Ukrane", "Developer"]

# Обычная распаковка
name, city, country, job = user_data
print(name)  # Andrey
print(city)  # Odesa
print(country)  # Ukrane
print(job)  # Developer

first, *middle, last = user_data
print(first)  # Andrey
print(middle)  # ['Odesa', 'Ukrane'] (все элементы между первым и последним)
print(last)  # Developer

# Продвинутая распаковка с использованием оператора * (захватывает остаток в список)
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)  # 1
print(middle)  # [2, 3, 4] (все элементы между первым и последним)
print(last)  # 5
