#Загрузка библиотек
import tkinter as tk
from tkinter import messagebox
import winsound

#Словарь Азбуки Морзе для корректной работы шифратора на Азбуке Морзе
morse_code = {
    "Russian": {
        'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-',
        'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....',
        'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '...-',
        'Ю': '..--', 'Я': '.-.-',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    },
    "English": {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
    }
}
#Словарь двоичного кода
binary_code = {
    "Russian": {
        'А': '1101000010010000', 'Б': '1101000010010001', 'В': '1101000010010010', 'Г': '1101000010010011',
        'Д': '1101000010010100', 'Е': '1101000010010101', 'Ё': '1101000010000001', 'Ж': '1101000010010110',
        'З': '1101000010010111', 'И': '1101000010011000', 'Й': '1101000010011001', 'К': '1101000010011010',
        'Л': '1101000010011011', 'М': '1101000010011100', 'Н': '1101000010011101', 'О': '1101000010011110',
        'П': '1101000010011111', 'Р': '1101000010100000', 'С': '1101000010100001', 'Т': '1101000010100010',
        'У': '1101000010100011', 'Ф': '1101000010100100', 'Х': '1101000010100101', 'Ц': '1101000010100110',
        'Ч': '1101000010100111', 'Ш': '1101000010101000', 'Щ': '1101000010101001', 'Ъ': '1101000010101010',
        'Ы': '1101000010101011', 'Ь': '1101000010101100', 'Э': '1101000010101101', 'Ю': '1101000010101110',
        'Я': '1101000010101111', '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011', '4': '00110100',
        '5': '00110101', '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001'
    },
    "English": {
        'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111',
        'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110',
        'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101',
        'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010', '0': '00110000', '1':'00110001',
        '2': '00110010', '3': '00110011', '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111', '8': '00111000',
        '9': '00111001'
    }
}

""" Основные функции шифрования (шифрование и дешифрование)"""

def caesar_cipher(text, shift, action, language): #Шифр Цезаря
    alphabet = ''
    if language == "English": #Английский алафавит
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif language == "Russian":
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #Русский алфавит
    else:
        messagebox.showerror("Ошибка", "Выбран неподдерживаемый язык")
        return ""

    result = '' #Строка, куда будет записываться результат
    for char in text: #Цикл для посимвольного шифрования
        if char.upper() in alphabet: #Если символ находится в алфавите
            index = (alphabet.index(char.upper()) + shift) % len(alphabet) #Шифрование символа
            if action == "Дешифровать":
                index = (alphabet.index(char.upper()) - shift) % len(alphabet) #Дешифрование
            if char.islower():
                result += alphabet[index].lower() #Для строчных букв
            else:
                result += alphabet[index] #Для заглавных букв
        else:
            result += char #Если символ не находится в алафавите, то возвращается он же

    return result #Возврат результат

def vigenere_cipher(text, key, action, language): #Шифр Виженера - работает по аналонии с шифром Цезаря
    alphabet = ''
    if language == "English":
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif language == "Russian":
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        messagebox.showerror("Ошибка", "Выбран неподдерживаемый язык")
        return ""

    result = ''
    key_length = len(key) #Длина ключа
    key = key.upper() #Ключ - слово
    text = text.upper()  # Заданный текст

    for i, char in enumerate(text):
        if char in alphabet:
            key_char = key[i % key_length]   #Символ ключевого слова
            shift = alphabet.index(key_char) #Определение номера алфавита по символам из ключевого слова (сдвиг)
            if action == "Дешифровать":
                shift = -shift #Обратный сдвиг
            index = (alphabet.index(char) + shift) % len(alphabet) #Шифрование
            result += alphabet[index]
        else:
            result += char

    return result.lower()

def atbash_cipher(text, language): #Шифр Атбаша
    if language == 'Russian': #Русский алфавит
        alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #Строчные буквы
        alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #Заглавные буквы
        result = ''
        for char in text:
            if char in alphabet_lower: #Если символ в строчном алфавите
                index = alphabet_lower.index(char) #Получение номера буквы
                result += alphabet_lower[32 - index] #Переворот алфавита
            elif char in alphabet_upper: #Если символ в заглавном алфавите
                index = alphabet_upper.index(char)
                result += alphabet_upper[32 - index]
            else:
                result += char
    elif language == 'English': #Английский алфавит
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        for char in text:
            if char in alphabet_lower:
                index = alphabet_lower.index(char)
                result += alphabet_lower[25 - index]
            elif char in alphabet_upper:
                index = alphabet_upper.index(char)
                result += alphabet_upper[25 - index]
            else:
                result += char

    return result

