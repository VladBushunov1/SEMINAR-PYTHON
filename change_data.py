from return_data_file import data_file


def change_row():
    data, num_file = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес: ")
    if num_file == 1:
        data[number_row - 1] = f'{number_row};{name};{surname};{phone};{address}\n'
    elif num_file == 2:
        data[number_row - 1] = f'{number_row}\n{name}\n{surname}\n{phone}\n{address}\n'
    with open(f'db/data_{num_file}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")
