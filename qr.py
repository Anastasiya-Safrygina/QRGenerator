from tkinter import PhotoImage
import qrcode


def generateQR(data):
    # param version
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=4)
    qr.add_data(data)
    qr.make(fit=False)
    img = qr.make_image(fill_color='black', back_color="white")
    img.save('qr.png')
    return PhotoImage(file='qr.png')
