import numpy as np

arr = np.arange(12)
print("Original 1D array:", arr)

# Reshape меняет форму (представление) массива, не копируя данные
reshaped = arr.reshape(3, 4)  # Общий размер должен совпадать (3 * 4 = 12): 3 строки по 4 элемента
print("\nReshaped to 3x4:")
print(reshaped)

# Flatten преобразует многомерный массив обратно в одномерный (1D)
flattened = reshaped.flatten()
print("\nFlattened:", flattened)

# Reshape с -1 (автоматический расчёт размерности)
auto_reshape = arr.reshape(2, -1)  # -1 означает "посчитай количество столбцов в каждой строке автоматически"
print("\nAuto reshape (2 rows, auto columns):")
print(auto_reshape)


matrix_2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(f"Original: \n{matrix_2d}")
print(f"Transposed: \n{matrix_2d.T}")

a = np.array(
    [
        [1,2],
        [3,4]
    ]
)

b = np.array(
    [
        [5,6],
        [7,8]
    ]
)


print("\n--- Concatenation ---")
print("Array a:\n", a)
print("Array b:\n", b)
print(f"Vertical Concatenation (vstack): \n {np.vstack((a,b))}")
print(f"Horizontal Concatenation (hstack): \n {np.hstack((a,b))}")
print("Concatenation implementation: ")
print(f"Vertical Concatenation: \n {np.concatenate((a, b), axis=0)}") # axis=0 для Vertical
print(f"Horizontal Concatenation: \n {np.concatenate((a, b), axis=1)}") # axis=1 для Horizontal
