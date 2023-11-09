# random password generator
from random import *
from tkinter import *
root = Tk()
root.title("Password Generator")
root.geometry("700x500+200+100")
root.configure(bg= "#FFD39B")
f=("Arial",30,"bold")

def compute():
	text="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pw=""
	for i in range(8):
		r=randrange(0, len(text) - 1)
		pw=pw+ text[r]
		ans.configure(text=pw)

label=Label(root,text="Password Generator",bg="black",fg="white",font=f)
label.pack(pady=50)
btn=Button(root,text="Generate",font=f,command=compute)
btn.pack(pady=20)
ans=Label(root,font=f,bg="#FFD39B")
ans.pack(pady=20)
root.mainloop()