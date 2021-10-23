import concurrent.futures
import sys
import re
import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox


def engine():
    for file in files:  # create a loop for matching files and make required manipulations
        file_ext = os.path.splitext(file)[1]
        pattern = r'([\w]+)'
        match = re.search(pattern, file_ext)
        if match:
            folder_name = match.group().upper()
            path1 = path + folder_name
            if not os.path.exists(path1):
                os.mkdir(path1)
            os.chdir(path)
            os.system("move " + '"' + file + '"' + " " + '"' + path1 + '"')
            lst.append(folder_name)


if __name__ == "__main__":

    root = Tk()
    root.withdraw()
    temp_file = tkinter.filedialog.askdirectory(parent=root, initialdir=os.getcwd(),
                                                title="Select a folder to sort")
    path = temp_file + "/"
    files = os.listdir(path)
    lst = []  # empty list

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(engine)

    if len(temp_file) > 0:
        tkinter.messagebox.showinfo(title="Successfully", message="Files sorted")
