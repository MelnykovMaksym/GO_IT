import concurrent.futures
import sys
import re
import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox


def engine():
    for file in files:  # create a loop for matching files and make required manipulations
        file_ext = os.path.splitext(file)[1]  # define file extension
        pattern = r'([\w]+)'  # create the pattern
        match = re.search(pattern, file_ext)  # extract extension
        print(match)
        if match:
            folder_name = match.group().upper()  # use group() - If a group matches multiple
            # times, only the last match is accessible
            path1 = path + folder_name  # create the path to move files
            if not os.path.exists(path1):
                os.mkdir(path1)
            os.chdir(path)  # establish directory to next manipulations
            os.system("move " + '"' + file + '"' + " " + '"' + path1 + '"')  # replace files


if __name__ == "__main__":

    root = Tk()
    root.withdraw()
    temp_file = tkinter.filedialog.askdirectory(parent=root, initialdir=os.getcwd(),
                                                title="Select a folder to sort")
    path = temp_file + "/"
    files = os.listdir(path)


    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(engine)

    if len(temp_file) > 0:
        tkinter.messagebox.showinfo(title="Successfully", message="Files sorted")
