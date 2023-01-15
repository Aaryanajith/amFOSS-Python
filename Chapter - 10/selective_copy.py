import shutil as sh
from pathlib import Path
import os

p = Path.home()

# sh.copy(p / 'spam.txt', p / 'Chapter10')

for folderName, subfolders, filenames in os.walk(p):

     for file in filenames:

         if file.endswith(".pdf",".jpg"):

                filepath = os.path.join(os.path.abspath(folderName), file)

