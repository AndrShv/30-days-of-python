unique_ids = {101, 102, 103, 101}  # Дубликат 101 автоматически удалится
print("OLD:", unique_ids)  # {101, 102, 103}


unique_ids.add(104)
print("NEW:", unique_ids)  # {101, 102, 103, 104}


# Быстрое удаление дубликатов из списка
dirty_list = [1, 2, 2, 3, 3, 3]
clean_list = list(set(dirty_list))  # [1, 2, 3]

if 104 in unique_ids:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
