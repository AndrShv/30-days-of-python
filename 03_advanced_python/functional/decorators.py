import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Заняло {end - start} секунд")
    return wrapper

@timer_decorator
def heavy_request():
    print("Начался тяжелый запрос к датчикам...")
    time.sleep(1.5)
    print("Данные получены!")


heavy_request()