def morse_cipher(text, language): # Шифратор Морзе
    morse_dict = morse_code.get(language, None)
    if not morse_dict:
        messagebox.showerror("Ошибка", "Выбран неподдерживаемый язык")
        return ""

    result = ''
    for char in text: #Преобразует символы по словарю (ключ = значение)
        if char.upper() in morse_dict:
            result += morse_dict[char.upper()] + ' '
        elif char == ' ':
            result += ' '
        else:
            result += char

    return result

def morse_decipher(text, language): #Дешифратор Морзе
    morse_dict = morse_code.get(language, None)
    if not morse_dict:
        messagebox.showerror("Ошибка", "Выбран неподдерживаемый язык")
        return ""

    result = ''
    morse_list = text.split(' ')
    for morse_char in morse_list: #Преобразует символы по словарю (значение = ключ)
        if morse_char in morse_dict.values():
            for key, value in morse_dict.items():
                if morse_char == value:
                    result += key + ' '
        elif morse_char == ' ':
            result += ' '
        else:
            result += morse_char

    return result.lower()

def binary_cipher(text, language): #Шифратор (Двоичный код)
    binary_dict = binary_code.get(language, None)
    if not binary_dict:
        messagebox.showerror("Ошибка", "Выбран неподдерживаемый язык")
        return ""

    result = ''
    for char in text:
        if char.upper() in binary_dict:
            result += binary_dict[char.upper()] + ' '
        elif char == ' ':
            result += ' '
        else:
            result += char

    return result

def binary_decipher(text, language): #Дешифратор (Двоичный код)
    binary_dict = binary_code.get(language, None)
    if not binary_dict:
        messagebox.showerror("Ошибка", "Выбран неподдерживаемый язык")
        return ""

    result = ''
    binary_list = text.split(' ')
    for binary_char in binary_list:
        if binary_char in binary_dict.values():
            for key, value in binary_dict.items():
                if binary_char == value:
                    result += key + ' '
        elif binary_char == ' ':
            result += ' '
        else:
            result += binary_char

    return result

"""Выполнение шифров (для срабатывания функции при нажатии на кнопку)"""

def perform_ceasar_cipher(): #Шифр Цезаря
    text = input_text.get("1.0", "end-1c") #Глобальные переменные
    shift = int(shift_var.get())
    action = action_var.get()
    language = language_var.get()

    result = caesar_cipher(text, shift, action, language) #Получение результата
    output_text.delete("1.0", tk.END) #Удаление текста из поля
    output_text.insert(tk.END, result) #Добавление текста в поле

def perform_vigenere_cipher(): #Шифр Виженера
    text = input_text.get("1.0", "end-1c")
    key = key_var.get()
    action = action_var.get()
    language = language_var.get()

    result = vigenere_cipher(text, key, action, language)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def perform_atbash_cipher(): #Шифр Атбаша
    text = input_text.get("1.0", "end-1c")
    action = action_var.get()
    language = language_var.get()

    result = atbash_cipher(text, language)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def perform_morse_cipher(): #Азбука Морзе
    text = input_text.get("1.0", "end-1c")
    action = action_var.get()
    language = language_var.get()

    if action == "Зашифровать":
        result = morse_cipher(text, language)
    else:
        result = morse_decipher(text, language)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def perform_binary_cipher():
    text = input_text.get("1.0", "end-1c")
    action = action_var.get()
    language = language_var.get()

    if action == "Зашифровать":
        result = binary_cipher(text, language)
    else:
        result = binary_decipher(text, language)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result.lower())

""" Вспомогательные функции"""

def clear_text(): #Удаление текста
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

def play_morse_code(text): #Функция звукового воспроиведения азбуки Морзе
    for char in text:
        if char == '.':
            winsound.Beep(1000, 200)  # Воспроизведение точки
        elif char == '-':
            winsound.Beep(1000, 600)  # Воспроизведение тире
        elif char == ' ':
            pass  # Пауза между символами

def play_morse_result(): #Воспроизведение результата
    text = output_text.get("1.0", "end-1c")
    play_morse_code(text)

""" Функции, отвечающие за создание новых окон. Содержат в себе различные графические элементы. """

