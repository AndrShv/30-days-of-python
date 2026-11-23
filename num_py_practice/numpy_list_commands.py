

import numpy as np

# Method 1: np.array()
# Создает numpy list
numpy_list_1 = np.array([1, 2, 3, 4, 5])
print(f"numpy_list created by array() method: {numpy_list_1}")

# Method 3: np.arrange().
# Такой же метод как и range(list) (start, stop, step)
numpy_list_2 = np.arange(10, 0, -1)
print(f"numpy_list created by arrange() method: {numpy_list_2}")

# Method 3: np.linspace().
# Делит отрезок от start до stop и разбивает его на колличество num точек
# Точек всегда на 1 больше, чем число num
numpy_list_3 = np.linspace(0, 10, 5)
print(f"numpy_list created by linspace() method: {numpy_list_3}")


# Method 4: np.zeros()
# Создает numpy list из 0; 10 - размер(не включая 10), float - тип данных
numpy_list_4 = np.zeros(10, float)
print(f"numpy_list created by zeros() method: {numpy_list_4}")


# Method 5: np.ones()
# Создает numpy list из 1; 10 - размер(не включая 10), float - тип данных
numpy_list_5 = np.ones(10, float)
print(f"numpy_list created by ones() method: {numpy_list_5}")



# Method 6: np.full()
# Создает numpy list из указаных значений; 10 - размер(не включая 10), 3 - зачения которыми заполняется список, float - тип данных
numpy_list_6 = np.full(10, 3, float)
print(f"numpy_list created by fill() method: {numpy_list_6}")



# Method 7: np.eye()
# Создает матрицу; N — это высота (количество строк), а M — ширина (количество столбцов), k — это номер диагонали, на которой будут стоять 1,
numpy_list_7 = np.eye(5,5,0, float)
print(f"numpy_list created by eye() method: \n {numpy_list_7}")

# Method 8: np.random.rand()
# Создает массив указанной формы со случайными числами от 0 (включительно) до 1 (не включительно).
numpy_list_8 = np.random.rand(5)
print(f"numpy_list created by random() method: {numpy_list_8}")


# Method 9: np.random.randint()
# Создает массив со случайными целыми числами в диапазоне [low, high).
# low — нижняя граница (включительно), high — верхняя граница (не включительно), size — размер или форма массива.
numpy_list_9 = np.random.randint(low=1, high=100, size=5)
print(f"numpy_list created by randint() method: {numpy_list_9}")


# Method 10: np.random.uniform()
# Создает массив со случайными дробными числами в диапазоне [low, high).
# low — нижняя граница (включительно), high — верхняя граница (не включительно), size — размер массива.
numpy_list_10 = np.random.uniform(low=10, high=50, size=5)
print(f"numpy_list created by uniform() method: {numpy_list_10}")













