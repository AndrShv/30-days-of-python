# Запись в файл
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Привет из Python!")

# Чтение из файла
with open("report.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
