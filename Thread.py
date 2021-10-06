from threading import Thread
import sys
import re
import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

def engine():
    root = Tk()
    root.withdraw()
    temp_file = tkinter.filedialog.askdirectory(parent=root, initialdir=os.getcwd(), title="Select a folder to sort")
    path = temp_file + "/"
    files = os.listdir(path)
    ext = []
    for k in files:
        file_ext = os.path.splitext(k)[1]
        pattern = r'([\w]+)'
        match = re.search(pattern, file_ext)
        if match:
            folder_name = match.group().upper()
            path1 = path + folder_name
            if not os.path.exists(path1):
                os.mkdir(path1)
            os.chdir(path)
            os.system("move " + '"' + k + '"' + " " + '"' + path1 + '"')
            ext.append(folder_name)
    if len(temp_file) > 0:
        tkinter.messagebox.showinfo(title="Successfully", message="Files sorted")

thread = Thread(target=engine)
thread.start()
