import asyncio


async def async_func():
    print('Запуск ...')
    await asyncio.sleep(1)
    print('... Готово!')

async def main():
    await async_func()


asyncio.run(main())