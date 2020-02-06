print('\033c')

daily_fact = "\033[91m2020 - 2 - 5\n\n\t\033[35m1971 – 2 - 5\n\tAstronauts alledegadly land on the moon in the Apollo 14 mission.\033[0m"

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")

print("\033[34mTest\033[0m")
print("\033[34;1mTest\033[0m")
print("\033[94mTest\033[0m")


from dis import dis
import opcode
import asyncio


loop = asyncio.get_event_loop()

# - We can a future
# - We can do a coroutine
#   - implicitly scheduled to run as a asyncio.Task.

  #loop.run_until_complete()
