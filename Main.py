from pynput import keyboard
import time

def on_press(key):
    global ctrl_press_count, last_press_time
    if key == keyboard.Key.ctrl_r:
        current_time = time.time()
        if ctrl_press_count == 0 or (current_time - last_press_time) <= 0.5:
            ctrl_press_count += 1
            last_press_time = current_time
            if ctrl_press_count == 2:
                print("hello, world!")
                ctrl_press_count = 0  # Сброс счётчика после вывода сообщения
        else:
            ctrl_press_count = 1
            last_press_time = current_time

def on_release(key):
    pass  # Здесь можно добавить обработку отпускания клавиши, если нужно

# Инициализация счётчика нажатий и времени последнего нажатия
ctrl_press_count = 0
last_press_time = time.time()

# Создание слушателя
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
