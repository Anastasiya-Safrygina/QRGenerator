from tkinter import *
from tkinter import filedialog

from PIL import ImageTk
from qrcode.image.styles.moduledrawers import *

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

        self.dark_in_the_center = Label(bg='#141414', width=104, height=60)
        self.dark_in_the_center.place(x=400, y=0)

        self.qr_panel = Canvas(bg=self.canvas_bg, borderwidth=0, bd=0, width=500, height=500,
                               highlightthickness=2, highlightbackground=self.element_bg)
        self.qr_panel.place(x=510, y=60)

        self.save_button = Button(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font12,
                                  text='Сохранить...', command=self.save_button_click)
        self.save_button.place(x=900, y=620)

        self.data_text_label = Label(bg=self.win_bg, text="Текст или ссылка", fg=self.font_color, font=self.font_font12)
        self.data_text_label.place(x=1160, y=10)

        self.text_box = Text(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font8, width=55, height=5)
        self.text_box.bind("<KeyRelease>", self.on_modified_text)
        self.text_box.place(x=1160, y=40)

        self.data_img_label = Label(bg=self.win_bg, text="Загрузите логотип или выберите из доступных",
                                    fg=self.font_color, font=self.font_font10)
        self.data_img_label.place(x=1160, y=140)

        self.img_panel = Canvas(bg=self.element_bg, width=330, height=70,
                                highlightthickness=0, highlightbackground=self.font_color)
        self.img_panel.place(x=1160, y=170)
# Кнопки-логотипы
        vk = ImageTk.PhotoImage(Image.open('images/VK.png').resize((40, 40)))

        self.VK_button = Button(bd=2, width=40, height=40, image=vk, command=lambda: self.change_logo('images/VK.png'))
        self.VK_button.place(x=1160, y=255)

        zoom = ImageTk.PhotoImage(Image.open('images/ZOOM.png').resize((40, 40)))

        self.ZOOM_button = Button(bd=2, width=40, height=40, image=zoom,
                                  command=lambda: self.change_logo('images/ZOOM.png'))
        self.ZOOM_button.place(x=1215, y=255)

        discord = ImageTk.PhotoImage(Image.open('images/DISCORD.png').resize((40, 40)))

        self.DISCORD_button = Button(bd=2, width=40, height=40, image=discord,
                                     command=lambda: self.change_logo('images/DISCORD.png'))
        self.DISCORD_button.place(x=1270, y=255)

        youtube = ImageTk.PhotoImage(Image.open('images/YOUTUBE.png').resize((40, 40)))

        self.YOUTUBE_button = Button(bd=2, width=40, height=40, image=youtube,
                                     command=lambda: self.change_logo('images/YOUTUBE.png'))
        self.YOUTUBE_button.place(x=1325, y=255)

        telegramm = ImageTk.PhotoImage(Image.open('images/TELEGRAMM.png').resize((40, 40)))

        self.TELEGRAMM_button = Button(bd=2, width=40, height=40, image=telegramm,
                                       command=lambda: self.change_logo('images/TELEGRAMM.png'))
        self.TELEGRAMM_button.place(x=1380, y=255)

        sechenov = ImageTk.PhotoImage(Image.open('images/SECHENOV.png').resize((40, 40)))

        self.SECHENOV_button = Button(bd=2, width=40, height=40, image=sechenov,
                                      command=lambda: self.change_logo('images/SECHENOV.png'))
        self.SECHENOV_button.place(x=1435, y=255)

        self.load_image_button = Button(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font12,
                                        text='Загрузить...', command=self.load_image_button_click)
        self.load_image_button.place(x=1380, y=330)

        self.settings_label = Label(bg=self.win_bg, text="Расширенные настроки", fg=self.font_color,
                                    font=("Cascadia Code", 15))
        self.settings_label.place(x=10, y=10)

        self.design_label = Label(bg=self.element_bg, text="Дизайн", fg=self.font_color, font=self.font_font12,
                                  width=41)
        self.design_label.place(x=10, y=50)

        self.pattern_label = Label(bg=self.win_bg, text="● Шаблон QR-кода", fg=self.font_color, font=self.font_font10)
        self.pattern_label.place(x=20, y=80)
