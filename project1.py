from pathlib import Path
# p = Path('/Users/gageludlow/Projects')

p = Path(input())

for child in p.iterdir():
    if child.is_dir:
        
    print(child)

