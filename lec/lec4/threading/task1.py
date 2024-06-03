import threading
import time

'''Эта программа создает 5 потоков и запускает функцию worker() в каждом из них. 
Функция worker() занимает 3 секунды на выполнение. Весь код работает многопоточно, 
то есть каждый поток работает независимо от других, и выполнение программы не блокируется на время выполнения функции.
'''


def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Все потоки завершили работу")
