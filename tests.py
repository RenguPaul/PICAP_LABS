# test_computer_os.py
import unittest
from main import get_os_data, get_computer_data, get_computer_os_data
from main import create_one_to_many, create_many_to_many
from main import task_b1, task_b2, task_b3

class TestComputerOS(unittest.TestCase):
    """Тесты для программы компьютеров и ОС"""
    
    def setUp(self):
        """Подготовка данных для тестов"""
        self.oss = get_os_data()
        self.computers = get_computer_data()
        self.computers_os = get_computer_os_data()
        self.one_to_many = create_one_to_many(self.computers, self.oss)
        self.many_to_many = create_many_to_many(self.computers, self.oss, self.computers_os)
    
    def test_one_to_many_creation(self):
        """Тест 1: Проверка создания связи один-ко-многим"""
        # Проверяем, что связь создана правильно
        self.assertEqual(len(self.one_to_many), 7)  # 7 компьютеров в исходных данных
        # Проверяем, что у каждого компьютера есть правильная ОС
        for model, ram, os_name in self.one_to_many:
            self.assertIsInstance(model, str)
            self.assertIsInstance(ram, int)
            self.assertIsInstance(os_name, str)
    
    def test_task_b1_computers_starting_with_A(self):
        """Тест 2: Проверка задания B1 (компьютеры на 'A')"""
        result = task_b1(self.one_to_many)
        
        # Ожидаем только компьютеры, начинающиеся с 'A'
        expected = [('Acer Aspire', 4, 'Linux')]
        
        self.assertEqual(len(result), 1)  # Должен быть только 1 компьютер на 'A'
        self.assertEqual(result, expected)
        
        # Проверяем, что все компьютеры в результате действительно начинаются с 'A'
        for model, _, _ in result:
            self.assertTrue(model.startswith('A'))
    
    def test_task_b2_min_ram_per_os(self):
        """Тест 3: Проверка задания B2 (минимальная RAM для каждой ОС)"""
        result = task_b2(self.oss, self.one_to_many)
        
        # Проверяем структуру результата
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
        
        # Проверяем, что результат отсортирован по минимальной RAM
        for i in range(len(result) - 1):
            current_min_ram = result[i][1]
            next_min_ram = result[i + 1][1]
            self.assertLessEqual(current_min_ram, next_min_ram)
        
        # Проверяем конкретные значения (на основе известных данных)
        expected_os_names = ['Linux', 'Android', 'Windows', 'macOS']
        result_os_names = [os_name for os_name, _ in result]
        
        # Проверяем, что все ожидаемые ОС присутствуют в результате
        for os_name in expected_os_names:
            self.assertIn(os_name, result_os_names)
    
    def test_task_b3_sorted_many_to_many(self):
        """Тест 4: Проверка задания B3 (отсортированные связи многие-ко-многим)"""
        result = task_b3(self.many_to_many)
        
        # Проверяем, что результат отсортирован по названию компьютера
        for i in range(len(result) - 1):
            current_model = result[i][0]
            next_model = result[i + 1][0]
            self.assertLessEqual(current_model, next_model)
        
        # Проверяем, что у нас есть данные для Dell XPS (должен быть дважды из-за двух ОС)
        dell_entries = [entry for entry in result if entry[0] == 'Dell XPS']
        self.assertEqual(len(dell_entries), 2)
    
    def test_many_to_many_creation(self):
        """Тест 5: Проверка создания связи многие-ко-многим"""
        # Проверяем, что у компьютеров с несколькими ОС есть несколько записей
        computer_counts = {}
        for model, _, _ in self.many_to_many:
            computer_counts[model] = computer_counts.get(model, 0) + 1
        
        # Dell XPS и Lenovo ThinkPad должны иметь по 2 записи (2 ОС)
        self.assertEqual(computer_counts.get('Dell XPS', 0), 2)
        self.assertEqual(computer_counts.get('Lenovo ThinkPad', 0), 2)

if __name__ == '__main__':
    unittest.main()
