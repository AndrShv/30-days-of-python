import numpy as np
print("---Matrix 2D Specs---")
matrix_2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matrix_2d)
print(f"Matrix 2D shape(размер в каждом массииве): {matrix_2d.shape}")
print(f"Matrix 2D dtype(тип данных): {matrix_2d.dtype}")
print(f"Matrix 2D dimension(сколько всего измерений): {matrix_2d.ndim}")
print(f"Matrix 2D size(общее колличество элементов): {matrix_2d.size}")
print("\n")



print("---Matrix 3D Specs---")


matrix_3d = np.array(
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
)

print(matrix_3d)
print(f"Matrix 3D shape(размер в каждом массииве): {matrix_3d.shape}")
print(f"Matrix 3D dtype(тип данных): {matrix_3d.dtype}")
print(f"Matrix 3D dimension(сколько всего измерений): {matrix_3d.ndim}")
print(f"Matrix 3D size(общее колличество элементов): {matrix_3d.size}")



print("\n")


zeros_2d = np.zeros((3,3),int)
print(f"2D zero matrix: {zeros_2d}")

ones_3d = np.ones((3, 3, 3), int)
print(f"3D ones matrix: {ones_3d}")





