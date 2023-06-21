# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import csv
import json
import pickle
from pathlib import Path


def traverse_directory(path: Path):
    result_dict = {}
    for object in path.glob('*'):
        obj_dict = {
            'parent': str(object.parent),
        }
        if object.is_dir():
            obj_dict.setdefault('type', 'dir')
            size = 0
            for obj in object.glob('**/*'):
                if obj.is_file():
                    size += obj.stat().st_size
            obj_dict.setdefault('size', size)
            obj_dict.setdefault('inside', traverse_directory(Path(object)))
        if object.is_file():
            obj_dict.setdefault('type', 'file')
            obj_dict.setdefault('size', object.stat().st_size)
        result_dict.setdefault(object.name, obj_dict)
    return result_dict


# JSON

def save_to_json(path: Path, filename: str):
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(traverse_directory(path), f, ensure_ascii=False, indent=3)


# CSV

TITLE = ['Name', 'Parent', 'Type', 'Size', 'Inside']


def dict_to_list(input_dict: dict) -> list:
    result = [[TITLE]]
    for object, values in input_dict.items():
        obj_list = []
        obj_list.append(object)
        obj_list.append(values['parent'])
        obj_list.append(values['type'])
        obj_list.append(values['size'])
        if values['type'] == 'dir':
            inside_list = [i for i in values['inside']]
            obj_list.append(inside_list)
            result.append(obj_list)
            return_list = dict_to_list(values['inside'])[1:]
            for line in return_list:
                result.append(line)
        else:
            result.append(obj_list)

    return result


def save_to_csv(path: Path, filename: str):
    with open(f'{filename}.csv', 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', lineterminator='\n')
        output_data = dict_to_list(traverse_directory(path))
        csv_write.writerows(output_data)


# Pickle
def save_to_pickle(path: Path, filename: str):
    with open(f'{filename}.pickle', 'wb') as f:
        pickle.dump(traverse_directory(path), f)


def load_pickle(path: Path, json_file: str):
    with (
        open(path, 'rb') as pickle_read,
        open(f'{json_file}.json', 'w', encoding='utf-8') as write_json
    ):
        res = pickle.load(pickle_read)
        json.dump(res, write_json, ensure_ascii=False, indent=3)
