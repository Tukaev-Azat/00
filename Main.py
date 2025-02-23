import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog

# Функция для выбора файла и преобразования данных
def convert_excel_to_json():
    # Создаем окно для выбора файла
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    file_path = filedialog.askopenfilename(
        title="Выберите файл Excel",
        filetypes=(("Excel Files", "*.xls;*.xlsx"), ("All Files", "*.*"))
    )

    if file_path:
        # Читаем данные из Excel файла
        df = pd.read_excel(file_path)

        # Конвертируем DataFrame в формат JSON
        json_data = df.to_dict(orient='records')
        json_output = json.dumps(json_data, ensure_ascii=False, indent=4)

        # Выводим данные в терминал
        print(json_output)
    else:
        print("Файл не выбран.")

# Запускаем функцию
convert_excel_to_json()