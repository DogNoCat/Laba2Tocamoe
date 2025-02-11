import re
from typing import List
from datetime import datetime
import os


def find_valid_dates(text: str) -> List[str]:
    """
    Функция для поиска корректных дат в формате ДД.ММ.ГГГG в тексте.

    :param text: Строка, в которой нужно найти даты
    :return: Список корректных дат в формате строки
    """
    pattern = r"\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b"
    matches = re.findall(pattern, text)

    valid_dates = []
    for match in matches:
        date_str = ".".join(match)
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
            valid_dates.append(date_str)
        except ValueError:
            continue

    return valid_dates
def count_dates(text: str) -> int:
    """
    Подсчитывает количество корректных дат в тексте.

    :param text: Строка, в которой нужно найти даты
    :return: Количество найденных дат
    """
    return len(find_valid_dates(text))

def find_dates_from_file(filepath: str) -> List[str]:
    """
    Функция для поиска корректных дат в текстовом файле.

    :param filepath: Путь к текстовому файлу
    :return: Список найденных корректных дат
    """
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    return find_valid_dates(content)
def count_dates_from_file(filepath: str) -> int:
    """
    Подсчитывает количество дат в текстовом файле.

    :param filepath: Путь к текстовому файлу
    :return: Количество найденных дат
    """
    return count_dates(read_file_content(filepath))

def read_file_content(filepath: str) -> str:
    """
    Читает содержимое текстового файла.

    :param filepath: Путь к текстовому файлу
    :return: Содержание файла как строка
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.")
        return ""

def main():
    try:
        print("Выберите опцию:")
        print("1. Ввести текст вручную")
        print("2. Проанализировать файл")
        choice = input("Введите номер опции (1/2): ")

        if choice == "1":
            user_text = input("Введите текст для поиска дат: ")
            print(f"Количество дат в тексте: {count_dates(user_text)}")
        elif choice == "2":
            filepath = input("Введите путь к текстовому файлу: ")
            if os.path.exists(filepath):
                file_content = read_file_content(filepath)
                print(f"Количество дат в файле '{os.path.basename(filepath)}': {count_dates(file_content)}")
            else:
                print("Указанный файл не найден.")
        else:
            print("Неверный выбор. Попробуйте ещё раз!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")