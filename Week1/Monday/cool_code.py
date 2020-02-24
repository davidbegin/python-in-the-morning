from dis import dis
import opcode

import os.path

sub_dir = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(sub_dir)

# We have to use os.path.join, versus just string concat
# to handle windows as well as if theres a / or not
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')

print(Path('.') == Path.cwd())
print(Path('.').resolve())
print(Path.cwd())





from glob import glob

top_level_csv_files = glob('*.csv')
all_csv_files = glob('**/*.csv', recursive=True)




# Which do yall think is more pythonic?

# Suprising
Path('src') / '.editorconfig'
# isidentical


# Most explict
Path('src').joinpath('.editorconfig')

Path('src', '.editorconfig')

Path('src/.editorconfig')
