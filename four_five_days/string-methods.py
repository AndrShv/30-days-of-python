text = "   Python for ML, Java, Go   "

# 1. Удаление пробелов по краям (аналог .trim() в Java)
print(text.strip())  # "Python for ML, Java, Go"

# 2. Разделение строки (аналог .split())
technologies = text.strip().split(", ")
print(technologies)  # ['Python for ML', 'Java', 'Go']

# 3. Объединение списка в строку с разделителем (в Java это String.join())
joined_text = " ->> ".join(technologies)
print(joined_text)  # "Python for ML ->> Java ->> Go"
