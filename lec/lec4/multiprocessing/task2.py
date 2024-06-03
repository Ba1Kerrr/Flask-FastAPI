import multiprocessing
import time

'''Эта программа создает 5 процессов и запускает функцию worker() в каждом из них. 
Функция worker() просто выводит сообщение о запуске процессаа, ждёт 3 секунды и сообщает о завершении. 
Весь код работает многопроцессорно, но в отличие от предыдущего примера, 
процессы запускаются и завершаются последовательно, блокируя выполнение программы на время выполнения каждого процесса.
'''


def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
    for p in processes:
        p.start()
        p.join()
    print("Все процессы завершили работу")
