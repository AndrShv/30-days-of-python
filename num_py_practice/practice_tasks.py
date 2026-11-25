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




matrix_def = np.random.randint(1,10, (3,3))
print(f"matrix_def: \n {matrix_def}")

