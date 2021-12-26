import os
import tkinter as tk
from tkinter import filedialog
import time
import pathlib
import shutil

folderpath = ""
file_name = "path.txt"
def sortAll(filepath, file):
    f = []
    file.close()
    while True:
        allFiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]
        for fileName in allFiles:
            fileSuffix = pathlib.Path(filepath + "/" + fileName).suffix
            if(os.path.exists(filepath + "/" + fileSuffix)):
                os.rename(filepath + "/" + fileName, filepath + "/" + fileSuffix + "/" + fileName)
            else:
                if(fileSuffix == ""):
                    if(os.path.exists(filepath + "/" + fileSuffix)):
                        os.rename(filepath + "/" + fileName, filepath + "/" + fileSuffix + "/" + fileName)
                    else:
                        os.makedirs("Others")
                else:
                    os.makedirs(filepath + "/" + fileSuffix)
                    os.rename(filepath + "/" + fileName, filepath + "/" + fileSuffix + "/" + fileName)
        time.sleep(300)
        
try:
    file = open(file_name, "r")
    sortAll(file.readline())
except IOError:
    folderpath = filedialog.askdirectory()
    root = tk.Tk()
    root.withdraw() 
    file = open(file_name, "w")
    file.write(folderpath);
    file.close()
    sortAll(folderpath, file)


