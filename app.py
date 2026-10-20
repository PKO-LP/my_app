from tkinter import *

root = Tk()
root.title("my.gui.app")
root.geometry("251x251")
root.iconbitmap(default="123123.ico")

clicks = 0

def click_button():
    global clicks
    clicks += 1
    btn.config(text=f"Кликов: {clicks}")
    if clicks == 10:
        label = Label(root, text="hello")
        label.pack()
    elif clicks == 20:
     label = Label(root, text="user")
     label.pack()

       

btn = Button(root, text=f"Кликов: {clicks}", command=click_button)
btn.pack(pady=50)
root.mainloop()