from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import sys
sys.path.append('C:/CoffeeShopManagentSystem-main')
import os
import CoffeeManagementSystem.Employee
import CoffeeManagementSystem.AccountSystem


class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file='images\\CoffeeShop-brand-logo.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome')

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        # ====== MENU BAR ==========
        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        home_bgImg = Image.open('images\\home_bg.jpg')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

        admIcon = Image.open('images\\user.png')
        new_size = (40, 40)  
        resized_admIcon = admIcon.resize(new_size,resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_admIcon)
        adm = Label(homepage, image=photo, bg='#ffffff')
        adm.image = photo
        adm.place(x=1285, y=5)

        heading = Label(homepage, text='© FELICIANO C0FFEE SH0P', bg='black', fg='#ff6c38', font=("yu gothic ui", 19, "bold"))
        heading.place(x=770, y=90)

        heading1 = Label(homepage, text='Welcome Employee', bg='black', fg='#ff6c38', font=("yu gothic ui", 50, "bold"))
        heading1.place(x=775, y=120)

        heading2 = Label(homepage, text='Trending', bg='black', fg='#ff6c38', font=("", 19, "bold"))
        heading2.place(x=150, y=95)

        # Coffee Image
        coffeeImage = Image.open('images\\menu-6.png')
        photo = ImageTk.PhotoImage(coffeeImage)
        coffeeImg = Label(homepage, image=photo, bg='black')
        coffeeImg.image = photo
        coffeeImg.place(x=50, y=150)

        coffeeImage2 = Image.open('images\\menu-5.png')
        photo = ImageTk.PhotoImage(coffeeImage2)
        coffeeImg2 = Label(homepage, image=photo, bg='black')
        coffeeImg2.image = photo
        coffeeImg2.place(x=160, y=150)

        coffeeImage3 = Image.open('images\\menu-4.png')
        photo = ImageTk.PhotoImage(coffeeImage3)
        coffeeImg3 = Label(homepage, image=photo, bg='black')
        coffeeImg3.image = photo
        coffeeImg3.place(x=270, y=150)

        coffeeImage4 = Image.open('images\\menu-3.png')
        photo = ImageTk.PhotoImage(coffeeImage4)
        coffeeImg4 = Label(homepage, image=photo, bg='black')
        coffeeImg4.image = photo
        coffeeImg4.place(x=50, y=275)

        coffeeImage5 = Image.open('images\\menu-2.png')
        photo = ImageTk.PhotoImage(coffeeImage5)
        coffeeImg5 = Label(homepage, image=photo, bg='black')
        coffeeImg5.image = photo
        coffeeImg5.place(x=160, y=275)

        coffeeImage6 = Image.open('images\\menu-1.png')
        photo = ImageTk.PhotoImage(coffeeImage6)
        coffeeImg6 = Label(homepage, image=photo, bg='black')
        coffeeImg6.image = photo
        coffeeImg6.place(x=270, y=275)

        heading3 = Label(homepage, text='Cappuccino', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading3.place(x=55, y=245)

        heading4 = Label(homepage, text='Mocha', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading4.place(x=182, y=245)

        heading5 = Label(homepage, text='Piccolo Latte', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading5.place(x=282, y=245)

        heading6 = Label(homepage, text="Cafe' Latte", bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading6.place(x=56, y=370)

        heading7 = Label(homepage, text='Espresso', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading7.place(x=170, y=370)

        heading8 = Label(homepage, text='Black Coffee with milk', bg='black', fg='#ffffff', font=("", 7, "bold"))
        heading8.place(x=265, y=370)

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=10, y=15)

        def manage():
            dashboard_window.withdraw()
            os.system("python Employee.py")
            dashboard_window.destroy()

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Manage', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                               command= manage)
        manage_button.place(x=80, y=15)

        # ========== PRODUCTS BUTTON =======
        product_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=manage)
        product_button.place(x=170, y=15)

        def logout():
            win = Toplevel()
            CoffeeManagementSystem.AccountSystem.AccountPage(win)
            dashboard_window.withdraw()
            win.deiconify()
        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=logout)
        logout_button.place(x=1220, y=15)


def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
