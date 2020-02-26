print('\033c')
import time

daily_fact = '\033[35;1m2020 - 2 - 3\n\n\t\033[36m36 Years ago on this Day\n\tElizabeth Holmes,\n\tAmerican fraudster,\n\tfounder of Theranos\n\twas born.'

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")


from dis import dis
import opcode
import threading

def spin():
    icon = "†"
    print('\033c')
    print(f"\n\t\033[36m{icon}\033[0m")
    tim.sleep(10)

class BeginThread(threading.Thread):
    def run(self):
        icon = "†"
        print('\033c')
        print(f"\n\t\033[36m{icon}\033[0m")
        time.sleep(10)

# thread = threading.Thread(target=BeginThread)

thread = threading.Thread(target=spin)
breakpoint()
thread.start()
# thread.join()

# spinner = threading.Thread(target=spin, args=('thinking!', done))
