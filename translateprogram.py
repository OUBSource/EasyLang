import os
from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar
from deep_translator import GoogleTranslator
from langdetect import detect

# Функция перевода текста
def translate(text, target_language="en"):
    try:
        # Определение исходного языка, если не выбран
        source_language = detect(text)
        if source_language == target_language:
            return text  # Если язык совпадает с целевым, просто возвращаем текст
        return GoogleTranslator(source=source_language, target=target_language).translate(text)
    except Exception as e:
        print(f"Error during translation: {e}")
        return text  # Если ошибка, возвращаем оригинальный текст

# Функция для обновления текста и сохранения выбранных языков в файл
def update_translation():
    text_to_translate = text_entry.get()
    target_language = target_language_var.get()
    
    if not text_to_translate:
        label.config(text="Please enter text to translate")
        return
    
    if not target_language:
        label.config(text="Please select a target language")
        return
    
    # Определение исходного языка
    source_language = detect(text_to_translate)
    
    # Перевод текста
    translated_text = translate(text_to_translate, target_language)
    label.config(text=translated_text)
    
    # Сохраняем выбранный язык в файл
    with open("LANG.TXT", "w") as file:
        file.write(f"{source_language} to {target_language}")

# Функция для получения исходного языка
def detect_source_language():
    text_to_translate = text_entry.get()
    if text_to_translate:
        source_language = detect(text_to_translate)
        source_language_label.config(text=f"Detected language: {source_language}")
    else:
        source_language_label.config(text="Enter text to detect language")

# Инициализация Tkinter
root = Tk()
root.title("Mini Translator")

# Текстовая метка
label = Label(root, text="Translation Result", font=("Arial", 16))
label.pack(pady=20)

# Поле для ввода текста
text_entry = Entry(root, font=("Arial", 14), width=40)
text_entry.pack(pady=10)

# Метка для отображения определенного языка
source_language_label = Label(root, text="Detected language will appear here", font=("Arial", 12))
source_language_label.pack(pady=5)

# Список языков
languages = [
    "en", "ru", "es", "fr", "de", "it", "pt", "ar", "zh", "ja", "ko", "nl", "tr", "pl", "uk",
    "sv", "no", "fi", "da", "cs", "el", "hi", "he", "hu", "ro", "th", "vi", "bn", "id", "ms"
]

# Настройки языка перевода
target_language_var = StringVar(root)
target_language_var.set("en")  # По умолчанию на английский

target_language_menu = OptionMenu(root, target_language_var, *languages)
target_language_menu.pack(pady=10)

# Кнопка перевода
translate_button = Button(root, text="Translate", command=update_translation, font=("Arial", 14))
translate_button.pack(pady=10)

# Кнопка определения языка исходного текста
detect_button = Button(root, text="Detect Language", command=detect_source_language, font=("Arial", 14))
detect_button.pack(pady=10)

# Кнопка выхода
exit_button = Button(root, text="Exit", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=10)

# Инициализация окна
root.geometry("500x400")
root.mainloop()
