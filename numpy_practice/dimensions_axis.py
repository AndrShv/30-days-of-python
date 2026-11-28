import numpy as np

matrix_2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print("Matrix_2D:")
print(matrix_2d)
print(f"Shape: {matrix_2d.shape}\n")

# axis=0: идем СВЕРХУ ВНИЗ (по всем строкам) и «сплющиваем» их в одну итоговую строку.
# Результат — сумма чисел для КАЖДОГО СТОЛБЦА по отдельности.
sum_axis0 = np.sum(matrix_2d, axis=0)  # сумируем по столбикам
print(f"axis=0 (down rows): {sum_axis0} → shape: {sum_axis0.shape}")
print(f" Example: Column 1 sum = "
      f"{matrix_2d[0, 1]} + {matrix_2d[1, 1]} + {matrix_2d[2, 1]} "
      f"= {sum_axis0[1]}\n")

# axis=1: идем СЛЕВА НАПРАВО (по всем столбцам) и «сплющиваем» их в один итоговый столбец.
# Результат — сумма чисел для КАЖДОЙ СТРОКИ по отдельности.
sum_axis1 = np.sum(matrix_2d, axis=1)  # сумируем по рядам
print(f"axis=1 (across columns): \n {sum_axis1} → shape: {sum_axis1.shape}")
print(f" Example: Row 0 sum is"
      f" {matrix_2d[0, 0]} + {matrix_2d[0, 1]} + {matrix_2d[0, 2]} = {sum_axis1[0]}\n")

matrix_3d = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ],
        [
            [13, 14, 15],
            [16, 17, 18]
        ]
    ]
)

print("Matrix_3D:")
print(matrix_3d)
print(f"Shape: {matrix_3d.shape}\n")
# в 3D
# axis=0 — это измерение
# axis=1 — это строки
# axis=2 — это столбцы


# axis=1: идем сверху вниз ПО СТРОКАМ -> получаем сумму каждого СТОЛБЦА внутри миров
sum_axis1_3d = np.sum(matrix_3d, axis=1)
print(f"axis=1 (down rows -> column sums): \n {sum_axis1_3d} -> shape: {sum_axis1_3d.shape}")
print(f"Example: World 0, Column 0 sum is "
      f"{matrix_3d[0, 0, 0]} + {matrix_3d[0, 1, 0]} "
      f" = {sum_axis1_3d[0, 0]}\n")





# axis=2: идем слева направо ПО СТОЛБЦАМ -> получаем сумму каждой СТРОКИ внутри миров
sum_axis2_3d = np.sum(matrix_3d, axis=2)
print(f"axis=2 (across columns -> row sums): \n {sum_axis2_3d} -> shape: {sum_axis2_3d.shape}")
print(f"Example: World 0, Row 0 sum is "
      f"{matrix_3d[0, 0, 0]} + {matrix_3d[0, 0, 1]} + {matrix_3d[0, 0, 2]} "
      f" = {sum_axis2_3d[0, 0]}")



