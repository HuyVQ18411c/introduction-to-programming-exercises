import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def close():
    replay = messagebox.askquestion('Quit?', "Are you sure?")
    if replay == 'yes':
        window.destroy()

btn_close = tk.Button(window, text='Close', command=close)
btn_close.place(x=50, y=50)

window.title('Example App')
window.mainloop()
