from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, GappedSquareModuleDrawer, VerticalBarsDrawer

from qr import generate_qr


class MainWindow(Tk):
    logo_img = None
    module_driver = SquareModuleDrawer()
    def __init__(self):
        Tk.__init__(self)

        self.win_bg = '#212121'
        self.canvas_bg = '#121212'
        self.element_bg = '#3f3f3f'
        self.font_color = '#FFFFFF'
        self.font_font10 = ("Cascadia Code", 10)
        self.font_font12 = ("Cascadia Code", 12)
        self.font_font8 = ("Cascadia Code", 8)

        self.title('QR Генератор')
        self.geometry('650x350')
        self['bg'] = self.win_bg

        self.qr_panel = Canvas(bg=self.canvas_bg, borderwidth=0, bd=0, width=500, height=500,
                               highlightthickness=2, highlightbackground=self.element_bg)
        self.qr_panel.place(x=510, y=60)

        self.save_button = Button(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font12,
                                  text='Сохранить...', command=self.save_button_click)
        self.save_button.place(x=900, y=620)

        self.date_text_label = Label(bg=self.win_bg, text="Текст или ссылка", fg=self.font_color, font=self.font_font12)
        self.date_text_label.place(x=1160, y=10)

        self.text_box = Text(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font8, width=55, height=5)
        self.text_box.bind("<KeyRelease>", self.on_modified_text)
        self.text_box.place(x=1160, y=40)

        self.date_img_label = Label(bg=self.win_bg, text="Загрузите логотип или выберите из доступных",
                                    fg=self.font_color, font=self.font_font10)
        self.date_img_label.place(x=1160, y=140)

        self.img_panel = Canvas(bg=self.element_bg, width=330, height=70,
                                highlightthickness=0, highlightbackground=self.font_color)
        self.img_panel.place(x=1160, y=170)

        self.VK_button = Button(bd=2, width=5, height=2, command=lambda: self.change_logo('images/VK.png'))
        self.VK_button.place(x=1160, y=255)

        self.ZOOM_button = Button(bd=2, width=5, height=2)
        self.ZOOM_button.place(x=1215, y=255)

        self.DISCORD_button = Button(bd=2, width=37, height=37, image=PhotoImage(file='images/DISCORD.png'))
        self.DISCORD_button.place(x=1270, y=255)

        self.YOUTUBE_button = Button(bd=2, width=5, height=2)
        self.YOUTUBE_button.place(x=1325, y=255)

        self.TELEGRAMM_button = Button(bd=2, width=37, height=37, image=PhotoImage(file='images/TELEGRAMM.png'))
        self.TELEGRAMM_button.place(x=1380, y=255)

        self.SECHENOV_button = Button(bd=2, width=37, height=37, image=PhotoImage(file='images/SECHENOV.png'))
        self.SECHENOV_button.place(x=1435, y=255)

        self.load_image_button = Button(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font12,
                                        text='Загрузить...', command=self.load_image_button_click)
        self.load_image_button.place(x=1420, y=310)

        self.settings_label = Label(bg=self.win_bg, text="Расширенные настроки", fg=self.font_color,
                                    font=("Cascadia Code", 15))
        self.settings_label.place(x=10, y=10)

        self.design_label = Label(bg=self.element_bg, text="Дизайн", fg=self.font_color, font=self.font_font12,
                                  width=41)
        self.design_label.place(x=10, y=50)

        self.pattern_label = Label(bg=self.win_bg, text="● Шаблон QR-кода", fg=self.font_color, font=self.font_font10)
        self.pattern_label.place(x=20, y=80)

        self.HorizontalBarsDrawer_button = Button(bd=2, width=37, height=37,
                                                  image=PhotoImage(file='images/Horizontal.png'))
        self.HorizontalBarsDrawer_button.place(x=15, y=115)

        vertical_bars_image = ImageTk.PhotoImage(Image.open('images/Vertical.png').resize((37, 37)))

        self.VerticalBarsDrawer_button = Button(bd=2, width=37, height=37, image=vertical_bars_image,
                                                command=lambda: self.change_module_driver('VerticalBarsDrawer'))
        self.VerticalBarsDrawer_button.place(x=70, y=115)

        self.SquareModuleDrawer_button = Button(bd=2, width=37, height=37, image=PhotoImage(file='images/Square.png'))
        self.SquareModuleDrawer_button.place(x=125, y=115)

        self.RoundedModuleDrawer_button = Button(bd=2, width=37, height=37, image=PhotoImage(file='images/Rounded.png'))
        self.RoundedModuleDrawer_button.place(x=180, y=115)

        self.CircleModuleDrawer_button = Button(bd=2, width=37, height=37, image=PhotoImage(file='images/Circle.png'))
        self.CircleModuleDrawer_button.place(x=235, y=115)

        self.GappedSquareModuleDrawer_button = Button(bd=2, width=37, height=37,
                                                      image=PhotoImage(file='images/Gapped.png'),
                                                      command=lambda: self.change_module_driver('GappedSquareModuleDrawer'))
        self.GappedSquareModuleDrawer_button.place(x=290, y=115)

        self.color_label = Label(bg=self.win_bg, text="● Цвет", fg=self.font_color, font=self.font_font10)
        self.color_label.place(x=20, y=160)

        self.mainloop()

    def change_logo(self, logo_path):
        self.logo_img = logo_path
        self.update_qr()

    def change_module_driver(self, driver_name):
        if driver_name == 'GappedSquareModuleDrawer':
            self.module_driver = GappedSquareModuleDrawer()
        if driver_name == 'VerticalBarsDrawer':
            self.module_driver = VerticalBarsDrawer()
        self.update_qr()

    def update_qr(self):
        img = generate_qr(self.text_box.get("1.0", END), module_driver=self.module_driver,
                          fill_color_param='black', back_color_param='white', image=self.logo_img)
        img = img.resize((500, 500))
        img = ImageTk.PhotoImage(img)
        self.qr_panel.create_image(0, 0, anchor=NW, image=img)

    def on_modified_text(self, event):
        self.update_qr()

    def save_button_click(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.png')
        generate_qr(self.text_box.get("1.0", END)).save(file_name)

    def load_image_button_click(self):
        file_name = filedialog.askopenfilename(filetypes=[("Файлы изображений", '.png .jpg .jpeg')])
        self.logo_img = file_name
        self.update_qr()