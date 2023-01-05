import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage


def generateQR(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=False)
    img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="C:\\Users\\aboev\\Downloads\\logo_vk\\Logo_VK\\JPG\\Blue\\VK_logo_Blue_120x120.jpg")
    img.save('qr.png')
    return Image.open('qr.png')
