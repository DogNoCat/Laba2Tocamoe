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
