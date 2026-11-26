import numpy as np

arr = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array:", arr)
# Basic statistics
print(f"\n--- Basic Statistics ---")
print(f"Sum: {np.sum(arr)}")
print (f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print (f"Standard deviation: {np.std(arr)}")
print (f"Variance: {np.var(arr)}")
print(f"Min: {np.min(arr)}")
print(f"Max: {np.max(arr)}")
print (f"Index of min: {np.argmin(arr)}")
print(f"Index of max: {np.argmax(arr)}")



# 2D array statistics (with axis parameter)
matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print("\n--- 2D Array Statistics ---")
print("Matrix:")
print(matrix)
print(f"Sum of all elements: {np.sum(matrix)}")
print(f"Sum of each column (axis=0): {np.sum(matrix, axis=0)}")  # Сумма каждого столбца (по вертикали)
print(f"Sum of each row (axis=1): {np.sum(matrix, axis=1)}")     # Сумма каждой строки (по горизонтали)
print(f"Mean of each column (axis=0): {np.mean(matrix, axis=0)}") # Среднее каждого столбца
print(f"Mean of each row (axis=1): {np.mean(matrix, axis=1)}")    # Среднее каждой строки
