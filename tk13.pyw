import tkinter as tk
root = tk.Tk()
root.geometry('300x200')
lb = tk.Label(text='This is label. This is a Label. this is a Label. ')
ms = tk.Message(text='This is s Message. This is a message. This is a Message. ')
[widget.pack() for widget in (lb, ms)]
root.mainloop()