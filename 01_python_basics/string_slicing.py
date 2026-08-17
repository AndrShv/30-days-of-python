language = "Python"

# Срезы:
print(language[0:2])  # "Py" (символы на индексах 0 и 1)
print(language[2:])  # "thon" (от 2-го индекса и до самого конца)
print(language[:2])  # "Py" (с начала и до 2-го индекса)
print(language[-1])  # "n" (последний символ! Отрицательные индексы идут с конца)
print(language[-3:])  # "hon" (последние 3 символа)

# Шаг (step):
print(language[::2])  # "Pto" (каждый второй символ)
print(
    language[::-1]
)  # "nohtyP" (строка задом наперед — в Java для этого нужен StringBuilder.reverse())
