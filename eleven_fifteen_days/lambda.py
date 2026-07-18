add = lambda x, y: x + y
print(add(5, 3))  # 8


temps = [20, 26, 19, 32]
# Увеличиваем каждую температуру на 1 градус

filtered_temps = map(lambda t: t+1, temps)
print(list(filtered_temps))
hot = filter(lambda t: t > 25, temps)
print(list(hot))