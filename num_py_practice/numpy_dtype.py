import numpy as np


arr_int = np.array([1, 2, 3, 4, 5])
arr_float = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
arr_mixed = np.array([1, 2.5, 3.2, 4])

print(f"Integer: {arr_int.dtype}")
print(f"Float: {arr_float.dtype}")
print(f"Mixed: {arr_mixed.dtype}")

arr_int_into_32_int = arr_int.astype(np.int32)
print(f"Integer of arr_int_into_32_int: {arr_int_into_32_int.dtype}")
print("Memory Usage: int32/float32 = 4 bytes, int64/float64 = 8 bytes per element!")