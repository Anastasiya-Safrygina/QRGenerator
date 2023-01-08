import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage


def generate_qr(data, module_driver, fill_color_param, back_color_param, image):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=False)
    img = qr.make_image(image_factory=StyledPilImage, fill_color=fill_color_param, back_color=back_color_param,
                        module_drawer=module_driver,
                        embeded_image_path=image)
    img.save('qr.png')
    return Image.open('qr.png')
