import numpy as np


arr  = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(f"Just Array: {arr}")
print(f"First elem: {arr[0]}")
print(f"Last elem: {arr[-1]}")
print(f"Elem from 1 to 3: {arr[1:4]}")
print(f"Elem from 2 to 10 with step 2: {arr[2:10:2]}") #
print(f"Every other elem: {arr[::2]}") #берет каждый второй элемент, начиная с 0 индекса


matrix_2d = np.array(
    [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18]
    ]
)


# Slicing 2D matrix indexing
print(f"Matrix 2d array: \n {matrix_2d}")
print(f"First row: {matrix_2d[0]}")
print(f"Last row: {matrix_2d[-1]}")
print(f"Second row: {matrix_2d[1]}")
print(f"Second row from 2 to 4 elem: {matrix_2d[1, 2:4]}")
print(f"First 2 rows and 3rd columns: {matrix_2d[0, 2:3]}, {matrix_2d[1, 2:3]}")




# Boolean indexing
print(f"Nums are bigger than 5: {matrix_2d[matrix_2d > 5]}" )
print(f"Even numbers: {matrix_2d[matrix_2d % 2 == 0]}")