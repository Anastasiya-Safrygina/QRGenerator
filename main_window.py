from tkinter import *
from tkinter import filedialog, colorchooser

from PIL import ImageTk
from qrcode.image.styles.colormasks import *
from qrcode.image.styles.moduledrawers import *

from qr import generate_qr


class MainWindow(Tk):
    logo_img = None
    module_driver = SquareModuleDrawer()
    back_color = (255, 255, 255)
    fill_color = (0, 0, 0)
    gradiant_color = (0, 0, 0)
    color_mask = SolidFillColorMask(back_color=back_color, front_color=fill_color)
    color_mask_value = None

    def __init__(self):
        # Вызов базового конструктора (Мы наследуемся от Tk)
        Tk.__init__(self)

        self.win_bg = '#212121'
        self.canvas_bg = '#121212'
        self.element_bg = '#3f3f3f'
        self.font_color = '#FFFFFF'
        self.font_font10 = ("Cascadia Code", 10)
        self.font_font12 = ("Cascadia Code", 12)
        self.font_font8 = ("Cascadia Code", 8)

        self.title('QR Генератор')
        self.geometry('1350x720')
        self.resizable(False, False)
        self['bg'] = self.win_bg

        self.dark_in_the_center = Label(bg='#141414', width=82, height=50)
        self.dark_in_the_center.place(x=400, y=0)

        self.qr_panel = Canvas(bg=self.canvas_bg, borderwidth=0, bd=0, width=350, height=350,
                               highlightthickness=2, highlightbackground=self.element_bg)
        self.qr_panel.place(x=510, y=60)

        self.save_button = Button(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font12,
                                  text='Сохранить...', command=self.save_button_click)
        self.save_button.place(x=800, y=450)

        self.data_text_label = Label(bg=self.win_bg, text="Текст или ссылка:", fg=self.font_color,
                                     font=("Cascadia Code", 15))
        self.data_text_label.place(x=1000, y=10)

        self.text_box = Text(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font8, width=55, height=5)
        self.text_box.bind("<KeyRelease>", self.on_modified_text)
        self.text_box.place(x=1000, y=50)

        self.data_img_label = Label(bg=self.win_bg, text="Загрузите или выберите логотип",
                                    fg=self.font_color, font=self.font_font12)
        self.data_img_label.place(x=1000, y=140)

        self.img_panel = Canvas(bg=self.element_bg, width=70, height=70,
                                highlightthickness=0, highlightbackground=self.font_color)
        self.img_panel.place(x=1105, y=170)
        # Кнопки-логотипы
        vk = ImageTk.PhotoImage(Image.open('images/VK.png').resize((40, 40)))

        self.VK_button = Button(bd=2, width=40, height=40, image=vk, command=lambda: self.change_logo('images/VK.png'))
        self.VK_button.place(x=1000, y=255)

        zoom = ImageTk.PhotoImage(Image.open('images/ZOOM.png').resize((40, 40)))

        self.ZOOM_button = Button(bd=2, width=40, height=40, image=zoom,
                                  command=lambda: self.change_logo('images/ZOOM.png'))
        self.ZOOM_button.place(x=1055, y=255)

        discord = ImageTk.PhotoImage(Image.open('images/DISCORD.png').resize((40, 40)))

        self.DISCORD_button = Button(bd=2, width=40, height=40, image=discord,
                                     command=lambda: self.change_logo('images/DISCORD.png'))
        self.DISCORD_button.place(x=1275, y=255)

        youtube = ImageTk.PhotoImage(Image.open('images/YOUTUBE.png').resize((40, 40)))

        self.YOUTUBE_button = Button(bd=2, width=40, height=40, image=youtube,
                                     command=lambda: self.change_logo('images/YOUTUBE.png'))
        self.YOUTUBE_button.place(x=1110, y=255)

        telegramm = ImageTk.PhotoImage(Image.open('images/TELEGRAMM.png').resize((40, 40)))

        self.TELEGRAMM_button = Button(bd=2, width=40, height=40, image=telegramm,
                                       command=lambda: self.change_logo('images/TELEGRAMM.png'))
        self.TELEGRAMM_button.place(x=1165, y=255)

        sechenov = ImageTk.PhotoImage(Image.open('images/SECHENOV.png').resize((40, 40)))

        self.SECHENOV_button = Button(bd=2, width=40, height=40, image=sechenov,
                                      command=lambda: self.change_logo('images/SECHENOV.png'))
        self.SECHENOV_button.place(x=1220, y=255)

        self.load_image_button = Button(bg=self.element_bg, fg=self.font_color, bd=0, font=self.font_font12,
                                        text='Загрузить...', command=self.load_image_button_click)
        self.load_image_button.place(x=1000, y=330)

        self.settings_label = Label(bg=self.win_bg, text="Расширенные настроки", fg=self.font_color,
                                    font=("Cascadia Code", 15))
        self.settings_label.place(x=70, y=10)

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

        # Работа с цветом
        self.color_label = Label(bg=self.win_bg, text="● Работа с цветом", fg=self.font_color, font=self.font_font10)
        self.color_label.place(x=20, y=165)

        self.back_color_label = Label(bg=self.win_bg, text="Фон:", fg=self.font_color, font=self.font_font10)
        self.back_color_label.place(x=15, y=205)

        self.back_color_button = Button(bd=0, width=5, height=2, bg='#ffffff', command=self.back_color_button_click)
        self.back_color_button.place(x=55, y=200)

        self.fill_color_label = Label(bg=self.win_bg, text="Цвет 1:", fg=self.font_color, font=("Cascadia Code", 9))
        self.fill_color_label.place(x=15, y=255)

        self.fill_color_button = Button(bd=0, width=5, height=2, bg='#000000', command=self.fill_color_button_click)
        self.fill_color_button.place(x=70, y=250)

        self.gradiant_label = Label(bg=self.win_bg, text="Градиент:", fg=self.font_color, font=("Cascadia Code", 9))
        self.gradiant_label.place(x=150, y=200)

        # Кластер радио_кнопок
        self.color_mask_value = IntVar()
        self.color_mask_value.set(1)
        self.SolidFillColorMask_radio = Radiobutton(text="Однотонный (Цвет 1)", bg=self.win_bg, fg=self.font_color,
                                                    selectcolor='black', activeforeground=self.font_color,
                                                    activebackground=self.win_bg,
                                                    variable=self.color_mask_value, value=1,
                                                    command=self.change_color_mask)
        self.SolidFillColorMask_radio.place(x=180, y=220)
        self.RadialGradiantColorMask_radio = Radiobutton(text="Радиальный", bg=self.win_bg, fg=self.font_color,
                                                         activeforeground=self.font_color, activebackground=self.win_bg,
                                                         selectcolor='black', variable=self.color_mask_value, value=2,
                                                         command=self.change_color_mask)
        self.RadialGradiantColorMask_radio.place(x=180, y=240)
        self.SquareGradiantColorMask_radio = Radiobutton(text="Квадратный", bg=self.win_bg, fg=self.font_color,
                                                         activeforeground=self.font_color, activebackground=self.win_bg,
                                                         selectcolor='black', variable=self.color_mask_value, value=3,
                                                         command=self.change_color_mask)
        self.SquareGradiantColorMask_radio.place(x=180, y=260)
        self.HorizontalGradiantColorMask_radio = Radiobutton(text="Слева направо (Цвет 1 → Цвет 2)",
                                                             bg=self.win_bg, fg=self.font_color,
                                                             activeforeground=self.font_color,
                                                             activebackground=self.win_bg,
                                                             selectcolor='black', variable=self.color_mask_value,
                                                             value=4, command=self.change_color_mask)
        self.HorizontalGradiantColorMask_radio.place(x=180, y=280)
        self.VerticalGradiantColorMask_radio = Radiobutton(text="Сверху вниз (Цвет 1 ↓ Цвет 2)", bg=self.win_bg,
                                                           fg=self.font_color,
                                                           activeforeground=self.font_color,
                                                           activebackground=self.win_bg,
                                                           selectcolor='black', variable=self.color_mask_value, value=5,
                                                           command=self.change_color_mask)
        self.VerticalGradiantColorMask_radio.place(x=180, y=300)

        self.gradiant_color_label = Label(bg=self.win_bg, text="Цвет 2:", fg=self.font_color, font=("Cascadia Code", 9))
        self.gradiant_color_label.place(x=15, y=305)

        self.gradiant_color_button = Button(bd=0, width=5, height=2, bg='#000000',
                                            command=self.gradiant_color_button_click)
        self.gradiant_color_button.place(x=70, y=300)

        self.mainloop()

    def change_logo(self, logo_path):
        self.logo_img = logo_path
        self.update_qr()

    def change_color_mask(self):
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
        val = self.color_mask_value.get()
        if val == 1:
            self.color_mask = SolidFillColorMask(back_color=self.back_color, front_color=self.fill_color)
        elif val == 2:
            self.color_mask = RadialGradiantColorMask(back_color=self.back_color, center_color=self.fill_color,
                                                      edge_color=self.gradiant_color)
        elif val == 3:
            self.color_mask = SquareGradiantColorMask(back_color=self.back_color, center_color=self.fill_color,
                                                      edge_color=self.gradiant_color)
        elif val == 4:
            self.color_mask = HorizontalGradiantColorMask(back_color=self.back_color, left_color=self.fill_color,
                                                          right_color=self.gradiant_color)
        elif val == 5:
            self.color_mask = VerticalGradiantColorMask(back_color=self.back_color, top_color=self.fill_color,
                                                        bottom_color=self.gradiant_color)

        img = generate_qr(self.text_box.get("1.0", END), module_driver=self.module_driver,
                          color_mask=self.color_mask, image=self.logo_img)
        img = img.resize((352, 352))
        img = ImageTk.PhotoImage(img)
        self.qr_panel.create_image(0, 0, anchor=NW, image=img)
        if self.logo_img is not None:
            logo = Image.open(self.logo_img).resize((70, 70))
            logo = ImageTk.PhotoImage(logo)
            self.img_panel.create_image(0, 0, anchor=NW, image=logo)

    def on_modified_text(self, event):
        self.update_qr()

    def save_button_click(self):
        file = filedialog.asksaveasfile(defaultextension='.png', filetypes=[('PNG', '.png'),
                                                                                     ('JPG', '.jpg'),
                                                                                     ('BMP', '.bmp')])
        if file is not None:
            generate_qr(self.text_box.get("1.0", END), module_driver=self.module_driver,
                        color_mask=self.color_mask, image=self.logo_img).save(file.name)

    def load_image_button_click(self):
        file = filedialog.askopenfile(filetypes=[("Файлы изображений", '.png .jpg .jpeg')])
        if file is not None:
            self.logo_img = file.name
            self.update_qr()

    def back_color_button_click(self):
        (rgb, hex) = colorchooser.askcolor()
        self.back_color_button.configure(bg=hex)
        self.back_color = (rgb[0] + 1, rgb[1] + 1, rgb[2] + 1)
        self.update_qr()

    def fill_color_button_click(self):
        (rgb, hex) = colorchooser.askcolor()
        self.fill_color_button.configure(bg=hex)
        self.fill_color = rgb
        self.update_qr()

    def gradiant_color_button_click(self):
        (rgb, hex) = colorchooser.askcolor()
        self.gradiant_color_button.configure(bg=hex)
        self.gradiant_color = rgb
        self.update_qr()
