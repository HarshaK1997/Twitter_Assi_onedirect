#GUI Design Module
#=================

# Please don't comment the below command even-though you are not using it here, it tells that Database should run first
import Database
import FetchData
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

path = 'Twitter.jpeg'

#Simple Output design
root = tk.Tk()
root.title("Your Twitter Links")
root['bg'] = 'black'

w, h, d = root.winfo_screenwidth(), root.winfo_screenheight(), root.winfo_screendepth()
root.geometry("%dx%d+%d+0" % (w, h, d))

#inserting image at top
img = ImageTk.PhotoImage(Image.open('TwitterPhoto.jpg'))
panel = tk.Label(root, image=img)
panel.pack(side="top", expand="no")

#inserting image at left
img1 = ImageTk.PhotoImage(Image.open(path))
panel1 = tk.Label(root, image=img1)
panel1.pack(side="left", expand="no")

#inserting image at right
img2 = ImageTk.PhotoImage(Image.open(path))
panel2 = tk.Label(root, image=img2)
panel2.pack(side="right", expand="no")

#inserting URL
for i in range(0, len(FetchData.URL)):
    lbl = tk.Label(root, text=FetchData.URL[i], fg="blue", cursor="hand2")
    lbl.config(text=FetchData.URL[i])
    lbl.pack()
    lbl.bind("<Button-1>", callback)

root.mainloop()