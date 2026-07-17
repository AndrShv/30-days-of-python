experiments = [
    ("CNN_Base", 120, "Success"),
    ("ResNet_v1", 450, "Success"),
    ("MobileNet", 300, "Failed"),
    ("CNN_Base", 115, "Success"),
    ("ResNet_v1", 460, "Success"),
    ("MobileNet", 280, "Success"),
    ("Transformer_X", 1000, "Success"),
    ("Transformer_X", 950, "Failed"),
]
filtered_experiments = []


def filter_experiments_by_status(experiments, target_status):
    for model, time, status in experiments:
        if status == target_status:
            filtered_experiments.append((model, time, status))
    return filtered_experiments


def filter_experiments_by_model_and_success(experiments, model_name, status):
    filtered_experiments = []
    for x in experiments:
        if x[0] == model_name and x[2] == status:
            filtered_experiments.append(x)
    return filtered_experiments


def find_avg_time_for_all_models(experiments):
    exp_length = len(experiments)
    sum_time = sum(time[1] for time in experiments)
    avg_time = sum_time / exp_length if exp_length > 0 else 0
    return avg_time


# 1. Сначала вызываем вашу первую функцию, чтобы наполнить списки:
filter_experiments_by_status(
    experiments, "Success"
)  # Второй аргумент пока не используется внутри функции, но мы передаем его

print("--- Задание 1 & 2 (Списки успешных/неуспешных) ---")
print("Filtered Experiments:", filtered_experiments)
print()  # Просто пустая строка для красоты в консоли


# 2. Теперь вызываем вторую функцию и сразу печатаем то, что она вернула:
print("--- Задание 3 (Фильтр по модели и статусу) ---")

resnet_success = filter_experiments_by_model_and_success(
    experiments, "ResNet_v1", "Success"
)
print("Успешные ResNet_v1:", resnet_success)

transformer_failed = filter_experiments_by_model_and_success(
    experiments, "Transformer_X", "Failed"
)
print("Упавшие Transformer_X:", transformer_failed)


# 3. Теперь вызываем третью функцию и сразу печатаем то, что она вернула:
print("--- Задание 4 (Среднее время для всех моделей) ---")
avg_time = find_avg_time_for_all_models(experiments)
print("Среднее время для всех моделей:", avg_time)
