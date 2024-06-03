import time
from pathlib import Path
import threading
'''Создать программу, которая будет производить подсчет количества слов 
в каждом файле в указанной директории и выводить результаты в консоль.
Используйте потоки.
'''

def process_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        contents = f.read()
        contents_world = len(contents.split())
        print(f"{f.name} содержит {contents_world} слов(а).")


def main():
    dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    threads = []
    for file_path in file_paths:
        t = threading.Thread(target=process_file(file_path))
        threads.append(t)
        t.start

    for t in threads:
        t.join


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'{time.time() - start_time:.2f}')
