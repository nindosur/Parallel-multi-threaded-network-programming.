import threading
import random
import math
import os


    # 1
def fill_list(lst):
    for i in range(10):
        lst.append(random.randint(1, 100))

def calculate_sum(lst):
    total_sum = sum(lst)
    print("Сумма чисел:", total_sum)

def srarifm(lst):
    sr = sum(lst) / len(lst)
    print("Ср. арифметическое:", sr)

my_list = []
t1 = threading.Thread(target=fill_list, args=(my_list,))
t2 = threading.Thread(target=calculate_sum, args=(my_list,))
t3 = threading.Thread(target=srarifm, args=(my_list,))

t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

print("Список:", my_list)

    # 2
input_path = input("Введите путь к входному файлу (в формате имяфайла.txt): ")
output_path = input("Введите путь к выходному файлу: ")

def generate_random_numbers(filename):
    with open(filename, "w") as f:
        for i in range(10):
            f.write(str(random.randint(1, 100)) + "\n")

def find_prime_numbers(filename, output_filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line.strip()))
    primes = []
    for num in numbers:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    with open(output_filename, "w") as f:
        for prime in primes:
            f.write(str(prime) + "\n")
    print(f"Найдено {len(primes)} простых чисел")

def calculate_factorials(filename, output_filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line.strip()))
    factorials = []
    for num in numbers:
        factorial = math.factorial(num)
        factorials.append(factorial)
    with open(output_filename, "w") as f:
        for factorial in factorials:
            f.write(str(factorial) + "\n")
    print(f"Рассчитаны факториалы для {len(factorials)} чисел")

t1 = threading.Thread(target=generate_random_numbers, args=[input_path])
t2 = threading.Thread(target=find_prime_numbers, args=[input_path, output_path + "_primes.txt"])
t3 = threading.Thread(target=calculate_factorials, args=[input_path, output_path + "_factorials.txt"])


t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

    # 3
# input_path = input("Введите путь к входному файлу (в формате имяфайла.txt): ")
# output_path = input("Введите путь к выходному файлу (в формате имяфайла.txt): ")
#
# def directorian_one(filename, output_filename):
#     with open(filename, 'r') as f:
#         print(f'Окрыт файл {filename}')
#         with open(output_filename, 'w') as f1:
#             print(f'Открыт файл {output_filename}')
#             for line in f:
#                 f1.write(line)
#                 print(f'Содержимое файла {input_path} перенесено.')
#
#
# t1 = threading.Thread(target=directorian_one, args=[input_path, output_path])
#
# t1.start()
# t1.join()


    # 3
old_dir = input('Введите путь к исходной директории: ')
new_dir = input('Введите путь к новой директории: ')

def copy_files(old_dir, new_dir):
    files = os.listdir(old_dir)
    os.makedirs(new_dir, exist_ok=True)

    for file in files:
        current_file = os.path.join(old_dir, file)
        new_file = os.path.join(new_dir, file)

        if os.path.isfile(current_file):
            with open(current_file, 'rb') as f1, open(new_file, 'wb') as f2:
                f2.write(f1.read())
        elif os.path.isdir(current_file):
            copy_files(current_file, new_file)


copy_thread = threading.Thread(target=copy_files, args=(old_dir, new_dir))

copy_thread.start()
copy_thread.join()


print(f'Копирование завершено!')


    # 4
class FileSearcher:
    def __init__(self, directory_path, search_word):
        self.directory_path = directory_path
        self.search_word = search_word
        self.found_files = []

    def search_files(self):
        for root, dirs, files in os.walk(self.directory_path):
            for filename in files:
                filepath = os.path.join(root, filename)
                if self.search_word in open(filepath).read():
                    self.found_files.append(filepath)

class TextEditor:
    def __init__(self):
        self.banned_words = []

    def load_banned_words(self, filepath):
        with open(filepath) as f:
            self.banned_words = f.read().splitlines()

    def censor_text(self, text):
        for banned_word in self.banned_words:
            text = text.replace(banned_word, '**ЦЕНЗУРА**')
        return text

def main():
    directory_path = input('Введите путь к директории: ')
    search_word = input('Введите слово для поиска: ')
    banned_words_file = input('Введите путь к файлу с запрещенными словами: ')
    output_file = input('Введите имя файла для сохранения результата: ')

    file_searcher = FileSearcher(directory_path, search_word)
    file_searcher_thread = threading.Thread(target=file_searcher.search_files)

    file_searcher_thread.start()
    file_searcher_thread.join()

    text_editor = TextEditor()
    text_editor.load_banned_words(banned_words_file)

    with open(output_file, 'w') as f:
        for found_file in file_searcher.found_files:
            f.write(open(found_file).read())

    with open(output_file, 'r') as f:
        text = f.read()

    censored_text = text_editor.censor_text(text)

    with open(output_file, 'w') as f:
        f.write(censored_text)

    print('Все операции выполнены!')

if __name__ == '__main__':
    main()
