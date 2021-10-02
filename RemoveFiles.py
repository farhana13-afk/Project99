import os
import time
import shutil

path = input("Enter the path of the directory to be sorted ")

days = int(input("Enter the number of days you want to keep file: "))
seconds = time.time() - (days * 24 * 60 * 60)
exist = os.path.exists(path)

if(exist == True):
    os.walk(path)
    os.path.join(path)
    ctime = os.stat(path).st_ctime
    if(ctime > seconds):
        if(exist):
            os.remove(path)
        else:
            shutil.remove()
else:
    print("Not Found, path doesn't exist")