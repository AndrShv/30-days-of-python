from unittest.mock import MagicMock
from fastapi import HTTPException
import pytest

from safecity_platform.api.incident_controller import get_incident, create_incident
from safecity_platform.dto.data_transf_obj import IncidentRequest
from safecity_platform.models.categories import IncidentCategory, LawBreakingCategory


def test_get_incident_unit_not_found():
    """Unit-тест: проверяем логику бросания HTTPException(404) при отсутствии записи."""
    # Создаем фейковую сессию БД
    mock_db = MagicMock()

    # Задаем поведение: db.query().filter().first() возвращает None
    mock_db.query.return_value.filter.return_value.first.return_value = None

    # Вызываем функцию напрямую как обычную Python-функцию (без HTTP-клиента)
    with pytest.raises(HTTPException) as exc_info:
        get_incident(incident_id="fake-id", db=mock_db)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Инцидент не найден"


def test_create_incident_unit_db_calls():
    """Unit-тест: проверяем, что контроллер вызывал db.add(), db.commit() и db.refresh()."""
    mock_db = MagicMock()

    request_data = IncidentRequest(
        title="Тестовый инцидент",
        incident_category=IncidentCategory.ACCIDENT,
        law_breaking_category=LawBreakingCategory.STOLEN_PLATE
    )

    # Вызываем напрямую
    create_incident(data=request_data, db=mock_db)

    # Проверяем, что контроллер вызвал нужные методы БД ровно по 1 разу
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()