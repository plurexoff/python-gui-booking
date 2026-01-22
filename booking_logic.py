from datetime import datetime

class BookingSystem:
    def validate_input(self, name, date_str, guests):
        """Проверяет корректность введенных данных."""
        if not name:
            raise ValueError("Имя не может быть пустым")
        
        if not date_str:
            raise ValueError("Дата не может быть пустой")
            
        try:
            # Проверка формата даты
            datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте ДД.ММ.ГГГГ")

        try:
            guests_int = int(guests)
            if guests_int < 1:
                raise ValueError("Количество гостей должно быть больше 0")
        except ValueError:
            raise ValueError("Количество гостей должно быть числом")

        return True

    def create_booking_message(self, name, date_str, guests):
        """Создает сообщение о бронировании."""
        self.validate_input(name, date_str, guests)
        return f"Бронь подтверждена!\nГость: {name}\nДата: {date_str}\nКол-во персон: {guests}"
