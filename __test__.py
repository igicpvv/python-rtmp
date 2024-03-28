import asyncio
from threading import Thread

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

#asyncio.create_task(main())
thread = Thread(target=lambda : asyncio.run(main()), args=[])
thread.start()
print("AAA")