from choice_file import choice_number_file


def data_file():
    num_file = choice_number_file()
    with open(f'db/data_{num_file}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, num_file
