from tkinter import *
from tkinter import ttk
import time
import webbrowser


currentTab = ()
url = 'https://www.google.com/search?q='


def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "Name-List Search":
        currentTab = 0
    if tab_text == "Address-List Search":
        currentTab = 1
    # print(currentTab)


def count_lines():
    if currentTab == 0:
        listtocount = w1.get()
    elif currentTab == 1:
        listtocount = w2.get()
    with open(listtocount) as g:
        lines = g.readlines()
        print("Lines in List =", len(lines))


container = Tk()
container.title("Multi-Tab-Search-GUI")

tab_parent = ttk.Notebook(container)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

# tab changed event
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)

# Setup Tabs
tab_parent.add(tab1, text='Name-List Search')
tab_parent.add(tab2, text='Address-List Search')

# tab1 contents #########################################################################

# label - tab1 - Name-List Search
# lbl1 = Label(tab1, text="Name-List Search", font=("Arial Bold", 20))
# lbl1.grid(column=1, row=0)

# label - Input Name-List.csv
wLabel1 = Label(tab1, text=" Input Name-List.csv :", font=("Arial", 10), width=20)
wLabel1.grid(column=0, row=0)
# user input - Input Name-List.csv
w1 = Entry(tab1, width=26)
w1.grid(column=1, row=0)
# button - check current tab
chkTabBtn1 = Button(tab1, text="Count Lines", command=count_lines)
chkTabBtn1.grid(column=2, row=0)

# label - Input Address OR State
searchTerm1 = Label(tab1, text=" Input Address OR State :", font=("Arial", 10), width=20)
searchTerm1.grid(column=0, row=1)
# txt entry - Input Address Or State
txt1 = Entry(tab1, width=26)
txt1.grid(column=1, row=1)

# label - Delay in Sec
dly1 = Label(tab1, text=" Delay in Sec :", font=("Arial", 10), width=20)
dly1.grid(column=0, row=2)

# Spinbox - Delay in Sec
combo1 = Spinbox(tab1, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width=5)
combo1.grid(column=1, row=2)


# define clicked action.
def clicked_start1():
    inputlist = w1.get()
    loc = txt1.get()
    usrdly = combo1.get()
    # tab1.title("Performing Search")
    print(inputlist + " " + loc + " " + usrdly)
    with open(inputlist) as f:
        data = f.readlines()
        for x in data:
            y = x.replace(',', '')
            z = y.replace('.', '')
            time.sleep(int(usrdly))
            webbrowser.open_new_tab(url + z + " " + loc)
    print("Tabs Opened.")


# Yes button.
btn = Button(tab1, text="Start", command=clicked_start1)
btn.grid(column=2, row=2)

# tab2 contents #########################################################################

# label - tab2 - Address-List Search
# lbl2 = Label(tab2, text="Address-List Search", font=("Arial Bold", 20))
# lbl2.grid(column=1, row=0)

# label - Input Name-List.csv
wLabel2 = Label(tab2, text=" Input Address-List.csv :", font=("Arial", 10), width=20)
wLabel2.grid(column=0, row=0)
# user input - Input Name-List.csv
w2 = Entry(tab2, width=26)
w2.grid(column=1, row=0)
# button - check current tab
chkTabBtn2 = Button(tab2, text="Count Lines", command=count_lines)
chkTabBtn2.grid(column=2, row=0)

# label - Input Address OR State
searchTerm2 = Label(tab2, text=" Input Provider Name :", font=("Arial", 10), width=20)
searchTerm2.grid(column=0, row=1)
# txt entry - Input Address Or State
txt2 = Entry(tab2, width=26)
txt2.grid(column=1, row=1)

# label - Delay in Sec
dly2 = Label(tab2, text=" Delay in Sec :", font=("Arial", 10), width=20)
dly2.grid(column=0, row=2)
# Spinbox - Delay in Sec
combo2 = Spinbox(tab2, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width=5)
combo2.grid(column=1, row=2)


# define clicked action.
def clicked_start2():
    inputlist = w2.get()
    name = txt2.get()
    usrdly = combo2.get()
    # tab1.title("Performing Search")
    print(inputlist + " " + name + " " + usrdly)
    with open(inputlist) as f:
        data = f.readlines()
        for x in data:
            y = x.replace(',', '')
            z = y.replace('.', '')
            time.sleep(int(usrdly))
            webbrowser.open_new_tab(url + name + " " + z)
    print("Tabs Opened.")


# Yes button.
btn = Button(tab2, text="Start", bg="Green", command=clicked_start2)
btn.grid(column=2, row=2)

#########################################################################################


tab_parent.pack(expand=1, fill='both')

container.mainloop()
