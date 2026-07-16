user = {"username": "andrshv", "role": "developer", "experience": 3}

# 1. Безопасное чтение через .get() — если ключа нет, вернет None (или дефолт), а не упадет
email = user.get("email")  # Вернет None
email = user.get("email", "n/a")
username = user.get("username")

print(f"Email: {email}, Username: {username}")


# 2. Добавление и обновление
user["experience"] = 4  # Обновили существующий
user["status"] = "active"  # Создали новый

for key, value in user.items():
    print(f"{key}: {value}")
