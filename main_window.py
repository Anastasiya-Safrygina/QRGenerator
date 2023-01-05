from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk
from qr import generateQR


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('QR Генератор')
        self.geometry('650x350')
        self.size_entry = Entry()
        self.size_entry.grid(row=0, column=0, sticky=N, padx=15, pady=15)

        self.qr_panel = Canvas(width=200, height=220, highlightthickness=1, highlightbackground="black")
        self.qr_panel.grid(row=1, column=1, padx=15, pady=15, rowspan=2)

        self.text_box = Text(width=25, height=8)
        self.text_box.bind("<KeyRelease>", self.on_modified_text)
        self.text_box.grid(row=0, column=2, padx=15, pady=5, rowspan=2)

        self.image_panel = Canvas(width=200, height=200, highlightthickness=1, highlightbackground="black")
        self.image_panel.grid(row=2, column=2, padx=15, pady=5, rowspan=2)

        self.save_button = Button(text="Сохранить...", command=self.save_button_click)
        self.save_button.grid(row=3, column=1, sticky=N)

        self.load_image_button = Button(text="Загрузить изображение...", command=self.load_image_button_click)
        self.load_image_button.grid(row=4, column=2, sticky=NW)

        self.mainloop()

    def on_modified_text(self, event):
        img = generateQR(self.text_box.get("1.0", END))
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        self.qr_panel.create_image(0, 0, anchor=NW, image=img)

    def save_button_click(self):
        file_name = filedialog.asksaveasfilename(defaultextension='.png')
        generateQR(self.text_box.get("1.0", END)).save(file_name)

    def load_image_button_click(self):
        file_name = filedialog.askopenfilename(filetypes=[("Файлы изображений", '.png .jpg .jpeg')])