def create_caesar_cipher_window(): #Шифр Цезаря
    #Создание нового окна и задание загаловка
    caesar_cipher_window = tk.Toplevel(root)
    caesar_cipher_window.title("Шифр Цезаря")

    # Создание виджетов (метки, поля, кнопки)
    language_label = tk.Label(caesar_cipher_window, text="Язык:")
    language_label.pack()
    language_var.set("Russian")  # Значение по умолчанию
    language_menu = tk.OptionMenu(caesar_cipher_window, language_var, "Russian", "English")
    language_menu.pack()

    shift_label = tk.Label(caesar_cipher_window, text="Сдвиг:")
    shift_label.pack()
    shift_entry = tk.Entry(caesar_cipher_window, textvariable=shift_var)
    shift_entry.pack()

    action_label = tk.Label(caesar_cipher_window, text="Действие:" )
    action_label.pack()
    action_var.set("Зашифровать")  # Значение по умолчанию
    action_menu = tk.OptionMenu(caesar_cipher_window, action_var, "Зашифровать", "Дешифровать")
    action_menu.pack()

    input_label = tk.Label(caesar_cipher_window, text="Входной текст:")
    input_label.pack()
    global input_text
    input_text = tk.Text(caesar_cipher_window, height=5, width=40)
    input_text.pack()

    output_label = tk.Label(caesar_cipher_window, text="Результат:")
    output_label.pack()
    global output_text
    output_text = tk.Text(caesar_cipher_window, height=5, width=40)
    output_text.pack()

    cipher_button = tk.Button(caesar_cipher_window, text="Выполнить шифрование/дешифрование", command=perform_ceasar_cipher)
    cipher_button.pack()

    clear_button = tk.Button(caesar_cipher_window, text="Стереть", command=clear_text)
    clear_button.pack()

def create_vigenere_cipher_window(): #Шифр Виженера
    vigenere_cipher_window = tk.Toplevel(root)
    vigenere_cipher_window.title("Шифр Виженера")

    language_label = tk.Label(vigenere_cipher_window, text="Язык:")
    language_label.pack()
    language_var.set("Russian")
    language_menu = tk.OptionMenu(vigenere_cipher_window, language_var, "Russian", "English")
    language_menu.pack()

    key_label = tk.Label(vigenere_cipher_window, text="Ключевое слово:")
    key_label.pack()
    global key_var
    key_var = tk.StringVar()
    key_entry = tk.Entry(vigenere_cipher_window, textvariable=key_var)
    key_entry.pack()

    action_label = tk.Label(vigenere_cipher_window, text="Действие:")
    action_label.pack()
    action_var.set("Зашифровать")
    action_menu = tk.OptionMenu(vigenere_cipher_window, action_var, "Зашифровать", "Дешифровать")
    action_menu.pack()

    input_label = tk.Label(vigenere_cipher_window, text="Входной текст:")
    input_label.pack()
    global input_text
    input_text = tk.Text(vigenere_cipher_window, height=5, width=40)
    input_text.pack()

    output_label = tk.Label(vigenere_cipher_window, text="Результат:")
    output_label.pack()
    global output_text
    output_text = tk.Text(vigenere_cipher_window, height=5, width=40)
    output_text.pack()

    cipher_button = tk.Button(vigenere_cipher_window, text="Выполнить шифрование/дешифрование", command=perform_vigenere_cipher)
    cipher_button.pack()

    clear_button = tk.Button(vigenere_cipher_window, text="Стереть", command=clear_text)
    clear_button.pack()

def create_atbash_cipher_window(): #Шифр Атбаша
    atbash_cipher_window = tk.Toplevel(root)
    atbash_cipher_window.title("Шифр Атбаша")

    language_label = tk.Label(atbash_cipher_window, text="Язык:")
    language_label.pack()
    language_var.set("Russian")
    language_menu = tk.OptionMenu(atbash_cipher_window, language_var, "Russian", "English")
    language_menu.pack()

    input_label = tk.Label(atbash_cipher_window, text="Входной текст:")
    input_label.pack()
    global input_text
    input_text = tk.Text(atbash_cipher_window, height=5, width=40)
    input_text.pack()

    output_label = tk.Label(atbash_cipher_window, text="Результат:")
    output_label.pack()
    global output_text
    output_text = tk.Text(atbash_cipher_window, height=5, width=40)
    output_text.pack()

    cipher_button = tk.Button(atbash_cipher_window, text="Выполнить шифрование/дешифрование", command=perform_atbash_cipher)
    cipher_button.pack()

    clear_button = tk.Button(atbash_cipher_window, text="Стереть", command=clear_text)
    clear_button.pack()

