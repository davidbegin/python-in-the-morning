print("\033c")

import asyncio

async def factorial(name, number):
    print("Pausing for Sleep")
    await asyncio.sleep(10)
    print("We have awoken")

    with open(f"{name}.txt", "w") as f1:
        f1.write(str(number))

    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(0.1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return name


await def slow_func():


async def main():
    print("Lets Create a Task")
    task = asyncio.shield(factorial("A", 2))
    # task = asyncio.create_task(factorial("A", 2))
    print("Lets Cancel a Task")
    task.cancelled()









    # Schedule three calls *concurrently*:
    # return await asyncio.gather(
    #     factorial("A", 2),
    #     factorial("B", 3),
    #     factorial("C", 4),
    #     return_exceptions=True
    # )

    # 

    # return_exceptions=False

result = asyncio.run(main())

print(f"Result of Gather: {result}")

