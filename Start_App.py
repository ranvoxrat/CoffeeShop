from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import sys
import os

root = Tk()
root.resizable(0, 0)

# Load and resize the background image
original_image = Image.open('images\\home_bg.jpg')  # Update this line
new_size = (730, 730)
resized_image = original_image.resize(new_size, Image.BILINEAR)
photo_image = ImageTk.PhotoImage(resized_image)

# Create a label for the background image and place it to cover the entire window
background_label = Label(root, image=photo_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set window size and position
height = 730
width = 730
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
# root.wm_attributes('-alpha', 0.9)
root.wm_attributes('-topmost', True)

welcome_label = Label(text='WELCOME TO FELICIANO COFFEE SHOP', bg='#000000', font=("poppins", 20, "bold"), fg='white')
welcome_label.place(x=80, y=505)

progress_label = Label(root, text="Please Wait...", font=('poppins', 13, 'normal'), fg='white',bg='#000000')
progress_label.place(x=560, y=670)
progress = Progressbar(root, orient=HORIZONTAL, length=width, mode='determinate')  # Set length to width of the window
progress.place(x=0, y=height - 20)  # Align with the bottom of the window

exit_btn = Button(text='x', bg='#000000', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"),
                  activebackground='#000000', fg='white')
exit_btn.place(x=700, y=0)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python AccountSystem.py")
    root.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10 * i) + '%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10 * i
        i += 1
    elif i == 11:
        progress['value'] = 100  # Set the progress bar to 100% when done
        top()
        i += 1  # Increment i to avoid calling 'top' multiple times


load()

root.mainloop()