# Кнопки-шаблоны
        horizontal_bars_image = ImageTk.PhotoImage(Image.open('images/Horizontal.png').resize((40, 40)))

        self.HorizontalBarsDrawer_button = Button(bd=2, width=40, height=40, image=horizontal_bars_image,
                                                  command=lambda: self.change_module_driver('HorizontalBarsDrawer'))
        self.HorizontalBarsDrawer_button.place(x=15, y=115)

        vertical_bars_image = ImageTk.PhotoImage(Image.open('images/Vertical.png').resize((40, 40)))

        self.VerticalBarsDrawer_button = Button(bd=2, width=40, height=40, image=vertical_bars_image,
                                                command=lambda: self.change_module_driver('VerticalBarsDrawer'))
        self.VerticalBarsDrawer_button.place(x=70, y=115)

        square_module_drawer = ImageTk.PhotoImage(Image.open('images/Square.png').resize((40, 40)))

        self.SquareModuleDrawer_button = Button(bd=2, width=40, height=40, image=square_module_drawer,
                                                command=lambda: self.change_module_driver('SquareModuleDrawer'))
        self.SquareModuleDrawer_button.place(x=125, y=115)

        rounded_module_drawer = ImageTk.PhotoImage(Image.open('images/Rounded.png').resize((40, 40)))

        self.RoundedModuleDrawer_button = Button(bd=2, width=40, height=40, image=rounded_module_drawer,
                                                 command=lambda: self.change_module_driver('RoundedModuleDrawer'))
        self.RoundedModuleDrawer_button.place(x=180, y=115)

        circle_module_drawer = ImageTk.PhotoImage(Image.open('images/Circle.png').resize((40, 40)))

        self.CircleModuleDrawer_button = Button(bd=2, width=40, height=40, image=circle_module_drawer,
                                                command=lambda: self.change_module_driver('CircleModuleDrawer'))
        self.CircleModuleDrawer_button.place(x=235, y=115)

        grapped_module_drawer = ImageTk.PhotoImage(Image.open('images/Gapped.png').resize((40, 40)))

        self.GappedSquareModuleDrawer_button = Button(bd=2, width=40, height=40, image=grapped_module_drawer,
                                                      command=lambda:
                                                      self.change_module_driver('GappedSquareModuleDrawer'))
        self.GappedSquareModuleDrawer_button.place(x=290, y=115)

        self.color_label = Label(bg=self.win_bg, text="● Цвет", fg=self.font_color, font=self.font_font10)
        self.color_label.place(x=20, y=160)

        self.back_color = Label(bg=self.win_bg, text="Фон #", fg=self.font_color, font=self.font_font8)
        self.back_color.place(x=15, y=190)

        self.back_color_entry = Entry(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font10, width=6)
        self.back_color_entry.place(x=50, y=193)

        self.fill_color = Label(bg=self.win_bg, text="Передний план #", fg=self.font_color, font=self.font_font8)
        self.fill_color.place(x=180, y=190)

        self.fill_color_entry = Entry(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font10, width=6)
        self.fill_color_entry.place(x=275, y=193)

        self.mainloop()

    def change_logo(self, logo_path):
        self.logo_img = logo_path
        self.update_qr()

    def change_module_driver(self, driver_name):
        if driver_name == 'GappedSquareModuleDrawer':
            self.module_driver = GappedSquareModuleDrawer(size_ratio=0.8)
        if driver_name == 'VerticalBarsDrawer':
            self.module_driver = VerticalBarsDrawer(horizontal_shrink=0.8)
        if driver_name == 'HorizontalBarsDrawer':
            self.module_driver = HorizontalBarsDrawer(vertical_shrink=0.8)
        if driver_name == 'SquareModuleDrawer':
            self.module_driver = SquareModuleDrawer()
        if driver_name == 'RoundedModuleDrawer':
            self.module_driver = RoundedModuleDrawer(radius_ratio=1)
        if driver_name == 'CircleModuleDrawer':
            self.module_driver = CircleModuleDrawer()
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
        generate_qr(self.text_box.get("1.0", END), module_driver=self.module_driver,
                    fill_color_param='black', back_color_param='white', image=self.logo_img).save(file_name)

    def load_image_button_click(self):
        file_name = filedialog.askopenfilename(filetypes=[("Файлы изображений", '.png .jpg .jpeg')])
        self.logo_img = file_name
        self.update_qr()
