from customtkinter import *
from CTkMessagebox import CTkMessagebox
from tkinter import LabelFrame, PhotoImage
from PIL import Image, ImageDraw, ImageFont
# import os
# import sys

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS2
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)
# -------------------------------------------- Create Party Page --------------------------------------------------
class DesignPage:
    def __init__(self, root, data):
        self.design_page = root
        self.design_page.geometry('1130x510+300+200')
        self.design_page.resizable(False, False)
        self.design_page.title("Certificate Generator")
        self.design_page.wm_iconbitmap(r"images\logo.ico")
        self.frame3 = CTkFrame(master=self.design_page, fg_color="White")
        self.frame3.pack(fill="both", expand=True)
        # ----------------------------------- Variables of Create Party Page -------------------------------------------
        self.data = data
        self.file_path = StringVar()
        self.color = StringVar()
        self.font = StringVar()
        self.size = StringVar()
        self.x = StringVar()
        self.y = StringVar()
        self.save_path = StringVar()
        # -------------------------------------------- Frames and Buttons of Create Party Page --------------------------------------------------

        self.page_title = CTkLabel(self.frame3, text="DESIGN CERTIFICATE", fg_color='#0f4d7d',
                                   font=('tajawal', 20, 'bold'), text_color='white', width=1120, height=35)
        self.page_title.place(x=5, y=10)

        self.data_detail_f = LabelFrame(self.frame3, text='Data Details', width=1385, height=230,
                                        borderwidth=2,
                                        relief=RIDGE, labelanchor='n', font=('tajawal', 15, 'bold'), bg='white')
        self.data_detail_f.place(x=15, y=80)

        self.file_path_lbl = CTkLabel(self.data_detail_f, text="File Path:", fg_color="white", text_color="black",
                                      font=("tajawal", 20, "bold"))
        self.file_path_lbl.place(x=15, y=3)

        self.file_path_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=450,
                                      height=27,
                                      fg_color='#FFFDD0',
                                      justify=CENTER, textvariable=self.file_path, text_color="black")
        self.file_path_ent.place(x=100, y=5)
        self.file_path_ent.bind("<Return>", self.go_to_color_field)
        self.file_path_ent.focus_set()

        self.color_lbl = CTkLabel(self.data_detail_f, text="Color:", fg_color="white",
                                  text_color="black",
                                  font=("tajawal", 20, "bold"))
        self.color_lbl.place(x=600, y=3)

        self.color_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=130,
                                  height=27,
                                  fg_color='#FFFDD0',
                                  justify=CENTER, textvariable=self.color, text_color="black")
        self.color_ent.place(x=660, y=5)
        self.color_ent.bind("<Return>", self.go_to_font_field)

        self.font_lbl = CTkLabel(self.data_detail_f, text="Font:", fg_color="white",
                                 text_color="black",
                                 font=("tajawal", 20, "bold"))
        self.font_lbl.place(x=830, y=3)

        self.font_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=130,
                                 height=27,
                                 fg_color='#FFFDD0',
                                 justify=CENTER, textvariable=self.font, text_color="black")
        self.font_ent.place(x=880, y=5)
        self.font_ent.bind("<Return>", self.go_to_size_field)

        self.size_lbl = CTkLabel(self.data_detail_f, text="Size:", fg_color="white",
                                 text_color="black",
                                 font=("tajawal", 20, "bold"))
        self.size_lbl.place(x=15, y=60)

        self.size_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=130,
                                 height=27,
                                 fg_color='#FFFDD0',
                                 justify=CENTER, textvariable=self.size, text_color="black")
        self.size_ent.place(x=60, y=60)
        self.size_ent.bind("<Return>", self.go_to_x_field)

        self.x_lbl = CTkLabel(self.data_detail_f, text="X-Place:", fg_color="white",
                              text_color="black",
                              font=("tajawal", 20, "bold"))
        self.x_lbl.place(x=250, y=60)

        self.x_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=130,
                              height=27,
                              fg_color='#FFFDD0',
                              justify=CENTER, textvariable=self.x, text_color="black")
        self.x_ent.place(x=330, y=60)
        self.x_ent.bind("<Return>", self.go_to_y_field)

        self.y_lbl = CTkLabel(self.data_detail_f, text="Y-Place:", fg_color="white",
                              text_color="black",
                              font=("tajawal", 20, "bold"))
        self.y_lbl.place(x=500, y=60)

        self.y_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=130,
                              height=27,
                              fg_color='#FFFDD0',
                              justify=CENTER, textvariable=self.y, text_color="black")
        self.y_ent.place(x=580, y=60)
        self.y_ent.bind("<Return>", self.go_to_save_path_field)

        self.save_path_lbl = CTkLabel(self.data_detail_f, text="Save Path:", fg_color="white",
                                      text_color="black",
                                      font=("tajawal", 20, "bold"))
        self.save_path_lbl.place(x=750, y=60)

        self.save_path_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=250,
                                      height=27,
                                      fg_color='#FFFDD0',
                                      justify=CENTER, textvariable=self.save_path, text_color="black")
        self.save_path_ent.place(x=850, y=60)
        self.save_path_ent.bind("<Return>", self.test_btn)

        self.generate_button = CTkButton(self.data_detail_f, corner_radius=0, font=('tajawal', 15), fg_color='green',
                                         text='Generate',
                                         text_color='black', border_width=1, border_color='black',
                                         width=180, command=self.generate_btn)
        self.generate_button.place(x=390, y=120)

        self.test_button = CTkButton(self.data_detail_f, corner_radius=0, font=('tajawal', 15), fg_color='blue',
                                     text='Test',
                                     text_color='black', border_width=1, border_color='black', width=180,
                                     command=self.test_btn)
        self.test_button.place(x=590, y=120)

    # ----------------------------------- Functions of Create Party Page -------------------------------------------
    def go_to_color_field(self, e):
        self.color_ent.focus_set()

    def go_to_font_field(self, e):
        self.font_ent.focus_set()

    def go_to_size_field(self, e):
        self.size_ent.focus_set()

    def go_to_x_field(self, e):
        self.x_ent.focus_set()

    def go_to_y_field(self, e):
        self.y_ent.focus_set()

    def go_to_save_path_field(self, e):
        self.save_path_ent.focus_set()

    def test_btn(self, e=None):
        try:
            if self.file_path.get() == '' or ' ' in self.file_path.get() or self.color.get() == '' or self.font.get() == '' or self.size_ent.get() == '' or self.x_ent.get() == '' or self.y_ent.get() == '' or self.save_path.get() == '':
                CTkMessagebox(title='Error', message='Please fill all blanks with right values without spaces',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
            elif self.x.get().isnumeric() is False or self.y.get().isnumeric() is False or self.size.get().isnumeric() is False:
                CTkMessagebox(title='Error', message='Please Fill all X, Y Fields With Numbers Not Text',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
            elif self.color.get().split(',')[0].isnumeric() is False or self.color.get().split(',')[
                1].isnumeric() is False or self.color.get().split(',')[2].isnumeric() is False:
                CTkMessagebox(title='Error', message='Please Fill Color Field With R,G,B',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
            else:
                im = Image.open(self.file_path.get())
                d = ImageDraw.Draw(im)
                location = (float(self.x.get()), float(self.y.get()))
                color = self.color.get().split(",")
                text_color = (int(color[0]), int(color[1]), int(color[2]))
                font = ImageFont.truetype(self.font.get(), float(self.size.get()))
                d.text(location, "Name Of The Person", fill=text_color, font=font)
                im.save(self.save_path.get() + r"\certificate_test.png")

                test_photo = CTkImage(light_image=Image.open(self.save_path.get() + r"\certificate_test.png"),
                                      size=(500, 250))
                test_bg_photo = CTkLabel(self.frame3, image=test_photo, text='')
                test_bg_photo.place(x=350, y=250)
        except FileNotFoundError:
            CTkMessagebox(title='Error', message="This Path Doesn't Found",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))
        except OSError:
            CTkMessagebox(title='Error', message="This Font Doesn't Found\nor You Enter Path Wrong\nPlease Write Path Without Double Coutations\n(\"\")",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))
        except IndexError:
            CTkMessagebox(title='Error', message='Please Fill Color Field With R,G,B',
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))

    def generate_btn(self, e=None):
        try:
            os.remove(self.save_path.get() + r"\certificate_test.png")
            if self.file_path.get() == '' or ' ' in self.file_path.get() or self.color.get() == '' or self.font.get() == '' or self.size_ent.get() == '' or self.x_ent.get() == '' or self.y_ent.get() == '' or self.save_path.get() == '':
                CTkMessagebox(title='Error', message='Please fill all blanks with right values without spaces',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
            elif self.x.get().isnumeric() is False or self.y.get().isnumeric() is False or self.size.get().isnumeric() is False:
                CTkMessagebox(title='Error', message='Please Fill all X, Y Fields With Numbers Not Text',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
            elif self.color.get().split(',')[0].isnumeric() is False or self.color.get().split(',')[
                1].isnumeric() is False or self.color.get().split(',')[2].isnumeric() is False:
                CTkMessagebox(title='Error', message='Please Fill Color Field With (R,G,B)',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
            else:
                count = 0
                for i in self.data:
                    count += 1
                    im = Image.open(self.file_path.get())
                    d = ImageDraw.Draw(im)
                    location = (float(self.x.get()), float(self.y.get()))
                    color = self.color.get().split(",")
                    text_color = (int(color[0]), int(color[1]), int(color[2]))
                    font = ImageFont.truetype(self.font.get(), float(self.size.get()))
                    d.text(location, i, fill=text_color, font=font)
                    im.save(self.save_path.get() + r"\certificate_" + i + str(count) + ".pdf")
                CTkMessagebox(message="Certificates Is Successfully Generated.",
                              icon="check", option_1="Thanks")
        except FileNotFoundError:
            CTkMessagebox(title='Error', message="This Path Doesn't Found",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))
        except OSError:
            CTkMessagebox(title='Error', message="This Font Doesn't Found",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))

    def clear(self):
        self.file_path.set('')
        self.color.set('')
        self.font.set('')
        self.size.set('')
        self.x.set('')
        self.y.set('')
        self.save_path.set('')
