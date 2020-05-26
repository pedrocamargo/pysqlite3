import urllib.request
import zipfile
import os
from os.path import join, dirname
from shutil import move

pth = 'https://www.sqlite.org/2020/sqlite-amalgamation-3320100.zip'


outfolder = join(dirname(dirname(os.path.abspath(__file__))), 'src')

dest_path = join(outfolder, "sqlite-amalgamation-3320100.zip")
urllib.request.urlretrieve(pth, dest_path)


zipfile.ZipFile(dest_path).extractall(outfolder)


for file in os.walk(outfolder):
    if 'sqlite3.c' in file[2]:
        for item in file[2]:
            move(join(file[0], item), join(outfolder, item))
