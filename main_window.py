from tkinter import *


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title('QR Генератор')
        self.geometry('650x320')

        self.size_entry = Entry()
        self.size_entry.grid(row=0, column=0)

        self.qr_panel = Canvas()
