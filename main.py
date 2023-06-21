from pathlib import Path

from my_serialize_package.names_numbers_to_json import names_numbers_to_json
from my_serialize_package.users_by_access import users_to_json, users_to_csv
from my_serialize_package.traversal_dir import save_to_json, save_to_csv, save_to_pickle, load_pickle

if __name__ == '__main__':
    # task1
    # file = Path('result.txt')
    # names_numbers_to_json(file)

    # task2
    # file = Path('users.json')
    # users_to_json(file)

    # task3
    # file = Path('users.csv')
    # users_to_csv(file)

    # home_task
    res_file = 'travel_result'
    path = Path('.')
    # json
    save_to_json(path, res_file)
    # csv
    save_to_csv(path, res_file)
    # pickle
    save_to_pickle(path, res_file)
    load_pickle(Path(f'{res_file}.pickle'), 'check_pickle')

    print()
