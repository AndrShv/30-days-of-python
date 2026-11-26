import numpy as np

a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)
b = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)
print(f"Matrix a: \n {a}")
print(f"Matrix b: \n {b}")
# Поэлементное умножение (каждый элемент умножается на элемент на той же позиции, НЕ матричное умножение)
print(f"\nElement-wise multiplication (a * b): {a*b}")


# Скалярное произведение векторов (попарно перемножаем элементы и складываем результаты)
v1 = np.array(
    [1, 2, 3]
)
v2 = np.array(
    [4, 5, 6]
)
print(f"\nDot product of vectors {v1} and {v2}: {np.dot(v1, v2)}")




matrix = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)
print("\n--- Matrix Properties ---")
print("Matrix:")
print(matrix)
print (f"Determinant: {np.linalg.det(matrix)}") # 1*4, 2*3 -> 4-6 = -2

#Элементы на главной диагонали меняются местами,
# у побочной меняются знаки, и всё делится на определитель (-2):
print (f"Inverse: {np.linalg.inv(matrix)}")


# «Переворачивает» матрицу: строки становятся столбцами, а столбцы — строками.
print (f"Transpose: {matrix.T}")


# Eigenvalues and eigenvectors
eigenvals, eigenvecs = np.linalg.eig(matrix)
print(f"\nEigenvalues: {eigenvals}")
print (f"Eigenvectors:\n{eigenvecs}")