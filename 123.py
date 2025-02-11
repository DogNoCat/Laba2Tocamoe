import re
from typing import List
from datetime import datetime
import os


def find_valid_dates(text: str) -> List[str]:
    """
    ������� ��� ������ ���������� ��� � ������� ��.��.���G � ������.

    :param text: ������, � ������� ����� ����� ����
    :return: ������ ���������� ��� � ������� ������
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
    ������������ ���������� ���������� ��� � ������.

    :param text: ������, � ������� ����� ����� ����
    :return: ���������� ��������� ���
    """
    return len(find_valid_dates(text))

def find_dates_from_file(filepath: str) -> List[str]:
    """
    ������� ��� ������ ���������� ��� � ��������� �����.

    :param filepath: ���� � ���������� �����
    :return: ������ ��������� ���������� ���
    """
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    return find_valid_dates(content)
def count_dates_from_file(filepath: str) -> int:
    """
    ������������ ���������� ��� � ��������� �����.

    :param filepath: ���� � ���������� �����
    :return: ���������� ��������� ���
    """
    return count_dates(read_file_content(filepath))

def read_file_content(filepath: str) -> str:
    """
    ������ ���������� ���������� �����.

    :param filepath: ���� � ���������� �����
    :return: ���������� ����� ��� ������
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"���� '{filepath}' �� ������.")
        return ""

def main():
    try:
        print("�������� �����:")
        print("1. ������ ����� �������")
        print("2. ���������������� ����")
        choice = input("������� ����� ����� (1/2): ")

        if choice == "1":
            user_text = input("������� ����� ��� ������ ���: ")
            print(f"���������� ��� � ������: {count_dates(user_text)}")
        elif choice == "2":
            filepath = input("������� ���� � ���������� �����: ")
            if os.path.exists(filepath):
                file_content = read_file_content(filepath)
                print(f"���������� ��� � ����� '{os.path.basename(filepath)}': {count_dates(file_content)}")
            else:
                print("��������� ���� �� ������.")
        else:
            print("�������� �����. ���������� ��� ���!")

    except Exception as e:
        print(f"��������� ������: {e}")