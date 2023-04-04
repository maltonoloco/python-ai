import tkinter as tk
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import ecc_operations as ecc

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Benutzeroberfläche")
        self.master.geometry("600x400")
        self.button_frame = tk.Frame(master)

        self.button1 = tk.Button(self.button_frame, text="Knopf 1")
        self.button2 = tk.Button(self.button_frame, text="Knopf 2")

        self.button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.entry1 = tk.Entry()
        self.entry2 = tk.Entry()

        self.button1.pack(side=tk.LEFT)
        self.button2.pack(side=tk.LEFT)
        self.entry1.pack(side=tk.LEFT)
        self.entry2.pack(side=tk.LEFT)

        self.button_frame.pack()

root = tk.Tk()
gui = GUI(root)

root.mainloop()

        



