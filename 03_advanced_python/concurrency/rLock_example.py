import threading
rlock = threading.RLock()

def outer_function():
    with rlock:
        print("Вошли во внешнюю функцию")
        inner_function()

def inner_function():
    with rlock:
        print("Вошли во внутреннюю функцию")

outer_function()