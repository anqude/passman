from customtkinter import CTkLabel,CTkButton,CTkEntry,CTkScrollableFrame,CTkTabview,CTk,get_appearance_mode,set_widget_scaling,set_window_scaling
from tkinter import PhotoImage
import os
import sys

window = CTk()
scriptdir=os.path.abspath(__file__)

try:
	direct=scriptdir.removesuffix('\PassmanGUI.py')
	assert os.path.isdir(direct), 'You fucked bro'
	
except:
	direct=scriptdir.removesuffix('/PassmanGUI.py')

sys.path.append(direct)



from logics import *
window.title("PassMan by Anqude")


theme=get_appearance_mode()
if theme=="Dark":
	bg_color="#242424"
	fg_color="#dbdbdb"
else:
	fg_color="#242424"
	bg_color="#dbdbdb"
	
scriptdir=os.path.abspath(__file__)
os.chdir(direct)
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/icon.png'))
tabview = CTkTabview(window)
tab_write=tabview.add("Write") # add tab at the end
tab_read=tabview.add("Read")  # add tab at the end
tabview.set("Write")  # set currently visible tab

def get_password():
	fpassword=Password_entry.get()
	return fpassword
def enter():
	Pass_text.pack_forget()
	Password_entry.pack_forget()
	button.pack_forget()
	get_password()
	banan()
	
Password_entry=CTkEntry(window)
Pass_text=CTkLabel(window,text="Password: ")
button=CTkButton(window,text="Log in!", command=enter)

Pass_text.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
Password_entry.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
button.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")

Names=["Website:","Login:","Password:","Create time:"]

def func(index):
	inform=read_info_file(get_password())
	tabview.pack_forget()
	Site_label=CTkLabel(window,text=Names[0])
	Site_val=CTkLabel(window)
	Login_label=CTkLabel(window,text=Names[1])
	Login_val=CTkLabel(window)
	Password_label=CTkLabel(window,text=Names[2])
	Password_val=CTkLabel(window)
	def rewrite():
		Site_val.grid_forget()
		Login_val.grid_forget()
		Password_val.grid_forget()
		CopyLoginB.grid_forget()
		CopyPassB.grid_forget()
		QRShare.grid_forget()
		Site_entry=CTkEntry(window)
		Site_entry.insert(0, inform[index][0])
		Login_entry=CTkEntry(window)
		Login_entry.insert(0, inform[index][1])
		Password_entry=CTkEntry(window)
		Password_entry.insert(0, inform[index][2])
		Site_entry.grid(row=0, column=1,padx=12,pady=10)
		Login_entry.grid(row=1, column=1,padx=12,pady=10)
		Password_entry.grid(row=2, column=1,padx=12,pady=10)
		def save():
			edit_info_file(index,Site_entry.get(),Login_entry.get(),Password_entry.get(),get_password())
			readl()
			DontEdit()
		RewrireButton.configure(command=save,text="Save!")
		ExitButton.grid_forget()
		RewrireButton.grid_forget()
		RewrireButton.grid(row=3, column=0,padx=12,pady=10)
		
		def DontEdit():
			Site_entry.grid_forget()
			Login_entry.grid_forget()
			Password_entry.grid_forget()
			Site_label.grid_forget()
			Login_label.grid_forget()
			Password_label.grid_forget()
			RewrireButton.grid_forget()
			ExitButton.grid_forget()
			func(index)
		ExitButton.configure(command=DontEdit,text="Don`t save!")
		ExitButton.grid_forget()
		ExitButton.grid(row=3, column=1,padx=12,pady=10)
		

	
	def Exit():
		Site_label.grid_forget()
		Site_val.grid_forget()
		Login_label.grid_forget()
		Login_val.grid_forget()
		Password_label.grid_forget()
		Password_val.grid_forget()
		RewrireButton.grid_forget()
		ExitButton.grid_forget()
		ExitButton.grid_forget()
		CopyLoginB.grid_forget()
		CopyPassB.grid_forget()
		QRShare.grid_forget()
		tabview.pack(fill="both", expand=True,anchor='center')
	
	ExitButton=CTkButton(window,command=Exit,text="Exit!")
	Site_val.configure(text=inform[index][0])
	Login_val.configure(text=inform[index][1])
	Password_val.configure(text=inform[index][2])
	Site_label.grid(row=0, column=0,padx=12,pady=10)
	Site_val.grid(row=0, column=1,padx=12,pady=10)
	Login_label.grid(row=1, column=0,padx=12,pady=10)
	Login_val.grid(row=1, column=1,padx=12,pady=10)
	Password_label.grid(row=2, column=0,padx=12,pady=10)
	Password_val.grid(row=2, column=1,padx=12,pady=10)
	RewrireButton=CTkButton(window,command=rewrite,text="🖊",width=10)
	RewrireButton.grid(row=3, column=2,padx=12,pady=10)
	ExitButton.grid(row=3, column=1,padx=12,pady=10)
	def CopyLogin():
		from pyperclip import copy
		copy(inform[index][1])
	CopyLoginB=CTkButton(window,command=CopyLogin,text="📋",width=10)
	def CopyPass():
		from pyperclip import copy
		copy(inform[index][2])

	def genadiy():
		state=qr_image(inform[index][0],inform[index][1],inform[index][2],fg_color,bg_color)
		from tkinter import Toplevel,Label
		from PIL import ImageTk, Image
		if state==True:
			window = Toplevel()
			window.geometry("200x200")
			window.configure(bg=bg_color)
			window.title("QR")  
			window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='qr.png'))
			bg = ImageTk.PhotoImage(file="qr.png")
			label = Label(window,background=bg_color,highlightbackground=bg_color)
			label.pack(fill="both", expand=True,anchor='center')
			counter_loop=[0]
			def resize_image(win):
				if counter_loop[0]%3==0:
					image = Image.open("qr.png")
					size=min(win.width,win.height)
					resized = image.resize((size, size))
					image2 = ImageTk.PhotoImage(resized)
					window.image2=image2
					label.configure(image=image2)
				counter_loop.insert(0,counter_loop[0]+1)
			window.bind("<Configure>", resize_image)
			window.mainloop()
		else:
			window = Toplevel()
			window.configure(bg=bg_color)
			window.title("Warning!")
			window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='./ui/warn.png'))
			label = Label(window,background=bg_color,highlightbackground=bg_color,text="Too much data to make QR!",foreground=fg_color,font=("Monospace",16))
			label.pack(fill="both", expand=True,anchor='center')
			window.attributes('-topmost', True)
			window.update()
			window.mainloop()
	CopyPassB=CTkButton(window,command=CopyPass,text="📋",width=10)
	QRShare=CTkButton(window,command=genadiy,text="QR!")
	CopyLoginB.grid(row=1, column=2,padx=12,pady=10)
	CopyPassB.grid(row=2, column=2,padx=12,pady=10)
	QRShare.grid(row=3, column=0,padx=12,pady=10)
