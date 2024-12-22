import asyncio
import time


def task(taskName):
    curtime = time.perf_counter() - start_time
    print(f"{curtime:.2f}:\t{taskName}")


async def WakeUp():
    task("Проснуться")
    await  asyncio.sleep(0.2)

async def Food():
    task("Поставить чайник")
    await asyncio.sleep(2)
    task("Заварить чай")
    await asyncio.sleep(0.5)
    task("Положить еду в микроволновку")
    await asyncio.sleep(2)
    task("Достать разогретую еду")
    await asyncio.sleep(0.5)


async def Routine():
    task("Умыться")
    await asyncio.sleep(1)
    task("Почистить зубы")
    await asyncio.sleep(4)
    task("Поесть")
    await asyncio.sleep(1)


async def Leave():
    task("Одеться")
    await asyncio.sleep(0.5)
    task("Выдвигаться в школу")





async def main():
    await WakeUp()

    task_1 = asyncio.create_task(Food())
    task_2 = asyncio.create_task(Routine())
    await asyncio.gather(task_1, task_2)

    #выход осуществляется после всего прочего
    await Leave()

#Подсчёт затраченного  времени
start_time = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - start_time

print(f"Утро заняло {round(elapsed*10)} минут")