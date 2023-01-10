import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask


def generate_qr(data, module_driver, fill_color_param, back_color_param, image):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=3)
    qr.add_data(data)
    qr.make(fit=False)
    img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=module_driver,
                        embeded_image_path=image,
                        color_mask=SolidFillColorMask(back_color=back_color_param, front_color=fill_color_param))
    img.save('qr.png')
    return Image.open('qr.png')
