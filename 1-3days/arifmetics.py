# --- Арифметика ---
a = 5
b = 3

print(a + b)  # 8  (Сложение)
print(a * b)  # 15  (Умножение)
print(
    a / b
)  # 1.6666666666666667 (Деление — ВСЕГДА возвращает float, даже если делится нацело!)
print(a**b)  # 125  (Возведение в степень: 5 во 3-й степени. )
print(a // b)  # 1  (Целочисленное деление: отбрасывает дробную часть)
print(a % b)  # 2  (Остаток от деления / Modulus)


x = True
y = False

print(x and y)  # False (Логическое И)
print(x or y)  # True (Логическое ИЛИ)
print(not x)  # False (Логическое НЕ)


print(3 == "3")  # False (в отличие от JS, Python строго разделяет типы)


list_one = [1, 2]
list_two = [1, 2]
print(list_one == list_two)  # True (значения одинаковые)
print(list_one is list_two)  # False (объекты в памяти разные)
