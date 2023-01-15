import os
from pathlib import Path

p = Path.home()

files=os.listdir(p)

q=Path.cwd()
print(q)

for file in files:
    fi=os.path.getsize(file)
    if fi >100:
        fi_rel=os.path.relpath(file)
        print(fi ,fi_rel)