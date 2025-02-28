def replace_characters(input_str):
    replacements = {
        'q': 'й', 'w': 'ц', 'e': 'у', 
        'r': 'к', 't': 'е', 'y': 'н',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 
        'R': 'К', 'T': 'Е', 'Y': 'Н'
    }
    
    output_str = ''
    for char in input_str:
        if char in replacements:
            output_str += replacements[char]
        else:
            output_str += char
    
    return output_str

def replace_characters0(input_str):
    # Создаем таблицу перевода
    translation_table = str.maketrans({
        'q': 'й', 'w': 'ц', 'e': 'у', 
        'r': 'к', 't': 'е', 'y': 'н',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 
        'R': 'К', 'T': 'Е', 'Y': 'Н'
    })
    
    # Применяем перевод к строке
    output_str = input_str.translate(translation_table)
    return output_str

# Пример использования
input_string = "Hello, World! qwerty"
result = replace_characters(input_string)
print(result)  # "Hello, World! йцукен"

def replace_characters1(input_str):
    replacements = {
        'q': 'й',
        'w': 'ц',
        'e': 'у'
    }
    
    output_str = ''.join(replacements.get(char, char) for char in input_str)
    return output_str


def replace_characters2(input_str):
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
        '~': 'Ё'
    }
    
    output_str = ''.join(replacements.get(char, char) for char in input_str)
    return output_str