scrollFrame = CTkScrollableFrame(master=tab_read)
scrollFrame.pack(fill="both",expand=True,padx=20, pady=20)
def readl():
	try:
		buttonEdit.grid_forget()
		Infos_label.grid_forget()
		title.grid_forget()
	except:
		for i in range(2):
			Title=CTkLabel(scrollFrame,text=Names[i])
			Title.grid(row=0, column=i,padx=12,pady=10)
		inform=read_info_file(get_password())
		for i in range(len(inform)):
			buttonEdit=CTkButton(scrollFrame,text="≡",command=lambda x=i: func(x),width=12)
			buttonEdit.grid(row=i+1, column=2,padx=12,pady=10)

			for j in range(2):
				Infos_label= CTkLabel(scrollFrame,text=inform[i][j])
				Infos_label.grid(row=i+1, column=j,padx=12,pady=10)
	
	   
def banan():
	tabview.pack(fill="both", expand=True,anchor='center')
	readl()


def write ():
	write_to_file(Web_entry.get(),log_entry.get(),pas_entry.get(),get_password())
	readl()


Site_label=CTkLabel(tab_write,text=Names[0])
Login_label=CTkLabel(tab_write,text=Names[1])
Password_label=CTkLabel(tab_write,text=Names[2])
Web_entry=CTkEntry(tab_write)
log_entry=CTkEntry(tab_write)
pas_entry=CTkEntry(tab_write)
SaveBut=CTkButton(tab_write,text="Save!", command=write)
Web_entry.grid(row=0, column=1,padx=12,pady=10)
log_entry.grid(row=1, column=1,padx=12,pady=10)
pas_entry.grid(row=2, column=1,padx=12,pady=10)
Site_label.grid(row=0, column=0,padx=12,pady=10)
Login_label.grid(row=1, column=0,padx=12,pady=10)
Password_label.grid(row=2, column=0,padx=12,pady=10)
SaveBut.grid(row=3, column=1,padx=12,pady=10)
def importFF():
	paths=importEntry.get()
	importcsv(paths,get_password())
	readl()
	importLabel.pack_forget()
	importBD.pack_forget()
	importEntry.pack_forget()
	tabview.pack(fill="both", expand=True,anchor='center')
	importB.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
	ExportB.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
	importEntry.delete(0, 'end')
	
importLabel=CTkLabel(window,text="Path:")
importEntry=CTkEntry(window)
def importDialog():
	tabview.pack_forget()
	importB.pack_forget()
	ExportB.pack_forget()
	importLabel.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
	importEntry.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
	importBD.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
def Export():
	exportFF(get_password())
ExportB=CTkButton(tab_read,command=Export,text="Export!")
importB=CTkButton(tab_read,command=importDialog,text="Import!")

importBD=CTkButton(window,command=importFF,text="Import!")
importB.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
ExportB.pack(fill="x", expand=True,padx=5,pady=5, side="top",anchor="n")
window.mainloop()
