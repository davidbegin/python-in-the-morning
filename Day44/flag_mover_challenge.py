print("\033c")

from pathlib import Path
import glob
import os
from tqdm import tqdm

# Challenge:
# Take a list of items in a folder and nest them underneath a folder
# of the root of their name

for flag in tqdm([flag for flag in Path("flags/").glob("*.gif")]):
    flag_name = flag.parts[1][0:2]
    Path(f"flags/{flag_name}").mkdir()
    flag.rename(f"flags/{flag_name}/{flag_name}.gif")
