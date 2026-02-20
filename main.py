import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

window = Tk()
window.title("Secret Notes")
window.minsize(width =600,height =400)
window.config(padx = 10, pady = 10)

def click_button_save():
    title = entry1.get()
    secret = text.get("1.0", "end-1c")
    key = entry2.get()

    if len(title) == 0 or len(secret) == 0 or len(key) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
        return

    secret_encrypted = encode(key, secret)
    try:
        with open("secret.txt", "w", encoding="utf-8") as file:
            file.write(f"\n{title}\n{secret_encrypted}")
    except FileNotFoundError:
        with open("secret.txt", "w", encoding="utf-8") as file:
            file.write(f"\n{title}\n{secret_encrypted}")
    finally:
        entry1.delete(0, END)
        text.delete("1.0", END)
        entry2.delete(0, END)

def click_button_decrypt():
    key = entry2.get()

    if len(key) == 0:
        messagebox.showinfo(title="Error!", message="Please enter master key.")
        return

    try:
        with open("secret.txt", "r", encoding="utf-8") as file:
            lines = file.read().splitlines()

        lines = [line for line in lines if line != ""]

        if len(lines) < 2:
            messagebox.showinfo(title="Error!", message="secret.txt format is wrong or empty.")
            return

        title_from_file = lines[0]
        secret_encrypted_from_file = lines[1]

        decrypted_secret = decode(key, secret_encrypted_from_file)

        text.delete("1.0", END)
        text.insert("1.0", decrypted_secret)

        entry1.delete(0, END)
        entry1.insert(0, title_from_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="secret.txt not found.")
    except:
        messagebox.showinfo(title="Error!", message="Wrong master key or corrupted data.")

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
button2 = tkinter.Button(text = "Decrypt", command = click_button_decrypt)
button2.pack()

window.mainloop()