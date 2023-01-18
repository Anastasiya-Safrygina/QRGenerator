import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage


def generate_qr(data, module_driver, color_mask, image):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=3)
    qr.add_data(data)
    img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=module_driver,
                        embeded_image_path=image,
                        color_mask=color_mask)
    img.save('qr.png')
    return Image.open('qr.png')
