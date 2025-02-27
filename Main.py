import keyboard
import time
import threading
import tkinter as tk
from tkinter import messagebox
import pyperclip

def get_selected_text():
    """Получает выделенный текст из активного окна."""
    try:
        # Копируем выделенный текст в буфер обмена
        pyperclip.copy("")  # Очищаем буфер обмена
        keyboard.press_and_release('ctrl+c')  # Копируем выделенный текст
        time.sleep(0.05)  # Небольшая задержка, чтобы текст успел скопироваться
        selected_text = pyperclip.paste()  # Получаем текст из буфера обмена
        return selected_text
    except pyperclip.PyperclipException:
        return ""  # Возвращаем пустую строку, если pyperclip не работает
    
def show_message():
    #root = tk.Tk()
    #root.withdraw()  # Скрыть основное окно
    
    #messagebox.showinfo("Сообщение", "Привет, мир!")
    messagebox.showinfo("Сообщение", get_selected_text())
    #root.destroy()

def on_ctrl_pressed():
    global last_ctrl_press_time
    current_time = time.time()
    if current_time - last_ctrl_press_time < 0.5:  # Двойное нажатие в течение 0.5 секунд
        show_message_thread = threading.Thread(target=show_message)
        show_message_thread.start()
    last_ctrl_press_time = current_time

last_ctrl_press_time = 0

keyboard.on_press_key('ctrl', lambda e: on_ctrl_pressed())

keyboard.wait()  # Держите скрипт запущенным