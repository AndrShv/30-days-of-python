
# List Comprehension
numbers = [1, 2, 3, 4, 5, 6]
squares_even = [x ** 2 for x in numbers if x % 2 == 0]
print(squares_even)

#  Dict Comprehension
numbers = [1, 2, 3, 4]
sq_dict = {x: x ** 2 for x in numbers}
print(sq_dict)

# Set Comprehension
text = "hello world"
vowels = {char for char in text if char in 'aeiou'}
print(vowels)

# Generator Expression
numbers = [1, 2, 3, 4, 5, 6]
gen = (x ** 2 for x in numbers)

print(gen)
print(next(gen)) # 1
print(next(gen)) # 4 (2**2)
print(next(gen)) # 9 (3**2)

for val in gen:
    print(val)





