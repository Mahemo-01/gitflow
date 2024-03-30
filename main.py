import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

# Title txt
title_label = ttk.Label(master = window, text = 'Miles to km', font = 'Calibri 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar() # guarda y actualiza valores en otra var
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert')

entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# Output label
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'km', 
    font = 'Calibri 16',
    textvariable = output_string)
output_label.pack(pady = 5)

# loop run my window
window.mainloop()