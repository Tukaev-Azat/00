import subprocess
import time
import keyboard
import pyperclip

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

def upload_replacements():
    #загрузить перекодировочный файл
    with open('replacements.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line[0], line[1]
                replacements[key] = value
                
def keyboard_listener():
    #запустить слушатель клавиатуры
    keyboard.on_press_key("print screen", lambda _: get_selected_text())
    keyboard.wait()

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


upload_replacements()

# Запускаем прослушиватель клавиатуры в отдельном потоке
keyboard_thread = threading.Thread(target=keyboard_listener)
keyboard_thread.daemon = True
keyboard_thread.start()

create_tray_icon()