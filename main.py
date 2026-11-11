from warehouse import Warehouse

MIN_ITEMS_COUNT = 0
UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Добавить товар',
    '2': 'Узнать количество конкретного товара',
    '3': 'Узнать общее количество всех товаров',
    '4': 'Посмотреть все товары',
    '5': 'Выйти'
}

(ADD_ITEM_COMMAND, GET_ITEM_COUNT_COMMAND, GET_TOTAL_COUNT_COMMAND,
 SHOW_ALL_ITEMS_COMMAND, EXIT_COMMAND) = commands.keys()

warehouse = Warehouse()


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def is_valid_item_title(item_title: str) -> bool:
    if isinstance(item_title, str):
        if item_title.strip():
            return True

    return False


def is_valid_number(item_count: str) -> bool:
    if item_count.isdigit():
        item_count = int(item_count)

        if item_count >= MIN_ITEMS_COUNT:
            return True

    return False


is_program_running = True

while is_program_running:
    print_commands()
    user_command_number = input('Выберите действие и укажите его номер: ').strip()

    if user_command_number in commands:
        if user_command_number == ADD_ITEM_COMMAND:
            user_item_title = input('Укажите название товара: ').strip().capitalize()

            if is_valid_item_title(user_item_title):
                if user_item_title in warehouse:
                    print('Ошибка. Такой товар уже есть на складе')
                else:
                    user_items_count = input('Укажите количество товаров: ').strip()

                    if is_valid_number(user_items_count):
                        user_items_count = int(user_items_count)
                        warehouse[user_item_title] = user_items_count
                        print('Товар успешно добавлен')
                    else:
                        print('Ошибка. Количество должно быть неотрицательным числом')
            else:
                print('Ошибка. Название товара не может быть пустым')

        elif user_command_number == GET_ITEM_COUNT_COMMAND:
            user_item_title = input('Укажите название товара: ').strip().capitalize()
            user_item_count = warehouse[user_item_title]
            print(f'Количество товара "{user_item_title}": {user_item_count}')

        elif user_command_number == GET_TOTAL_COUNT_COMMAND:
            total_items_count = len(warehouse)
            print(f'Общее количество всех товаров: {total_items_count}')

        elif user_command_number == SHOW_ALL_ITEMS_COMMAND:
            items_count = len(warehouse)

            if items_count > MIN_ITEMS_COUNT:
                for title, count in warehouse:
                    print(f'{title}: {count}')
            else:
                print('Склад пуст')

        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
