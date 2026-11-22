import numpy as np

def_py_list = [1,2,3,4,5,6]
numpy_list = np.array([1,2,3,4,5,6])


print(f"Default Python List is: {def_py_list}")
print(f"Numpy List is: {numpy_list}")
print(f"Default Python type is: {type(def_py_list)}")
print(f"Numpy List is: {type(numpy_list)}")


edited_numpy_list = numpy_list+10
print(f"Edited NumPy List is {edited_numpy_list}")
