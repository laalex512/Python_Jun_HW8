# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json
from pathlib import Path


def names_numbers_to_json(file: Path):
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split(' : ')
            file_data[name.capitalize()] = float(number)

    with open(f'{file.stem}.json', 'w', encoding='utf-8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=2)
