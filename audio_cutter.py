from tkinter import *
from tkinter import filedialog
from functools import partial


def cut():
    pass

def update_cut_type_label(cut_type_value):
    if cut_type_value.get() == 'One cut':
        one_cut_label.grid(row=10,column=0,padx=5, pady=5)
        one_cut_from_label.grid(row=10,column=1,padx=5, pady=5)
        one_cut_from_entry.grid(row=10,column=2,padx=5, pady=5)
        one_cut_to_label.grid(row=10,column=3,padx=5, pady=5)
        one_cut_to_entry.grid(row=10,column=4,padx=5, pady=5)
    elif cut_type_value.get() == 'Every period':
        every_period_entry.grid(row=10,column=0,padx=5, pady=5)
    else: # Multi cut
        multi_cut_details.grid(row=10,column=0,padx=5, pady=5)    

def get_source_file():
    source_name = filedialog.askopenfilename(title="Select your track", filetypes=(("mp3 Music Files","*.mp3"),("m4a Music Files","*.m4a")))
    source_name_label.grid(row=0,column=2,padx=5, pady=5)
    source_name_label.configure(text=source_name)

def get_destination():
    destination_name = filedialog.askdirectory(title="Select destination folder")
    destination_name_label.grid(row=1,column=2,padx=5, pady=5)
    destination_name_label.configure(text=destination_name)

# main app window
root_app = Tk()

root_app.title(':: Audio CuTTeR Tool ::')
root_app.geometry('800x350')
root_app.resizable(False,False)

#labels
source_label = Label(root_app, text="Source")
source_name_label= Label(root_app, text="")
destination_label = Label(root_app, text="Destination")
destination_name_label= Label(root_app, text="")
one_cut_label = Label(root_app, text="One cut")
one_cut_from_label = Label(root_app, text="From")
one_cut_to_label = Label(root_app, text="To")
every_period_label = Label(root_app, text="Every")
multi_cut_label = Label(root_app, text="Multi cut")

#entry
one_cut_from_entry = Entry(root_app, textvariable=StringVar(root_app))
one_cut_to_entry = Entry(root_app, textvariable=StringVar(root_app))
every_period_entry = Entry(root_app, textvariable=StringVar(root_app))
multi_cut_details = Text(root_app, height = 5, width = 52)

cut_type = ['One cut', 'Every period', 'Multi cut']
cut_type_value = StringVar(root_app, 'one_cut')
for i, value in enumerate(cut_type, 1):
    cut_type_label = Label(root_app, text=value)
    cut_type_radiobutton = Radiobutton(root_app, variable=cut_type_value, value=value,
                              command=partial(update_cut_type_label, 
                                              cut_type_value))
    cut_type_label.grid(row=i+3, column=0)
    cut_type_radiobutton.grid(row=i+3, column=1)

#buttons
source_btn = Button(root_app, text="Choose file", command=partial(get_source_file))
destination_btn = Button(root_app, text="Choose destination folder", command=partial(get_destination))
cut_btn = Button(root_app, text="Cut now", command=partial(cut))


#grid
source_label.grid(row=0,column=0,padx=5, pady=5)
source_btn.grid(row=0,column=1,padx=5, pady=5)
destination_label.grid(row=1,column=0,padx=5, pady=5)
destination_btn.grid(row=1,column=1,padx=5, pady=5)

cut_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

# run infinitely
root_app.mainloop()


