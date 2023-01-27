import webbrowser
import tkinter as tk 

def open_url(): 
    webbrowser.open_new(entry.get())

root = tk.Tk() 
root.title("Simple browser")
root.geometry("300x300")

entry = tk.Entry(root) 
entry.pack() 

open_button = tk.Button(root, text="Open", command=open_url)
open_button.pack() 

root.mainloop()

