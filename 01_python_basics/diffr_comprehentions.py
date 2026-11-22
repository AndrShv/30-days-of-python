
# List Comprehension
numbers = [1, 2, 3, 4, 5, 6]
squares_even = [x ** 2 for x in numbers if x % 2 == 0]
print(squares_even)
print(squares_even[2])
print(squares_even[-1])

#  Dict Comprehension
numbers = [1, 2, 3, 4]
sq_dict = {x: x ** 2 for x in numbers}
print(sq_dict.get(2, "пусто"))

# Set Comprehension
text = "hello world"
vowels = {char for char in text if char in 'aeiou'}
print(vowels)
# Способ 1: Превратить в список (если нужен индекс, но порядок случайный)
vowels_list = list(vowels)
one_char = vowels_list[0]
# Способ 2: Извлечь и удалить случайный элемент
discarded = vowels.pop()

# Generator Expression
numbers = [1, 2, 3, 4, 5, 6]
gen = (x ** 2 for x in numbers)

print(gen)
print(next(gen)) # 1
print(next(gen)) # 4 (2**2)
print(next(gen)) # 9 (3**2)

for val in gen:
    print(val)





