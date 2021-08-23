from tkinter import *
from tkinter import filedialog,messagebox
from functools import partial


def cut():
    if not source_name_label.cget("text"):
        messagebox.showerror("error","Choose mp3 source file!")  
        return
    if not destination_name_label.cget("text"):
        messagebox.showerror("error","Choose destination folder!")  
        return
    if cut_type_value.get() == 'One cut':
        pass
    elif cut_type_value.get() == 'Every period':
        pass
    else:
        pass

def about():
    messagebox.showinfo("ABouT","Tool developed by f4khRi\n <f4khri@gmx.com>")  

def update_cut_type_label(cut_type_value):
    if cut_type_value.get() == 'One cut':
        one_cut_from_label.grid(row=10,column=0, sticky=W)
        one_cut_from_entry.grid(row=10,column=1, sticky=W)
        one_cut_to_label.grid(row=10,column=2, sticky=W)
        one_cut_to_entry.grid(row=10,column=3, sticky=W)
        every_period_entry.grid_remove()
        multi_cut_details.grid_remove()
    elif cut_type_value.get() == 'Every period':
        every_period_entry.grid(row=10,column=0, sticky=W)
        one_cut_from_label.grid_remove()
        one_cut_from_entry.grid_remove()
        one_cut_to_label.grid_remove()
        one_cut_to_entry.grid_remove()
        multi_cut_details.grid_remove()
    else: # Multi cut
        multi_cut_details.grid(row=10,column=0, sticky=W)
        one_cut_from_label.grid_remove()
        one_cut_from_entry.grid_remove()
        one_cut_to_label.grid_remove()
        one_cut_to_entry.grid_remove()    
        every_period_entry.grid_remove()

def get_source_file():
    source_name = filedialog.askopenfilename(title="Select your mp3 track", filetypes=(("mp3 Music Files","*.mp3"),("m4a Music Files","*.m4a")))
    source_name_label.grid(row=0,column=2,sticky=W, pady=5)
    source_name_label.configure(text=source_name)

def get_destination():
    destination_name = filedialog.askdirectory(title="Select destination folder")
    destination_name_label.grid(row=1,column=2,sticky=W, pady=5)
    destination_name_label.configure(text=destination_name)

# main app window
root_app = Tk()
root_app.title('::: MP3 CuTTeR Tool :::')
root_app.resizable(False,False)

#labels
source_label = Label(root_app, text="Source")
source_name_label= Label(root_app, text="")
destination_label = Label(root_app, text="Destination")
destination_name_label= Label(root_app, text="")
one_cut_from_label = Label(root_app, text="From")
one_cut_to_label = Label(root_app, text="To")

#entries
one_cut_from_entry = Entry(root_app, textvariable=StringVar(root_app))
one_cut_from_entry.insert(0, "hh:mm:ss")
one_cut_to_entry = Entry(root_app, textvariable=StringVar(root_app))
one_cut_to_entry.insert(0, "hh:mm:ss")
every_period_entry = Entry(root_app, textvariable=StringVar(root_app))
every_period_entry.insert(0, "hh:mm:ss")
multi_cut_details = Text(root_app,height=8, width=20)
multi_cut_details.insert(1.0, "hh:mm:ss - hh:mm:ss\nhh:mm:ss - hh:mm:ss\nhh:mm:ss - hh:mm:ss")

cut_type = ['One cut', 'Every period', 'Multi cut']
cut_type_value = StringVar(root_app, 'one_cut')
for i, value in enumerate(cut_type, 1):
    cut_type_label = Label(root_app, text=value)
    cut_type_radiobutton = Radiobutton(root_app, variable=cut_type_value, value=value,
                              command=partial(update_cut_type_label, 
                                              cut_type_value))
    cut_type_label.grid(row=i+3, column=0,sticky=W)
    cut_type_radiobutton.grid(row=i+3, column=1,sticky=W)

#buttons
source_btn = Button(root_app, text="Choose mp3 source file   ", command=partial(get_source_file))
destination_btn = Button(root_app, text="Choose destination folder", command=partial(get_destination))
cut_btn = Button(root_app, text="Cut now", command=partial(cut))
about_btn = Button(root_app, text="About", command=partial(about))


#grid
source_label.grid(row=0, column=0, sticky=W, pady=5)
source_btn.grid(row=0, column=1, sticky=W, pady=5)
destination_label.grid(row=1, column=0, sticky=W, pady=5)
destination_btn.grid(row=1, column=1, sticky=W, pady=5)

cut_btn.grid(row=22, column=0, columnspan=3, sticky=W,padx=5, pady=10)
about_btn.grid(row=22, column=2, sticky=E,padx=5, pady=10)

# run infinitely
root_app.mainloop()


