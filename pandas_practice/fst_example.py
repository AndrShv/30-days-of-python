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
