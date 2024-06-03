import threading

'''Эта программа создает 5 потоков и запускает функцию increment() в каждом из них. 
Функция increment() увеличивает значение глобальной переменной counter на 1 миллион раз. 
Весь код работает многопоточно, но из-за того, что несколько потоков работают с одной переменной, 
может возникнуть проблема гонки данных (race condition), 
когда результат выполнения программы может быть непредсказуемым.
'''

counter = 0


def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f"Значение счетчика: {counter:_}")


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Значение счетчика в финале: {counter:_}")
