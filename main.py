import qrcode
from qrcode import constants

code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=4
)


code.add_data('The address where the QR will be created should be given here.')
code.make(fit=True)

image = code.make_image(fill_color="black",back_color="white")
image.save('png file name should be given here.png')