import pandas as pd

new_data_frame = pd.DataFrame()

data = pd.read_csv('orders.csv')

# .head() Выводит первые 5 значений
print(data.head())
# .tail() Выводит последние 5 значений
print(data.tail())
# .info() выводит информацию о файле
print(data.info())
# .describe() выводит статиску
print(data.describe())
# .columns выводит список столбиков и их тип
print(data.columns)
# .index выодит start, stop, step о index в табличке
print(data.index)

# Считает общее количество строк (записей) в столбце "city" (результат: 100)
print(len(data["city"]))

# Находит и выводит массив всех уникальных городов без повторений
print(f"Unique cities: \n {data['city'].unique()}")

# Выбирает и выводит только два указанных столбца (двойные скобки нужны для передачи списка названий)
print(f"City and Products: \n {data[['city', 'product']]}")

# Берет первую строку (индекс 0) и преобразует её в обычный горизонтальный список Python без названий столбцов
print(f"1st Line: \n{list(data.iloc[0])}")

# Выводит конкретную ячейку: 1-я строка (индекс 0) и 4-й столбец по счёту (индекс 3 — город)
print(f"1st Line and 4th column: \n{data.iloc}")
print(f"1st Line and City(4th) column: \n{data.iloc[0]["city"]}")

# Делает срез и выводит первые 3 строки таблицы целиком (с индексами 0, 1 и 2)
print(f"First 3 lines: \n{data.iloc[0:3]}")

print(f"Accessories with Discount > 150: \n{data[(data['total_amount'] > 150) & (data['category'] == 'Аксессуары')]}")
print(f"Products with total_amount > 200 and order_date between 2026-01-09 and 2026-01-27:\n {
data[
    (data["product"] == "Смартфон") & 
    (data["total_amount"] > 200) &
    (data["order_date"].between("2026-01-09", "2026-01-27"))
]}")



