print('\033c')

daily_fact = '\033[35;1m2020 - 1 - 31\n\n\t\033[36m59 Years ago on this Day\n\tProject Mercury: Mercury-Redstone 2: Ham the Chimp\n\ttravels into outer space.'

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")

from dis import dis
import opcode
import sys
import time
from tqdm import tqdm

# TypeError: 'float' object cannot be interpreted as an integer

# epic_list = range(sys.maxsize // 2_000_000)

# epic_list = [0]*(sys.maxsize // 2_000_000)

thang = tqdm(range(10000))

for x in thang:
    time.sleep(0.0001)
    pass

# print(list(epic_list))

# breakpoint()


