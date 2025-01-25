import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles = entryInt.get()
    km = miles * 1.61
    outputstr.set(km)

window = ttk.Window(themename="journal")
window.title("Converter")
window.geometry("300x150")

title = ttk.Label(master=window , text="Miles to Km converter", font="Calibri 24 bold")
title.pack()

input_frame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt)
button = ttk.Button(master=input_frame,text="convert", command=convert)
input_frame.pack(pady=10)
entry.pack(side="left", padx=0)
button.pack(side="left", padx=0)

outputstr = tk.StringVar()
output_label = ttk.Label(master=window, text="output" , font="Calibri 24", textvariable=outputstr)
output_label.pack(pady=5)


window.mainloop()