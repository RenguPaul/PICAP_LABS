# main.py (рефакторинг основной программы)
from operator import itemgetter

class OS:
    """Операционная система"""
    def __init__(self, id, name, version):
        self.id = id
        self.name = name
        self.version = version

class Computer:
    """Компьютер"""
    def __init__(self, id, model, ram_gb, os_id):
        self.id = id
        self.model = model
        self.ram_gb = ram_gb
        self.os_id = os_id

class ComputerOS:
    """Компьютеры с ОС для реализации связи многие-ко-многим"""
    def __init__(self, computer_id, os_id):
        self.computer_id = computer_id
        self.os_id = os_id

# Тестовые данные
def get_os_data():
    """Возвращает список операционных систем"""
    return [
        OS(1, 'Windows', '10'),
        OS(2, 'Linux', 'Ubuntu 20.04'),
        OS(3, 'macOS', 'Monterey'),
        OS(4, 'Android', '11'),
        OS(5, 'Windows', '11'),
    ]

def get_computer_data():
    """Возвращает список компьютеров"""
    return [
        Computer(1, 'Dell XPS', 16, 1),
        Computer(2, 'HP Pavilion', 8, 2),
        Computer(3, 'MacBook Pro', 16, 3),
        Computer(4, 'Lenovo ThinkPad', 32, 1),
        Computer(5, 'Asus ZenBook', 8, 5),
        Computer(6, 'Samsung Tablet', 6, 4),
        Computer(7, 'Acer Aspire', 4, 2),
    ]

def get_computer_os_data():
    """Возвращает данные связи компьютеров и ОС"""
    return [
        ComputerOS(1, 1),
        ComputerOS(2, 2),
        ComputerOS(3, 3),
        ComputerOS(4, 1),
        ComputerOS(5, 5),
        ComputerOS(6, 4),
        ComputerOS(7, 2),
        ComputerOS(1, 5),  # Dell XPS имеет две ОС
        ComputerOS(4, 2),  # Lenovo ThinkPad имеет две ОС
    ]

def create_one_to_many(computers, oss):
    """Создает связь один-ко-многим между компьютерами и ОС"""
    return [(c.model, c.ram_gb, os.name)
            for os in oss
            for c in computers
            if c.os_id == os.id]

def create_many_to_many(computers, oss, computers_os):
    """Создает связь многие-ко-многим между компьютерами и ОС"""
    many_to_many_temp = [(os.name, cos.os_id, cos.computer_id)
                         for os in oss
                         for cos in computers_os
                         if os.id == cos.os_id]
    
    return [(c.model, c.ram_gb, os_name)
            for os_name, os_id, computer_id in many_to_many_temp
            for c in computers if c.id == computer_id]

def task_b1(one_to_many):
    """Задание B1: компьютеры с моделью на 'A' и их ОС"""
    return list(filter(lambda i: i[0].startswith('A'), one_to_many))

def task_b2(oss, one_to_many):
    """Задание B2: ОС с минимальной RAM компьютеров"""
    res_2_unsorted = []
    for os in oss:
        os_computers = list(filter(lambda i: i[2] == os.name, one_to_many))
        if len(os_computers) > 0:
            os_rams = [ram for _, ram, _ in os_computers]
            min_ram = min(os_rams)
            res_2_unsorted.append((os.name, min_ram))
    
    return sorted(res_2_unsorted, key=itemgetter(1))

def task_b3(many_to_many):
    """Задание B3: связанные компьютеры и ОС, отсортированные по компьютерам"""
    return sorted(many_to_many, key=itemgetter(0))

def main():
    """Основная функция"""
    # Получение данных
    oss = get_os_data()
    computers = get_computer_data()
    computers_os = get_computer_os_data()
    
    # Создание связей
    one_to_many = create_one_to_many(computers, oss)
    many_to_many = create_many_to_many(computers, oss, computers_os)
    
    # Выполнение заданий
    print('Задание В1')
    print('Список всех компьютеров, у которых модель начинается с буквы "А", и названия их ОС:')
    res_1 = task_b1(one_to_many)
    print(res_1)

    print('\nЗадание В2')
    print('Список ОС с минимальным объемом оперативной памяти компьютеров в каждой ОС, отсортированный по минимальной памяти:')
    res_2 = task_b2(oss, one_to_many)
    print(res_2)

    print('\nЗадание В3')
    print('Список всех связанных компьютеров и ОС, отсортированный по компьютерам:')
    res_3 = task_b3(many_to_many)
    print(res_3)

if __name__ == '__main__':
    main()
