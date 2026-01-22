import tkinter as tk
from tkinter import ttk, messagebox

def book_table():
    """Обработка события нажатия кнопки"""
    name = entry_name.get()
    date = entry_date.get()
    guests = spinbox_guests.get()
    
    # Простая валидация данных
    if not name or not date:
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
        return

    # Отображение результатов
    result_text = f"Бронь подтверждена!\nГость: {name}\nДата: {date}\nКол-во персон: {guests}"
    label_result.config(text=result_text, foreground="green")
    
    # Всплывающее окно
    messagebox.showinfo("Успешно", f"Столик забронирован на имя {name}")

# Создание главного окна
root = tk.Tk()
root.title("Система Бронирования")
root.geometry("400x350")
root.resizable(False, False)

# Настройка стилей
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10, "bold"))

# Заголовок
header = ttk.Label(root, text="Бронирование столика", font=("Arial", 16, "bold"))
header.pack(pady=15)

# Контейнер для полей ввода
frame = ttk.Frame(root)
frame.pack(pady=10, padx=20, fill='x')

# Поле: Имя
ttk.Label(frame, text="Ваше имя:").grid(row=0, column=0, sticky='w', pady=5)
entry_name = ttk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=5)

# Поле: Дата
ttk.Label(frame, text="Дата (ДД.ММ.ГГГГ):").grid(row=1, column=0, sticky='w', pady=5)
entry_date = ttk.Entry(frame, width=30)
entry_date.grid(row=1, column=1, pady=5)

# Поле: Количество гостей
ttk.Label(frame, text="Количество гостей:").grid(row=2, column=0, sticky='w', pady=5)
spinbox_guests = ttk.Spinbox(frame, from_=1, to=10, width=28)
spinbox_guests.set(2)
spinbox_guests.grid(row=2, column=1, pady=5)

# Кнопка подтверждения
btn_submit = ttk.Button(root, text="Забронировать", command=book_table)
btn_submit.pack(pady=20, ipadx=10, ipady=5)

# Виджет для отображения результатов
label_result = ttk.Label(root, text="", font=("Arial", 10, "italic"))
label_result.pack(pady=10)

# Запуск цикла событий
root.mainloop()