'''Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''
import copy
import csv
import json
from pathlib import Path

TITLE = ['Level access', 'ID', 'Name']
EMPTY_DICT = {
    "1": {},
    "2": {},
    "3": {},
    "4": {},
    "5": {},
    "6": {},
    "7": {},
}


def is_valid(current_dict: dict, user_id):
    for level in current_dict.values():
        if user_id in level.keys():
            print(f'{user_id} is not unique ID')
            return False
    return True


def ask_data(current_dict: dict) -> dict:
    flag_continue = True
    while flag_continue:
        input_data = input("Enter user, ID, access level(1-7): ")
        if input_data == 'q':
            flag_continue = False
        else:
            user, user_id, level = input_data.split(', ')
            if is_valid(current_dict, user_id):
                current_dict[level][user_id] = user
    return current_dict


# json

def read_from_json(file: Path) -> dict:
    current_data = copy.deepcopy(EMPTY_DICT)
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            current_data = json.load(f)
    return current_data


def write_to_json(file: Path, current_data: dict):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(current_data, f, ensure_ascii=False, indent=2)


def users_to_json(file: Path):
    current_data = read_from_json(file)

    ask_data(current_data)

    write_to_json(file, current_data)


# csv


def read_csv(file: Path) -> dict:
    result = copy.deepcopy(EMPTY_DICT)
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            csv_read = csv.reader(f)
            next(csv_read)
            for line in csv_read:
                if not line:  # проверка на пустую строку
                    result[line[0]][line[1]] = line[2]
    return result


def write_csv(file: Path, current_data: dict):
    with open(file, 'w', encoding='utf-8') as f:
        output_data = [TITLE]
        for level, mini_dict in current_data.items():
            for user_id, user in mini_dict.items():
                output_data.append([level, user_id, user])
        csv_write = csv.writer(f, dialect='excel', lineterminator='\n')
        csv_write.writerows(output_data)


def users_to_csv(file: Path):
    current_data = read_csv(file)

    ask_data(current_data)

    write_csv(file, current_data)
