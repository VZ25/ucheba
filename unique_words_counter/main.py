# программа для подсчёта уникальных слов в текстовом файле

import os


def count_unique_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()  # читаем текст и делаем все буквы маленькими
        words = text.split()  # разбиваем текст на отдельные слова
        unique_words = set(words)  # сохраняем только уникальные слова
        print("Уникальных слов:", len(unique_words))  # выводим результат


# запуск программы
if __name__ == "__main__":
    # получаем путь к текущей папке (там где этот файл)
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "sample.txt")
    count_unique_words(file_path)
