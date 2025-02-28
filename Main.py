import time
import keyboard
import time
import threading
import tkinter as tk
from tkinter import messagebox
import pyautogui
import pyperclip
from pywinauto import Application
from Functions.func_messages import *
    
def get_selected_text():
    
    """Получает выделенный текст из активного окна."""
    #if is_editable():
    try:
        ## Копируем выделенный текст в буфер обмена
        #pyautogui.hotkey('ctrl', 'c')  # Копируем выделенный текст
        #time.sleep(0.05)  # Небольшая задержка, чтобы текст успел скопироваться
        ##pyautogui.typewrite(replace_characters(pyperclip.paste()))  # Вставляем 'x' вместо выделенного текста
        #old_txt = pyperclip.paste()
        #new_txt = replace_characters( old_txt )
        #pyautogui.typewrite( new_txt )  # Вставляем 'x' вместо выделенного текста

        # Заменяем выделенный текст на 'x'
        #pyautogui.hotkey('ctrl', 'v')  # Вставляем 'x' вместо выделенного текста
        
        
        pyperclip.copy("")  # Очищаем буфер обмена
        keyboard.press_and_release('ctrl+c')  # Копируем выделенный текст
        time.sleep(0.05)  # Небольшая задержка, чтобы текст успел скопироваться
        old_txt = pyperclip.paste()
        new_txt = replace_characters( old_txt )
        #pyautogui.typewrite( new_txt )  # Вставляем 'x' вместо выделенного текста
        pyautogui.typewrite( 'new_txt' )  # Вставляем 'x' вместо выделенного текста
        time.sleep(0.05)  # Небольшая задержка, чтобы текст успел скопироваться
        #keyboard.press_and_release( 'ctrl+v' )  # Вставляем 'x' вместо выделенного текста
               
    except pyautogui.PyAutoGUIException:
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
        #show_message_thread = threading.Thread(target=show_message)
        #show_message_thread.start()
        get_selected_text()
    last_ctrl_press_time = current_time

last_ctrl_press_time = 0

keyboard.on_press_key('ctrl', lambda e: on_ctrl_pressed())

keyboard.wait()  # Держите скрипт запущенным