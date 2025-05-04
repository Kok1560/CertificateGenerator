from tkinter import ttk, LabelFrame
from CTkMessagebox import CTkMessagebox
from PIL import Image
from customtkinter import *
from pandas import read_excel
import pages.design
import pages.parent
import os
import sys


# -------------------------------------------- Create Party Page --------------------------------------------------
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class DataPage:
    def __init__(self, root):
        self.data_page = root
        self.data_page.geometry('1130x510+300+200')
        self.data_page.resizable(False, False)
        self.data_page.title("Certificate Generator")
        self.data_page.wm_iconbitmap(r"images\logo.ico")
        self.frame2 = CTkFrame(master=self.data_page, fg_color="White")
        self.frame2.pack(fill="both", expand=True)

        # ----------------------------------- Variables of Create Party Page -------------------------------------------

        self.file_path = StringVar()
        self.column_name = StringVar()
        self.dn_check = StringVar()
        self.fn_check = StringVar()
        self.mn_check = StringVar()
        self.ln_check = StringVar()
        self.final_names = []
        # -------------------------------------------- Frames and Buttons of Create Party Page --------------------------------------------------

        self.page_title = CTkLabel(self.frame2, text="IMPORT DATA", fg_color='#0f4d7d',
                                   font=('tajawal', 20, 'bold'), text_color='white', width=1120, height=35)
        self.page_title.place(x=5, y=10)

        self.data_detail_f = LabelFrame(self.frame2, text='Data Details', width=1385, height=230,
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
        self.file_path_ent.bind("<Return>", self.go_to_column_field)
        self.file_path_ent.focus_set()

        self.column_lbl = CTkLabel(self.data_detail_f, text="Column Name:", fg_color="white",
                                   text_color="black",
                                   font=("tajawal", 20, "bold"))
        self.column_lbl.place(x=600, y=3)

        self.column_ent = CTkEntry(self.data_detail_f, corner_radius=0, font=('tajawal', 15), width=130,
                                   height=27,
                                   fg_color='#FFFDD0',
                                   justify=CENTER, textvariable=self.column_name, text_color="black")
        self.column_ent.place(x=735, y=5)
        self.column_ent.bind("<Return>", self.show_data)

        self.dn_checkbox = CTkCheckBox(self.data_detail_f, text="Drop Nulls", fg_color="white", text_color="black",
                                       font=("tajawal", 18, "bold"), variable=self.dn_check, onvalue="on",
                                       offvalue="off")
        self.dn_checkbox.place(x=930, y=5)

        self.fn_checkbox = CTkCheckBox(self.data_detail_f, text="First Name", fg_color="white", text_color="black",
                                       font=("tajawal", 18, "bold"), variable=self.fn_check, onvalue="on",
                                       offvalue="off")
        self.fn_checkbox.place(x=330, y=60)

        self.mn_checkbox = CTkCheckBox(self.data_detail_f, text="Middle Name", fg_color="white", text_color="black",
                                       font=("tajawal", 18, "bold"), variable=self.mn_check, onvalue="on",
                                       offvalue="off")
        self.mn_checkbox.place(x=530, y=60)

        self.ln_checkbox = CTkCheckBox(self.data_detail_f, text="Last Name", fg_color="white", text_color="black",
                                       font=("tajawal", 18, "bold"), variable=self.ln_check, onvalue="on",
                                       offvalue="off")
        self.ln_checkbox.place(x=730, y=60)
        self.save_button = CTkButton(self.data_detail_f, corner_radius=0, font=('tajawal', 15), fg_color='green',
                                     text='Save',
                                     text_color='black', border_width=1, border_color='black', width=180,
                                     command=self.design_page)
        self.save_button.place(x=390, y=120)

        self.clear_button = CTkButton(self.data_detail_f, corner_radius=0, font=('tajawal', 15), fg_color='blue',
                                      text='Clear',
                                      text_color='black', border_width=1, border_color='black', width=180,
                                      command=self.clear)
        self.clear_button.place(x=590, y=120)

        self.certi_photo = CTkImage(light_image=Image.open(resource_path("images/certificate_image.png")),
                                    size=(600, 240))
        self.certi_bg_photo = CTkLabel(self.frame2, image=self.certi_photo, text='')
        self.certi_bg_photo.place(x=12, y=260)

        self.data_table_f = CTkFrame(self.frame2, width=500, height=250, corner_radius=0)
        self.data_table_f.place(x=620, y=250)

        self.style = ttk.Style()
        self.style.configure('Treeview', font=('tajawal', 15), rowheight=30, background='#D3D3D3', foreground='black',
                             fieldbackground='#white')
        self.style.configure('Treeview.Heading', font=('tajawal', 15))

        self.data_table = ttk.Treeview(self.data_table_f)
        self.data_table.place(x=21, y=0, width=603, height=313)

        self.scroll_y = ttk.Scrollbar(self.data_table_f, orient=VERTICAL, command=self.data_table.yview)
        self.scroll_y.place(x=0, y=0, height=313)
        self.data_table.configure(yscrollcommand=self.scroll_y.set)

        self.data_table['columns'] = ("id", "column_name")

        self.data_table.column("#0", width=0, stretch=NO)
        self.data_table.column("#1", width=100, anchor=CENTER)
        self.data_table.column("#2", width=100, anchor=CENTER)

        self.data_table.heading("#0", text='')

        self.data_table.tag_configure('oddrow', background='white')
        self.data_table.tag_configure('evenrow', background='lightblue')

        self.data_page.bind("<F1>", self.home_page)

    # ----------------------------------- Functions of Create Party Page -------------------------------------------
    def go_to_column_field(self, e):
        self.column_ent.focus_set()

    def show_data(self, e=None):
        try:
            count = 0
            names = []
            self.final_names = []
            data = read_excel(self.file_path.get())
            if self.file_path.get() == '' or ' ' in self.file_path.get() or self.column_ent.get() == '':
                CTkMessagebox(title='Error', message='Please fill all blanks with right values without spaces',
                              icon='cancel', sound=True,
                              font=('tajawal', 15, 'bold'))
                self.clear()
            elif self.dn_check.get() == 'on':
                data.dropna(subset=[self.column_ent.get()], inplace=True)
                names = [names for names in data[self.column_name.get()]]
            else:
                names = [names for names in data[self.column_name.get()]]

            name_num = 0
            if self.ln_check.get() == 'on':
                name_num = 3
            elif self.mn_check.get() == 'on':
                name_num = 2
            elif self.fn_check.get() == 'on':
                name_num = 1

            if name_num == 0:
                for name in names:
                    self.final_names.append(name)
            else:
                for name in names:
                    if len(name.split()) > name_num:
                        name = name.split()[0:name_num]
                        self.final_names.append(" ".join(name))
                    else:
                        self.final_names.append(name)

            data = self.final_names
            self.data_table.heading("#1", text="ID", anchor=CENTER)
            self.data_table.heading("#2", text=self.column_name.get(), anchor=CENTER)
            self.data_table.column("#2", width=150, anchor=CENTER)
            self.data_table.column("#1", width=50, anchor=CENTER)
            count = 0
            for item in self.data_table.get_children():
                self.data_table.delete(item)
            for eachcol in self.final_names:
                if count % 2 == 0:
                    self.data_table.insert('', 'end', values=(count + 1, eachcol), tags=('evenrow',))
                    count += 1
                else:
                    self.data_table.insert('', 'end', values=(count + 1, eachcol), tags=('oddrow',))
                    count += 1
        except FileNotFoundError:
            CTkMessagebox(title='Error', message="This Path Doesn't Found",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))
            for item in self.data_table.get_children():
                self.data_table.delete(item)
        except KeyError:
            CTkMessagebox(title='Error', message="This Coulumn Doesn't Found In DataBase",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))
            for item in self.data_table.get_children():
                self.data_table.delete(item)
        except AttributeError:
            CTkMessagebox(title='Error', message="Theres Is Nulls In DataBase Please Select Drop Nulls",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))
        except OSError:
            CTkMessagebox(title='Error', message="Please Write Path Without Double Coutations (\"\")",
                          icon='cancel', sound=True,
                          font=('tajawal', 15, 'bold'))

    def clear(self):
        self.file_path.set('')
        self.column_name.set('')
        self.dn_check.set('off')
        self.fn_check.set('off')
        self.mn_check.set('off')
        self.ln_check.set('off')
        for item in self.data_table.get_children():
            self.data_table.delete(item)

    def home_page(self, e):
        self.frame2.destroy()
        pages.parent.Homepage(self.data_page)

    def design_page(self):
        self.frame2.destroy()
        pages.design.DesignPage(self.data_page, self.final_names)
