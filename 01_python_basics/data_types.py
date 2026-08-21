print(type(10))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("Java to Python"))  # <class 'str'> (строки)
print(type(True))  # <class 'bool'> (Важно: Пишется с большой буквы!)


print(type([1, 2, 3]))  # <class 'list'> (динамический массив / список)

print(type(("a", "b", "c")))
# <class 'tuple'> (кортеж / неизменяемый список)
print(
    type(
        {
        "name": "John",
         "age": 30,
         "plan": "Learn Python"
         }
    )
)  # <class 'dict'> (Словарь / аналог HashMap)


list_words = ["Python ", "is ", "awesome!"]
print(" ".join(list_words))