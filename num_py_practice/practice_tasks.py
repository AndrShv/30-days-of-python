import numpy as np



# Задача 1. Создание и изменение формы (arange, reshape)
# 1) Создай одномерный массив из чисел от 1 до 16 включительно.
# 2) Преврати его в двумерную матрицу размером (4 * 4)
# 3) Выведи матрицу и её транспонированную версию (.T).
arr = np.arange(1,17)
print(f"arr: {arr}")

reshaped_matrix = np.reshape(arr, (4,4))
print(f"reshaped: {reshaped_matrix}")

transposed_matrix = reshaped_matrix.T
print(f"transposed_matrix: {transposed_matrix}")


# Задача 2. Срезы и фильтрация (Slicing & Boolean indexing)
# 1) Выведи каждый третий элемент массива (начиная с первого).
# 2) Выведи только те числа из массива, которые делятся на 4 без остатка (% 4 == 0).
# 3) Замени все числа, которые больше 15, на 0 (подсказка: можно использовать arr[arr > 15] = 0).
arr = np.arange(1,21)
print(f"arr: {arr}")
print(f"Every 3rd elem: {arr[::3]}")
print(f"Every elem % 4: {arr[arr % 4 == 0]}")

arr[arr > 15] = 0
print(f"Elements which are bigger than 15: {arr}")



# Задача 3. Статистика по осям (axis=0 и axis=1)
# 1) Найди общую сумму всех элементов матрицы.
# 2) Найди минимальное значение в каждом столбце (axis=0).
# 3) Найди среднее значение в каждой строке (axis=1).
matrix_def = np.random.randint(1,10, (3,3))
print(f"matrix_def: \n {matrix_def}")
sum_matrix = np.sum(matrix_def)
print(f"sum_matrix: {sum_matrix}")
min_val_in_each_column = np.min(matrix_def, axis=0)
print(f"min_val_in_each_column: {min_val_in_each_column}")
avg_matrix = np.mean(matrix_def, axis=1)
print(f"avg_matrix: {avg_matrix}")



# Задача 4. Поиск и уникальные значения (unique, where, argmax)
# 1) Выведи все уникальные оценки без повторений.
# 2) Найди индексы (позиции) всех пятёрок в массиве с помощью np.where.
# 3) Найди индекс первого самого высокого элемента через np.argmax.
grades = np.array([4, 5, 3, 5, 2, 4, 5, 3, 2, 5])
unique_nums = np.unique(grades)
print(f"Unique values: {unique_nums}")
find_index = np.where(grades == 5)
print(f"find_index: {find_index}")
find_max_value = np.argmax(grades)
print(f"find_max_value: {find_max_value}")




