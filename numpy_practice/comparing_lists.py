import time
import numpy as np

size = 1_000_000_0

py_list = list(range(size))
numpy_list = np.array(range(size))

print("---Performance Comparison---")
start_for_pylist = time.time()
result_for_pylist = [x+1 for x in py_list]
time_for_pylist = time.time() - start_for_pylist
print(f"Time for Py List is: {time_for_pylist}")


start_for_numpy_list = time.time()
result_for_numpy_list = numpy_list+1
time_for_numpy_list = time.time() - start_for_numpy_list
print(f"Time for NumPy List is: {time_for_numpy_list}")


print(f"NumPy is {time_for_pylist/time_for_numpy_list}x faster!")






