import pytest


# --- HAPPY PATHS (Успешные сценарии) ---

def test_create_incident_success(client):
    """Тест успешного создания инцидента."""
    response = client.post(
        "/incident/new",
        json={
            "title": "Утечка газа",
            "incident_category": "emergency",  # <-- маленькими буквами (.value)
            "law_breaking_category": "sth_else"  # <-- маленькими буквами (.value)
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Утечка газа"
    assert "id" in data


def test_get_incident_by_id_success(client):
    """Тест получения конкретного инцидента по его ID."""
    # 1. Создаем запись
    create_res = client.post(
        "/incident/new",
        json={
            "title": "Превышение скорости",
            "incident_category": "accident",  # <-- маленькими буквами
            "law_breaking_category": "speed_violation"  # <-- маленькими буквами
        }
    )
    assert create_res.status_code == 201
    incident_id = create_res.json()["id"]

    # 2. Запрашиваем по ID
    response = client.get(f"/incident/{incident_id}")
    assert response.status_code == 200
    assert response.json()["id"] == incident_id
    assert response.json()["title"] == "Превышение скорости"


def test_get_all_incidents_empty_and_populated(client):
    """Тест получения списка: сначала пустого, затем с элементами."""
    # 1. Проверяем, что изначально список пуст
    empty_res = client.get("/incident/all")
    assert empty_res.status_code == 200
    assert empty_res.json() == []

    # 2. Добавляем один инцидент
    create_res = client.post(
        "/incident/new",
        json={
            "title": "Пожар",
            "incident_category": "fire",  # <-- маленькими буквами
            "law_breaking_category": "sth_else"
        }
    )
    assert create_res.status_code == 201

    # 3. Проверяем, что теперь список содержит 1 элемент
    populated_res = client.get("/incident/all")
    assert populated_res.status_code == 200
    assert len(populated_res.json()) == 1


# --- CORNER CASES & VALIDATION (Крайние случаи и валидация) ---

def test_get_incident_not_found(client):
    """Тест получения несуществующего инцидента (ожидаем 404)."""
    random_id = "non-existent-uuid-12345"
    response = client.get(f"/incident/{random_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Инцидент не найден"


def test_create_incident_invalid_enum(client):
    """Тест отправки невалидного значения Enum (ожидаем 422 Unprocessable Entity)."""
    response = client.post(
        "/incident/new",
        json={
            "title": "НЛО над городом",
            "incident_category": "alien_attack",  # Несуществующая категория
            "law_breaking_category": "sth_else"
        }
    )
    assert response.status_code == 422


def test_create_incident_missing_field(client):
    """Тест отправки запроса без обязательного поля title (ожидаем 422)."""
    response = client.post(
        "/incident/new",
        json={
            "incident_category": "fire"
        }
    )
    assert response.status_code == 422