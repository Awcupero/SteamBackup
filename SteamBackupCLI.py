import os
import math
from pathlib import Path
import shutil



source = 'E:\\Games\\Steam\\steamapps\\common\\'  # The file or directory to backup
destination = 'C:\\Users\\Tcupe\\Desktop'  # The location to store the backups in
archive = "zip"
loop = True


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
    archive = "zip"
    loop = True

    try:
        base = os.path.basename(source)
        shutil.make_archive(base, archive, source)
        shutil.move('%s.%s'%(base,archive), destination)
        print("Backup Complete")
                
    except KeyboardInterrupt:
        print("Backup Canceled")
    except OSError:
        print("Backup Error")

def make_list():
    try:
        files = os.listdir(source)
        print("Steam Game Backuper CLI 1.0".center(40,"-"))

        for i, dest in enumerate(files, 1):
            print("[%d]. %s" % (i, dest),convert_size(get_directory_size(f"{source}{dest}")))
    except OSError:
        print("Incorrect Directory")
    except KeyboardInterrupt:
        print("Exited by user")


while loop:
    make_list()
    print("Type exit to end program")
    for dest in enumerate(os.listdir(source)):
        
        x = input("Please chose  game to archive :")

        if x == "1":     
            print("Menu 1 has been selected")
        #os.system('cls||clear')

            if x == "exit":
                break

#To do
#Have menu scale base on number of folders
#Get backup working with program selection
#testing github
