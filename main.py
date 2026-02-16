import tkinter
from tkinter import *
from PIL import ImageTk, Image
import random
import string

window = Tk()
window.title("Secret Notes")
window.minsize(width =600,height =400)
window.config(padx = 10, pady = 10)

def click_button_save():
    title = entry1.get()
    secret = text.get("1.0", END)
    key = entry2.get()

    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    with open("secret.txt", "w", encoding="utf-8") as file:
        file.write(title + "\n")
        file.write(random_password + "\n")

    entry1.delete(0, END)
    text.delete("1.0", END)
    entry2.delete(0, END)

def click_button_decrypt():
    pass

#image
img = ImageTk.PhotoImage(Image.open("topsecret.jpg"))
img_label = Label(window, image=img)
img_label.pack()

#label
label1 = Label(text ="Enter your title")
label1.config(font=("Arial",12))
label1.pack()

#entry1
entry1 = Entry(width = 40)
entry1.pack()

#label2
label2 = Label(text= "Enter your secret")
label2.config(font=("Arial",12))
label2.pack()

#text
text = Text(width=30, height=10)
text.pack()

#label3
label3 = Label(text = "Enter master key",)
label3.config(font=("Arial",12))
label3.pack()

#entry2
entry2 = Entry(width = 40)
entry2.pack()

#button
button1 = tkinter.Button(text = "Save & Encrypt", command = click_button_save)
button1.pack()

#button2
button2 = tkinter.Button(text = "Decrypt", command = click_button_save)
button2.pack()

window.mainloop()