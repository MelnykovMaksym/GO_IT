import sys
import re
import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import asyncio


async def engine():
    for file in files:  # create a loop for matching files and make required manipulations
        file_ext = os.path.splitext(file)[1]  # define file extension
        # print(f'File_ext {file_ext}')
        pattern = r'([\w]+)'  # create the pattern
        match = re.search(pattern, file_ext)  # extract extension
        # print(f"match {match}")
        if match:
            folder_name = match.group().upper()  # use group() - If a group matches multiple
            # times, only the last match is accessible
            # print(folder_name {folder_name}')
            path1 = path + folder_name  # create the path to move files
            # print(f"path1 {path1}")
            if not os.path.exists(path1):
                os.mkdir(path1)
            os.chdir(path)  # establish directory to next manipulations
            # print(f"os.chdir {os.chdir}")
            os.system("move " + '"' + file + '"' + " " + '"' + path1 + '"')  # replace files



async def main():
    await asyncio.gather(engine())


if __name__ == "__main__":

    root = Tk()
    root.withdraw()
    temp_file = tkinter.filedialog.askdirectory(parent=root, initialdir=os.getcwd(),
                                                title="Select a folder to sort")
    path = temp_file + "/"
    files = os.listdir(path)
    asyncio.run(main())

    if len(temp_file) > 0:
        tkinter.messagebox.showinfo(title="Successfully", message="Files sorted")
