from return_data_file import data_file


def add_row():
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес: ")
    data, num_file = data_file()
    now_number_row = len(data) + 1
    if num_file == 1:  
        z = ';'
    elif num_file == 2:
        z = '\n'
    
    with open(f'db/data_{num_file}.txt', 'a', encoding='utf-8') as file:    
        file.write(f'{now_number_row}{z}{name}{z}'
                     f'{surname}{z}{phone}{z}{address}\n')
    
    print("Данные успешно записаны!")