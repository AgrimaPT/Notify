from tkinter import *
from PIL import Image, ImageTk
from plyer import notification
from tkinter import messagebox
import time
import os

t=Tk()
t.title("notifyapp")
t.geometry("500x300")

img=Image.open(r"C:\Users\HP\Desktop\mini projects\notifyapp\images.png")
new_size = (50, 50)

# Resize the image
img_resized = img.resize(new_size, Image.LANCZOS)

# Save the resized image with adjusted quality
img_resized.save(r"C:\Users\HP\Desktop\mini projects\notifyapp\resized_image.png", quality=85)
tkimage=ImageTk.PhotoImage(img_resized)
img_label=Label(t,image=tkimage)
img_label.place(x=0,y=0)
t_label=Label(t,text="NOTIFY APP",font=("poppins",30,'bold'),fg="#528DFF")
t_label.place(x=123,y=0)

def details():
    tit=ttl.get()
    mssg=msg.get()
    tm=timee.get()

    if tit=="" or mssg=="" or tm=="":
        messagebox.showerror("Alert","Fill all the fields")
    else:
        int_time=int(float(tm))
        mintosec=int_time*60
        messagebox.showinfo("notifier set","set notification")
        t.destroy()
        time.sleep(mintosec)
        notification.notify(title='tit', message='mssg', app_name='Notify', app_icon='', timeout=10, ticker='')

t_label=Label(t,text="Title",font=("poppins",10))
t_label.place(x=12,y=70)

ttl=Entry(t,width="25",font=('poppins',13))
ttl.place(x=123,y=70)

msg_label=Label(t,text="Message",font=("poppins",10))
msg_label.place(x=12,y=120)

msg=Entry(t,width="40",font=('poppins',13))
msg.place(x=123,y=120,height=30)

time_label=Label(t,text="set time",font=("poppins",10))
time_label.place(x=12,y=175)

timee=Entry(t,width="5",font=('poppins',13))
timee.place(x=123,y=175)

t_min_label=Label(t,text="minutes",font=("poppins",10))
t_min_label.place(x=175,y=180)

btn=Button(t, text="Set Notification", font=('poppins',10,'bold'),fg="#ffffff",bg="#528DFF",width=20,
           command=details)
btn.place(x=170,y=230)

t.resizable(0,0)
t.mainloop()
