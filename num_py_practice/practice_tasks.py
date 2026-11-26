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




# Задача 5. Объединение массивов (vstack, hstack)
# 1) Первую заполни нулями (np.zeros, тип int).
# 2) Вторую заполни единицами (np.ones, тип int).
# 3) Склей их по вертикали (чтобы получилась матрица 4*2)
# 4) Склей их по горизонтали (чтобы получилась матрица 2*4)

a = np.zeros((2,2), int)
b = np.ones((2,2), int)
print(f" a: \n {a};\n b: \n {b}")
a_v_b = np.vstack((a,b))
a_h_b = np.hstack((a,b))
print(f"a_v_b: \n {a_v_b}")
print(f"a_h_b: \n {a_h_b}")

# Задача 6. Векторы и поэлементные операции
# 1) Умножь каждый элемент v1 на 10 и прибавь к нему v2.
# 2) Найди скалярное произведение векторов v1 и v2 (np.dot).

v1 = np.array([2, 4, 6])
v2 = np.array([1, 3, 5])
new_v1 = v1*10 + v2
print(f"new v1 vector: {new_v1}")
print(f"Scalar of vectors: {np.dot(v1, v2)}" )


M = np.array([
    [1, 3],
    [2, 4]
])
print(f"Definition: \n {np.linalg.det(M)}")
print(f"Inversion: \n {np.linalg.inv(M)}")
print(f"M @ M: \n {M @ M}")




