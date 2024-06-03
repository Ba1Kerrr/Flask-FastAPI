import asyncio
'''Эта программа демонстрирует асинхронный код с использованием функции asyncio.gather(), 
которая позволяет запускать несколько задач параллельно и ожидать их завершения. 
В функции count() с помощью ключевого слова await осуществляется ожидание выполнения операции asyncio.sleep(). 
В функции main() создаются три задачи с помощью функции count(), 
которые запускаются параллельно с помощью функции asyncio.gather(). 
Результаты выполнения задач выводятся на экран после их завершения.'''
async def count():
    print("Начало выполнения")
    await asyncio.sleep(1)
    print("Прошла 1 секунда")
    await asyncio.sleep(2)
    print("Прошло еще 2 секунды")
    return "Готово"
async def main():
    result = await asyncio.gather(count(), count(), count())
    print(result)
asyncio.run(main())