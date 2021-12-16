import unittest
import main
import time


class ProgramTests(unittest.TestCase):
    list_of_numbers_for_test = [1, 2, 3]
    data = []
    with open("input.txt", 'w') as file:
        for number in list_of_numbers_for_test:
            file.write(number.__str__() + " ")

    # Тест на подсчет произведения
    def test_calculate_multiplication(self):
        with open("input.txt", 'r') as file:
            input_ = []
            for line in file:
                input_.append([int(x) for x in line.split()])
            numbers = input_.pop()
            result = main.calculate_multiplication(numbers)
            self.assertEqual(6, result, "Test on multiplication")

    # Тест на подсчет суммы
    def test_calculate_sum(self):
        with open("input.txt", 'r') as file:
            input_ = []
            for line in file:
                input_.append([int(x) for x in line.split()])
            numbers = input_.pop()
            result = main.calculate_sum(numbers)
            self.assertEqual(6, result, "Test on sum")

    # Тест на поиск максимума
    def test_count_max(self):
        with open("input.txt", 'r') as file:
            input_ = []
            for line in file:
                input_.append([int(x) for x in line.split()])
            numbers = input_.pop()
            result = main.count_max(numbers)
            self.assertEqual(3, result, "Test on find max")

    # Тест на поиск минимума
    def test_count_min(self):
        with open("input.txt", 'r') as file:
            input_ = []
            for line in file:
                input_.append([int(x) for x in line.split()])
            numbers = input_.pop()
            result = main.count_min(numbers)
            self.assertEqual(1, result, "Test on find min")

    # Тест проверки скорости
    def test_check_speed(self):
        start_time = time.time()
        if __name__ == '__main__':
            main
        print("Elapsed time of program: " + (time.time() - start_time).__str__())

    # Тест на работу с большим количеством чисел
    def test_with_large_file(self):
        with open("input.txt", 'w') as file:
            for number in range(100000000):
                file.write(number.__str__() + " ")

        start_time = time.time()
        if __name__ == '__main__':
            main
        print("Elapsed time of program with large file: " + (time.time() - start_time).__str__())

    #Мой придуманный тест: корректная работа с пустым файлом
    def test_work_with_empty_file(self):
        with open("input.txt", 'w') as file:
            file.write("")
        if __name__ == '__main__':
            main


if __name__ == "__main__":
    unittest.main()
