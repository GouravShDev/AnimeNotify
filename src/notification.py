from tkinter import Tk, Label, Canvas, Frame, PhotoImage
# show notification

def genNotification(title, descr, icon, bg):
    notice = Tk()
    notice.title("Notification")
    notice.configure(background='black')
    notice.overrideredirect(True)
    resolution=str(int(notice.winfo_screenwidth()*0.25))+"x"+str(int(notice.winfo_screenheight()*0.20))+"+"+str(int(notice.winfo_screenwidth()*0.74))+"+"+str(int(notice.winfo_screenheight()*0.75))
    notice.geometry(resolution)
    bg_image=PhotoImage(file = bg)
    background_label = Label(notice, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1)
    background_label.pack()
    l=Label(notice, text="hello")
    l.pack()
    notice.mainloop()
genNotification("Anime", "descr..", "link", "icon.png")