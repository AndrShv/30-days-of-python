import time

def log_method(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Заняло {end - start} секунд")
    return wrapper