def create_morse_cipher_window(): #Азбука Морзе
    morse_cipher_window = tk.Toplevel(root)
    morse_cipher_window.title("Азбука Морзе")

    language_label = tk.Label(morse_cipher_window, text="Язык:")
    language_label.pack()
    language_var.set("Russian")
    language_menu = tk.OptionMenu(morse_cipher_window, language_var, "Russian", "English")
    language_menu.pack()

    action_label = tk.Label(morse_cipher_window, text="Действие:")
    action_label.pack()
    action_var.set("Зашифровать")
    action_menu = tk.OptionMenu(morse_cipher_window, action_var, "Зашифровать", "Дешифровать")
    action_menu.pack()

    input_label = tk.Label(morse_cipher_window, text="Входной текст:")
    input_label.pack()
    global input_text
    input_text = tk.Text(morse_cipher_window, height=5, width=40)
    input_text.pack()

    output_label = tk.Label(morse_cipher_window, text="Результат:")
    output_label.pack()
    global output_text
    output_text = tk.Text(morse_cipher_window, height=5, width=40)
    output_text.pack()

    cipher_button = tk.Button(morse_cipher_window, text="Выполнить шифрование/дешифрование", command=perform_morse_cipher)
    cipher_button.pack()

    play_morse_button = tk.Button(morse_cipher_window, text="Озвучить Морзе", command=play_morse_result)
    play_morse_button.pack()

    clear_button = tk.Button(morse_cipher_window, text="Стереть", command=clear_text)
    clear_button.pack()

def create_binary_cipher_window():
    binary_cipher_window = tk.Toplevel(root)
    binary_cipher_window.title("Двоичный код")

    language_label = tk.Label(binary_cipher_window, text="Язык:")
    language_label.pack()
    language_var.set("Russian")
    language_menu = tk.OptionMenu(binary_cipher_window, language_var, "Russian", "English")
    language_menu.pack()

    action_label = tk.Label(binary_cipher_window, text="Действие:")
    action_label.pack()
    action_var.set("Зашифровать")
    action_menu = tk.OptionMenu(binary_cipher_window, action_var, "Зашифровать", "Дешифровать")
    action_menu.pack()

    input_label = tk.Label(binary_cipher_window, text="Входной текст:")
    input_label.pack()
    global input_text
    input_text = tk.Text(binary_cipher_window, height=5, width=40)
    input_text.pack()

    output_label = tk.Label(binary_cipher_window, text="Результат:")
    output_label.pack()
    global output_text
    output_text = tk.Text(binary_cipher_window, height=5, width=40)
    output_text.pack()

    cipher_button = tk.Button(binary_cipher_window, text="Выполнить шифрование/дешифрование", command=perform_binary_cipher)
    cipher_button.pack()

    clear_button = tk.Button(binary_cipher_window, text="Стереть", command=clear_text)
    clear_button.pack()

class ThemeManager: #Класс для переключения темы
    def __init__(self, root):
        self.root = root
        self.is_dark_mode = False

    def toggle_theme(self):
        if self.is_dark_mode:
            self.root.tk_setPalette(background='#FFFFFF', foreground='#000000')
        else:
            self.root.tk_setPalette(background='#000000', foreground='#FFFFFF')
        self.is_dark_mode = not self.is_dark_mode


"""Создание главного(начального) окна"""

#Изначальная настрока
root = tk.Tk()
root.geometry('250x190')
root.title("Шифраторы")
root.configure(pady=5, padx=5)

theme_manager = ThemeManager(root) #Создание экземпляра класса

def toggle_theme(): #Переключение темы
    theme_manager.toggle_theme()

#Знак копирайта
copyryte_lable = tk.Label(root, text = "©Нечаев Евгений Александрович")
copyryte_lable.pack(anchor="nw")

#Кнопки на шифры
caesar_cipher_button = tk.Button(root, text="Шифр Цезаря", command=create_caesar_cipher_window)
caesar_cipher_button.pack(side="top", fill="x")

vigenere_cipher_button = tk.Button(root, text="Шифр Виженера", command=create_vigenere_cipher_window)
vigenere_cipher_button.pack(side="top", fill="x")

atbash_cipher_button = tk.Button(root, text="Шифр Атбаш", command=create_atbash_cipher_window)
atbash_cipher_button.pack(side="top", fill="x")

morse_cipher_button = tk.Button(root, text="Азбука Морзе", command=create_morse_cipher_window)
morse_cipher_button.pack(side="top", fill="x")

binary_cipher_button = tk.Button(root, text="Двоичный код", command=create_binary_cipher_window)
binary_cipher_button.pack(side="top", fill="x")

#Кнопка переключения темы
theme_button = tk.Button(root, text="Переключить тему", command=toggle_theme)
theme_button.pack(side="top", fill="x", ipady=20)

#Глобальные переменные
shift_var = tk.StringVar()
action_var = tk.StringVar()
language_var = tk.StringVar()

root.mainloop() #Отображение окна и взаимодействие с пользователем