import os

def main():
    print("Лабораторная работа №3-4 - Функциональные возможности Python")
    print("=" * 50)

    while True:
        print("\nВыберите задачу для выполнения:")
        print("1. field.py - Генератор field")
        print("2. gen_random.py - Генератор случайных чисел")
        print("3. unique.py - Итератор для удаления дубликатов")
        print("4. sort.py - Сортировка по модулю")
        print("5. print_result.py - Декоратор для вывода результатов")
        print("6. cm_timer.py - Контекстные менеджеры времени")
        print("7. process_data.py - Обработка данных вакансий")
        print("8. Выполнить все задачи последовательно")
        print("0. Выход")

        choice = input("\nВведите номер задачи (0-8): ").strip()

        match choice:
            case "1":
                print("\n" + "="*50)
                print("Задача 1: Генератор field")
                print("="*50)
                os.system('python3 field.py')

            case "2":
                print("\n" + "="*50)
                print("Задача 2: Генератор случайных чисел")
                print("="*50)
                os.system('python3 gen_random.py')

            case "3":
                print("\n" + "="*50)
                print("Задача 3: Итератор для удаления дубликатов")
                print("="*50)
                os.system('python3 unique.py')

            case "4":
                print("\n" + "="*50)
                print("Задача 4: Сортировка по модулю")
                print("="*50)
                os.system('python3 sort.py')

            case "5":
                print("\n" + "="*50)
                print("Задача 5: Декоратор для вывода результатов")
                print("="*50)
                os.system('python3 print_result.py')

            case "6":
                print("\n" + "="*50)
                print("Задача 6: Контекстные менеджеры времени")
                print("="*50)
                os.system('python3 cm_timer.py')

            case "7":
                print("\n" + "="*50)
                print("Задача 7: Обработка данных вакансий")
                print("="*50)
                if os.path.exists('data_light.json'):
                    os.system('python3 process_data.py data_light.json')
                else:
                    print("Файл data_light.json не найден!")
                    print("Создайте файл data_light.json в текущей директории")

            case "8":
                print("\n" + "="*50)
                print("Выполнение всех задач...")
                print("="*50)
                tasks = [
                    ("field.py", "Задача 1: Генератор field"),
                    ("gen_random.py", "Задача 2: Генератор случайных чисел"),
                    ("unique.py", "Задача 3: Итератор для удаления дубликатов"),
                    ("sort.py", "Задача 4: Сортировка по модулю"),
                    ("print_result.py", "Задача 5: Декоратор для вывода результатов"),
                    ("cm_timer.py", "Задача 6: Контекстные менеджеры времени")
                ]

                for task_file, task_name in tasks:
                    print(f"\n{task_name}")
                    print("-" * 40)
                    os.system(f'python3 {task_file}')

                print("\nЗадача 7: Обработка данных вакансий")
                print("-" * 40)
                if os.path.exists('data_light.json'):
                    os.system('python3 process_data.py data_light.json')
                else:
                    print("Файл data_light.json не найден! Пропускаем...")

            case "0":
                print("Выход из программы...")
                break

            case _:
                print("Неверный выбор! Пожалуйста, введите число от 0 до 8")

if __name__ == "__main__":
    main()
