import time
import keyboard
import time
import threading
import tkinter as tk
from tkinter import messagebox
import pyautogui
import pyperclip
#from pywinauto import Application
from Functions.func_messages import *
    
def get_selected_text():
    
    """Получает выделенный текст из активного окна."""
    """     #if is_editable():
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
        pyautogui.typewrite( new_txt )  # Вставляем 'x' вместо выделенного текста
        #pyautogui.typewrite( 'new_txt' )  # Вставляем 'x' вместо выделенного текста
        time.sleep(0.05)  # Небольшая задержка, чтобы текст успел скопироваться
        #keyboard.press_and_release( 'ctrl+v' )  # Вставляем 'x' вместо выделенного текста
               
    except pyautogui.PyAutoGUIException:
        return ""  # Возвращаем пустую строку, если pyperclip не работает """
        
    
    
    
    """     # Копируем выделенный текст в буфер обмена
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Небольшая пауза для завершения операции

    old_txt = pyperclip.paste()
    new_txt = replace_characters3( old_txt )
        
    # Заменяем содержимое буфера обмена на нужный символ
    pyperclip.copy(new_txt)  # Копируем символ в буфер обмена

    # Вставляем символ из буфера обмена
    pyautogui.hotkey('ctrl', 'v')
    
    pyperclip.copy("")  # Очищаем буфер обмена """
    
    # Копируем выделенный текст в буфер обмена
    keyboard.press_and_release( 'ctrl+c' )
    time.sleep(0.5)  # Небольшая пауза для завершения операции

    old_txt = pyperclip.paste()
    new_txt = replace_characters3( old_txt )
        
    # Заменяем содержимое буфера обмена на нужный символ
    pyperclip.copy(new_txt)  # Копируем символ в буфер обмена

    # Вставляем символ из буфера обмена
    keyboard.press_and_release( 'ctrl+v' )
    
    pyperclip.copy("")  # Очищаем буфер обмена
    

def on_ctrl_pressed():
    global last_ctrl_press_time
    current_time = time.time()
    if current_time - last_ctrl_press_time < 0.5:  # Двойное нажатие в течение 0.5 секунд
        #show_message_thread = threading.Thread(target=show_message)
        #show_message_thread.start()
        get_selected_text()
    last_ctrl_press_time = current_time


def replace_characters3(input_str):
    replacements = {
        'q': 'й',
        'w': 'ц',
        'e': 'у', 
        'r': 'к',
        't': 'е',
        'y': 'н',
        'u': 'г',
        'i': 'ш',
        'o': 'щ',
        'p': 'з',
        '[': 'х',
        ']': 'ъ',
        'a': 'ф',
        's': 'ы',
        'd': 'в',
        'f': 'а',
        'g': 'п',
        'h': 'р',
        'j': 'о',
        'k': 'л',
        'l': 'д',
        ';': 'ж',
        '''''': 'э',
        'z': 'я',
        'x': 'ч',
        'c': 'с',
        'v': 'м',
        'b': 'и',
        'n': 'т',
        'm': 'ь',
        ',': 'б',
        '.': 'ю',
        '`': 'ё',
        'Q': 'Й',
        'W': 'Ц',
        'E': 'У',
        'R': 'К',
        'T': 'Е',
        'Y': 'Н',
        'U': 'Г',
        'I': 'Ш',
        'O': 'Щ',
        'P': 'З',
        '{': 'Х',
        '}': 'Ъ',
        'A': 'Ф',
        'S': 'Ы',
        'D': 'В',
        'F': 'А',
        'G': 'П',
        'H': 'Р',
        'J': 'О',
        'K': 'Л',
        'L': 'Д',
        ';': 'Ж',
        '"': 'Э',
        'Z': 'Я',
        'X': 'Ч',
        'C': 'С',
        'V': 'М',
        'B': 'И',
        'N': 'Т',
        'M': 'Ь',
        '<': 'Б',
        '>': 'Ю',
        '~': 'Ё',
        
        
        'й': 'q',
        'ц':'w',
        'у':'e', 
        'к':'r',
        'е':'t',
        'н':'y',
        'г':'u',
        'ш':'i',
        'щ':'o',
        'з':'p',
        'х':'[',
        'ъ':']',
        'ф':'a',
        'ы':'s',
        'в':'d',
        'а':'f',
        'п':'g',
        'р':'h',
        'о':'j',
        'л':'k',
        'д':'l',
        'ж':';',
        'э':'''''',
        'я':'z',
        'ч':'x',
        'с':'c',
        'м':'v',
        'и':'b',
        'т':'n',
        'ь':'m',
        'б':',',
        'ю':'.',
        'ё':'`',
        'Й':'Q',
        'Ц':'W',
        'У':'E',
        'К':'R',
        'Е':'T',
        'Н':'Y',
        'Г':'U',
        'Ш':'I',
        'Щ':'O',
        'З':'P',
        'Х':'{',
        'Ъ':'}',
        'Ф':'A',
        'Ы':'S',
        'В':'D',
        'А':'F',
        'П':'G',
        'Р':'H',
        'О':'J',
        'Л':'K',
        'Д':'L',
        'Ж':':',
        'Э':'"',
        'Я':'Z',
        'Ч':'X',
        'С':'C',
        'М':'V',
        'И':'B',
        'Т':'N',
        'Ь':'M',
        'Б':'<',
        'Ю':'>',
        'Ё':'~'

    }
    
    output_str = ''.join(replacements.get(char, char) for char in input_str)
    return output_str


last_ctrl_press_time = 0

keyboard.on_press_key('ctrl', lambda e: on_ctrl_pressed())

keyboard.wait()  # Держите скрипт запущенным