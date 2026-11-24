try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Ошибка деления на ноль: {e}")
except Exception as e:
    print(f"Что-то еще пошло не так: {e}")
finally:
    print("Этот блок выполнится в любом случае")
