###########################################################
# Author: Anthony Cupero
# Version: 1.1
# Language: python 3.9
# A commandline program use to back up steam game to remote directory 
############################################################

import os
import math
from pathlib import Path
import shutil
from tqdm import tqdm


source = 'E:\\Games\\Steam\\steamapps\\common\\'  # The file or directory to backup
backupdestination = 'C:\\Users\\Tcupe\\Desktop\\'  # The location to store the backups in
archive = "zip"
loop = True
Gamelist = []
FSize = []
GName = []
Pad = []
Title = []
files = os.listdir(source)
Centerline = 10



def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_directory_size(source):
    """Returns the `directory` size in bytes."""
    
    total = 0

    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(source):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(source)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total
   
def make_archive(source, destination):
    try:
        base = os.path.basename(source)
        shutil.make_archive(base, archive, source)
        shutil.move('%s.%s'%(base,archive), destination)
        print("Backup Complete")
                
                
    except KeyboardInterrupt:
        print("Backup Canceled")
    except OSError as BackupError:
        print(BackupError)    

def make_list(): 

    for Length in files: 
        Pad.append(len(Length)) 
    y = int(max(Pad)+5)

    for i in range(0, len(GName)):
        print((f"{GName[i] :<{y}}{'|' :^{Centerline}}{FSize[i] :>10}")) 
        Title.append(len((f"{GName[i] :<{y}}{'|' :^{Centerline}}{FSize[i] :>10}")))

def title():
    try:

        for i, dest in enumerate(files, 1):
            Gamelist.append(dest)
            FSize.append(convert_size(get_directory_size(f"{source}{dest}")))
            GName.append("[%d] %s" % (i, dest))

    except OSError:
        print("Incorrect Directory")


    for Length in files: 
        Pad.append(len(Length)) 
    y = int(max(Pad)+5)

    for i in range(0, len(GName)):
        Title.append(len((f"{GName[i] :<{y}}{'|' :^{Centerline}}{FSize[i] :>10}")))

    print("Steam Game Backuper CLI 1.0".center(Title[0],"-"))

while True:
    try:
        
        title()
        make_list()
        for dest in enumerate(os.listdir(source)):
            x = int(input("Please chose game to archive :"))
            path = source + Gamelist[x-1] 
            make_archive(path , backupdestination)
    
    
    except KeyboardInterrupt:
        os.system('cls||clear')
        print("Exited by user")
    break
    
