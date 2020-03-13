import timeit

print('\033c')
print("\n\t\t\033[36;1;6;4mPerf Tests!\033[0m\n\n")


TIMES = 100000

SETUP = """
from glob import glob
from pathlib import Path

def glob_time():
    top_level_csv_files = glob('*.csv')
    all_csv_files = glob('**/*.csv', recursive=True)

def pathlib_time():
    top_level_csv_files = Path.cwd().glob('*.csv')
    all_csv_files = Path.cwd().rglob('*.csv')
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.4f}'.format(x) for x in res))


clock("glob_time()   : ", "glob_time()")
clock("pathlib_time(): ", "pathlib_time()")
