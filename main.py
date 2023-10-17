from subprocess import getoutput
from threading import Thread
from tkinter import Label, PhotoImage, RIDGE, Tk, Scrollbar, Frame
from tkinter.messagebox import showerror
from ctypes import windll

my_appid = 'logic_realm.hified.1.0'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_appid)

def dsps():
	root.spl.destroy()
	root.st.destroy()
	root.st2.destroy()
	main()

def splash_screen():
	image = PhotoImage(file="icon-png.png")
	image = image.zoom(5)
	image = image.subsample(32)
	root.spl = Label(root, image=image, border=0)
	root.spl.pack(pady=20)
	root.spl.image = image
	root.st = Label(root, text="HiFied", font="Helvetica 25 bold", border=0, bg="black", fg="white")
	root.st.pack(pady=0)
	root.st2 = Label(root, text="\n\nBy Logic Realm", font="Helvetica 12 italic", border=0, bg="black", fg="white")
	root.st2.pack(pady=0)
	root.after(3000, dsps)

def dump() -> list[str] and list[str]:
    profiles = getoutput("netsh wlan show profiles").split("   All User Profile     : ")
    profiles.remove(profiles[0])
    pas = []

    for i in range(len(profiles)):
        profiles[i] = profiles[i].replace("\n", "").removesuffix(" ")
        pasl = getoutput(f'netsh wlan show profile "{profiles[i]}" key=clear').split("    Key Content            : ")
        pasl.remove(pasl[0])
        try:
            pas.append(pasl[0].split('\n')[0])
        except:
            pas.append("Not Found")
    
    for i in range(len(profiles)):
        Label(root.frame, text=profiles[i], font="Georgia 14", relief=RIDGE, borderwidth=2, fg="green", width=40, bg="black").grid(row=i+1, column=0, ipadx=40, ipady=10)
        Label(root.frame, text=pas[i], font="Georgia 14", relief=RIDGE, borderwidth=2, fg="green", width=50, bg="black").grid(row=i+1, column=1, ipadx=70, ipady=10)

# def perm():
#     root.perm = Label(root, text="\n\nWanna Dump All Wifi Passwords, Which Are\n\nPreviously Connected ??", font="Helvetica 16 bold italic", border=0, bg="black", fg="white")
#     root.perm.pack(pady=0)

#     root.NB = Button(root, text="No", command=quit, width=10, bg="red", fg="#fff", pady=10, padx=15, font="Georgia, 13")
#     root.NB.place(x=30, y=200)

#     root.YB = Button(root, text="Yes", width=10, bg="green", fg="#fff", pady=10, padx=15, font="Georgia, 13", command=main)
#     root.YB.place(x=430, y=200)

def main():
    # root.perm.destroy()
    # root.NB.destroy()
    # root.YB.destroy()
    root.state("zoomed")
    root.mainFrame = Frame(root, bg="black")
    root.mainFrame.pack(side='left', fill='both', expand=True)
    root.scroll = Scrollbar(root)
    root.scroll.pack(side='right')
    root.Heading_Lebel = Label(root.mainFrame, font="Helvetica 16 bold italic underline", text="A l l     W i f i     P a s s w o r d s", border=0, bg="black", fg="blue")
    root.Heading_Lebel.pack(pady=20)
    root.frame = Frame(root.mainFrame, bg="black", borderwidth=2)
    root.frame.pack(pady=20, padx=20)
    ssidLabel = Label(root.frame, text="S S I D", font="Georgia 14 bold", relief=RIDGE, borderwidth=2, width=40, fg="red", bg="black")
    ssidLabel.grid(row=0, column=0, ipady=10)
    pasLabel = Label(root.frame, text="P a s s w o r d", font="Georgia 14 bold", relief=RIDGE, borderwidth=2, width=50, fg="red", bg="black")
    pasLabel.grid(row=0, column=1, ipadx=20, ipady=10)
    try:
        t = Thread(target=dump)
        t.start()
    except:
        showerror("Error Message", "Error While Dumping Data...")

root = Tk()
root.geometry("600x300")
root.resizable(False, False)
root.title("HiFied")
root.config(background="#000")
root.iconbitmap("icon.ico")

splash_screen()

root.mainloop()