from customtkinter import *
from PIL import Image
from datetime import date
from time import strftime
from pages.data import *
import pages.design


# ------------------------------------------------ inventory Page -----------------------------------------------

class Homepage:
    def __init__(self, root):
        self.parent_win = root
        self.parent_win.geometry('1350x700+100+100')
        self.parent_win.resizable(False, False)
        self.parent_win.title("Certificate Generator")
        self.parent_win.unbind("<F1>")
        self.frame1 = CTkFrame(master=root, fg_color="White")
        self.frame1.pack(fill="both", expand=True)

        self.page_title = CTkLabel(self.frame1, text="Certificate Generator", font=('tajawal', 40, 'bold'),
                                   fg_color="#010c48",
                                   text_color='white')
        self.page_title.pack(fill=X)

        # ------------------------------------------ Frames and Buttons of inventory Page --------------------------------------------------
        self.clock_lbl = CTkLabel(self.frame1,
                                  font=('tajawal', 20), fg_color="#4d636d", text_color='white')
        self.clock_lbl.pack(fill=X)
        self.update_clock()

        self.f1 = CTkFrame(self.frame1, height=390, width=200, border_width=2, corner_radius=0, fg_color='white')
        self.f1.place(x=1, y=87)

        self.menu_img = CTkImage(light_image=Image.open('images/logo.png'), size=(195, 195))
        self.menu_img_lab = CTkLabel(self.f1, image=self.menu_img, text='')
        self.menu_img_lab.place(x=2, y=2)

        self.menu_lab = CTkLabel(self.f1, text="Menu", text_color="white", fg_color="#009688",
                                 font=('tajawal', 20, 'bold'),
                                 width=196,
                                 height=40)
        self.menu_lab.place(x=2, y=200)

        self.row_img = CTkImage(light_image=Image.open("images/rows.png"), size=(20, 20))

        self.data_btn = CTkButton(self.f1, text="Data", font=('tajawal', 20, 'bold'),
                                  width=196, height=50, corner_radius=0, border_width=3, cursor="hand2",
                                  fg_color='white', text_color='black', border_color='black',
                                  image=self.row_img,
                                  compound=LEFT, anchor='w', command=self.data_p)
        self.data_btn.place(x=2, y=240)

        self.template_btn = CTkButton(self.f1, text="Template", font=('tajawal', 20, 'bold'),
                                      width=196, height=50, corner_radius=0, border_width=3, cursor="hand2",
                                      fg_color='white', text_color='black', border_color='black',
                                      image=self.row_img,
                                      compound=LEFT, anchor='w', command=self.design_p)
        self.template_btn.place(x=2, y=288)

        self.exit_btn = CTkButton(self.f1, text="Exit", font=('tajawal', 20, 'bold'),
                                  width=196, height=50, corner_radius=0, border_width=3, cursor="hand2",
                                  fg_color='white', text_color='black', border_color='black', image=self.row_img,
                                  compound=LEFT,
                                  anchor='w', command=self.parent_win.destroy)
        self.exit_btn.place(x=2, y=336)

        self.footer_lbl = CTkLabel(self.frame1,
                                   text=f"FOR PROBLEMS CALL +20 1211925856 \n MADE BY SKILLS AREA GROUP",
                                   font=('tajawal', 20), fg_color="#4d636d", text_color='white', height=50)
        self.footer_lbl.pack(side=BOTTOM, fill=X)

    # -------------------------------------------- Functions of inventory Page --------------------------------------------------
    def update_clock(self):
        current_time = strftime("%I:%M:%S %p")
        self.clock_lbl.configure(
            text=f"HELLO IN CERTIFICATE GENERATOR      \t\t DATE: {date.today()} \t\t\t TIME:  {current_time}")
        self.clock_lbl.after(1000, self.update_clock)

    def data_p(self):
        self.frame1.destroy()
        DataPage(self.parent_win)

    def design_p(self):
        self.frame1.destroy()
        pages.design.DesignPage(self.parent_win, [])

