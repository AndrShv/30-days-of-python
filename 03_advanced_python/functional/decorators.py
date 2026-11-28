import time
from functools import wraps


def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Заняло {end - start} секунд")
        return result
    return wrapper

@timer_decorator
def heavy_request():
    print("Начался тяжелый запрос к датчикам...")
    time.sleep(1.5)
    print("Данные получены!")


heavy_request()

class Logger:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        print(f"Вызов функции {self.func.__name__} с аргументами: {args}, {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"Функция {self.func.__name__} завершила работу")
        return result

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__class__(self.func.__get__(instance, owner))
@Logger
def add(a, b):
    return a + b

print(add(2, 3))




class Repeat:
    def __init__(self, num_times=1):
        self.num_times = num_times

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(self.num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(num_times=3)
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")

