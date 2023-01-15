from pathlib import Path
import glob,os
import re

p = Path.home()
os.chdir(p)

ur_regex = re.compile(input('Enter your Regex expression :'))

for i in glob.glob("*.txt"):
    currentFile = open(i)
    file = currentFile.read() 
    print(file)
    searchedText = ur_regex.search(file)
    print(searchedText.group() if searchedText else None)
