import pytest
from booking_logic import BookingSystem

@pytest.fixture
def booking_system():
    return BookingSystem()

def test_validate_input_success(booking_system):
    """Тест успешной валидации"""
    assert booking_system.validate_input("Иван", "25.12.2025", 2) is True

def test_validate_empty_name(booking_system):
    """Тест: пустое имя вызывает ошибку"""
    with pytest.raises(ValueError, match="Имя не может быть пустым"):
        booking_system.validate_input("", "25.12.2025", 2)

def test_validate_invalid_date_format(booking_system):
    """Тест: неверный формат даты"""
    with pytest.raises(ValueError, match="Неверный формат даты"):
        booking_system.validate_input("Иван", "2025/12/25", 2)

def test_validate_guests_negative(booking_system):
    """Тест: отрицательное количество гостей"""
    with pytest.raises(ValueError, match="Количество гостей должно быть больше 0"):
        booking_system.validate_input("Иван", "25.12.2025", -1)

def test_create_booking_message(booking_system):
    """Тест формирования сообщения"""
    msg = booking_system.create_booking_message("Анна", "01.01.2026", 3)
    assert "Анна" in msg
    assert "01.01.2026" in msg
    assert "3" in msg
