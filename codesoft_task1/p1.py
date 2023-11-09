#calculator
from tkinter import *
from tkinter.messagebox import *

def click(event):
	global scvalue
	text = event.widget.cget("text")
	# print(text)
	current_value = scvalue.get()

	if text == "=":
		try:
			if current_value.isdigit():
				value = int(current_value)
			else:
				value = eval(current_value)
			scvalue.set(value)
			screen.update()
		except SyntaxError:
			showerror("Error", "Invalid Expression")
			screen.delete(0,END)
			screen.focus()
		except ZeroDivisionError:
			showerror("Error","Cannot Divide by Zero")
			screen.delete(0,END)
			screen.focus()
		except Exception as e:
			showerror("Error","invalid Expression")
			screen.delete(0,END)
			screen.focus()
	elif text == "AC":
		scvalue.set("")
		screen.update()
	elif text == "<---":
		scvalue.set(current_value[:-1])
		screen.update()
	else:
		if len(current_value) >= 20:
			showwarning("Warning", "Max character limit reached")
			screen.delete(0,END)
			screen.focus()
		else:
			scvalue.set(current_value + text)
			screen.update()
	

root=Tk()
root.title("My Calculator")
root.geometry("320x560+250+30")
root.configure(bg="black")
#root.iconbitmap("calculator1.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font=("Arial",30,"bold"),justify=RIGHT,width=15,bg="black",fg="white")
screen.pack(pady=10)

frame=Frame(root,bg="black")
btn=Button(frame,text="AC",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=6,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="%",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=6,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="<---",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=6,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="/",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=6,pady=12)
btn.bind("<Button-1>",click)
frame.pack()


frame=Frame(root,bg="black")
btn=Button(frame,text="9",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="8",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="7",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="*",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="black")
btn=Button(frame,text="6",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="5",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="4",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="-",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=13,pady=12)
btn.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="black")
btn=Button(frame,text="3",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=12,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="2",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=12,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="1",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=12,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="+",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=12,pady=12)
btn.bind("<Button-1>",click)
frame.pack()

frame=Frame(root,bg="black")
btn=Button(frame,text="00",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=11,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="0",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=11,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text=".",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="white")
btn.pack(side=LEFT,padx=11,pady=12)
btn.bind("<Button-1>",click)
btn=Button(frame,text="=",font=("Arial",20,"bold"),padx=8,pady=10,bg="black",fg="orange")
btn.pack(side=LEFT,padx=11,pady=12)
btn.bind("<Button-1>",click)
frame.pack()

root.mainloop()