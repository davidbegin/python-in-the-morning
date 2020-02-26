from glob import glob

top_level_csv_files = glob('*.csv')
all_csv_files = glob('**/*.csv', recursive=True)

from pathlib import Path

top_level_csv_files = Path.cwd().glob('*.csv')
all_csv_files = Path.cwd().rglob('*.csv')

# Find all *.md files in a directory
# Find all *.md files recursively


# find . -name "*.md" 
# How do I do non-recursive for find
# What is faster find or python

all_csv_files = Path.cwd().rglob('*.csv')
