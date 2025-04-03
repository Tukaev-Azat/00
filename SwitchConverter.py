import subprocess
import time
import keyboard
import pyperclip

from pynput import keyboard as kb

import pystray
from pystray import MenuItem as item
from PIL import Image
import threading
import os

replacements = {}
    
def get_selected_text():
    # Копируем выделенный текст в буфер обмена
    keyboard.press_and_release( 'ctrl+c' )
    time.sleep(0.5)  # Небольшая пауза для завершения операции

    lv_new_txt = ''.join(replacements.get(char, char) for char in pyperclip.paste())

    # Заменяем содержимое буфера обмена на нужный символ
    pyperclip.copy(lv_new_txt)

    # Вставляем символ из буфера обмена
    keyboard.press_and_release( 'ctrl+v' )

    time.sleep(0.5)  # Небольшая пауза для завершения операции
    keyboard.press_and_release( 'alt+shift' )
    
def upload_replacements():
    #загрузить перекодировочный файл
    with open('replacements.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line[0], line[1]
                replacements[key] = value

def exit_action(icon, item):
    #закрытие программы
    icon.stop()
    # Даем pystray время, чтобы очиститься
    time.sleep(0.1)
    # Останавливаем keyboard.wait(), чтобы программа завершилась
    keyboard.unhook_all()
    icon.remove_notification()
    os._exit(0)

def open_settings_file():
    #открыть файл перекодировки
    lv_settings_file_name = 'replacements.txt'
    try:
        os.startfile(lv_settings_file_name)
    except AttributeError:
        try:
            os.system('open "%s"' % lv_settings_file_name)
        except:
            subprocess.call(['xdg-open', lv_settings_file_name])

def create_tray_icon():
    # Системный трей
    image = Image.open("ico.png")
    menu = (item('Настройки', open_settings_file),item('Выход', exit_action),)
    icon = pystray.Icon("Название", image, "Заголовок", menu)
    icon.run()

def on_press(key):
    # Анализ нажатий клавиш
    global ctrl_press_count, last_press_time
    if key == kb.Key.ctrl_r:
        current_time = time.time()
        if ctrl_press_count == 0 or (current_time - last_press_time) <= 0.5:
            ctrl_press_count += 1
            last_press_time = current_time
            if ctrl_press_count == 2:
                #print("hello, world!")
                get_selected_text()
                ctrl_press_count = 0  # Сброс счётчика после вывода сообщения
        else:
            ctrl_press_count = 1
            last_press_time = current_time

def on_release(key):
    pass  # Здесь можно добавить обработку отпускания клавиши, если нужно

upload_replacements()

# Инициализация счётчика нажатий и времени последнего нажатия
ctrl_press_count = 0
last_press_time = time.time()

# Создание слушателя
with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    #listener.join()
    create_tray_icon()