# GUI - Multi-URL-Opener - from user defined list.csv

from tkinter import *
from tkinter.ttk import *
# from os import listdir
# from os.path import isfile, join
import time
import webbrowser

# browser = webbrowser.get('firefox')
url = 'https://www.google.com/search?q='

# populate drop down with files in directory
# f = []
# onlyFiles = [f for f in listdir(
#     "/Users/trevor/PycharmProjects/multi-url-opener/") if isfile(join(
#         "/Users/trevor/PycharmProjects/multi-url-opener/", f))]


windowTitle = "Search Tool"

# define window name and window size.
window = Tk()
window.title(windowTitle)
window.geometry('460x110')

# drop down config
# variable = StringVar(window)
# variable.set(onlyFiles[0])

combo = Spinbox(window, values=(
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
), width=5)

# set delay.
# combo = Combobox(window)
# combo['values'] = (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
# combo.current(1)  # set the selected item.

# initial Hello text.
lbl = Label(window, text="Search by Tab Tool", font=("Arial Bold", 20))
lbl.grid(column=1, row=0)

# label - Select Name List
wLabel = Label(window, text=" Select Name List :", font=("Arial", 10), width=20)
wLabel.grid(column=0, row=1)

# # Option Menu - Select Name List
# w = OptionMenu(window, variable, *onlyFiles)
# w.grid(column=1, row=1)
w = Entry(window, width=26)
w.grid(column=1, row=1)

# label - Input Address OR State
searchTerm = Label(window, text=" Input Address OR State :", font=("Arial", 10), width=20)
searchTerm.grid(column=0, row=2)
# txt entry - Input Address Or State
txt = Entry(window, width=26)
txt.grid(column=1, row=2)

# label - Delay in Sec
dly = Label(window, text=" Delay in Sec :", font=("Arial", 10), width=20)
dly.grid(column=0, row=3)
# Spinbox - Delay in Sec
combo.grid(column=1, row=3)


# define clicked action.
def clickedstart():
    inputlist = w.get()
    loc = txt.get()
    usrdly = combo.get()
    # lbl.configure(text=res + " " + combo.get())
    window.title("Performing Search")
    print(inputlist + " " + loc + " " + usrdly)
    with open(inputlist) as f:
        data = f.readlines()
        for x in data:
            y = x.replace(',', '')
            z = y.replace('.', '')
            time.sleep(int(usrdly))
            webbrowser.open_new_tab(url + z + " " + loc)
        print(data[0])


# Yes button.
btn = Button(window, text="Start", command=clickedstart)
btn.grid(column=3, row=3)
# print(onlyFiles, "\n")
window.mainloop()
