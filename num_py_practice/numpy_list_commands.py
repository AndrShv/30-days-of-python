

import numpy as np

# Method 1: np.array()
# Создает numpy list
numpy_list_1 = np.array([1, 2, 3, 4, 5, 6])
print(f"numpy_list created by array() method{numpy_list_1}")

# Method 3: np.arrange().
# Такой же метод как и range(list) (start, stop, step)
numpy_list_2 = np.arange(10, 0, -1)
print(f"numpy_list created by arrange() method{numpy_list_2}")

# Method 3: np.linspace().
# Делит отрезок от start до stop и разбивает его на колличество num точек
# Точек всегда на 1 больше, чем число num
numpy_list_3 = np.linspace(0, 10, 5)
print(f"numpy_list created by linspace() method{numpy_list_3}")


# Method 4: np.zeros()
# Создает numpy list из 0; 10 - размер(не включая 10), float - тип данных
numpy_list_4 = np.zeros(10, float)
print(f"numpy_list created by fill() method{numpy_list_4}")









