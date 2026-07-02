import qrcode
from PIL import Image

file=open("data.txt","r")
datas=(file.read())
data_split_char=","#split logic add anything which suits your data
list_of_data=datas.split(data_split_char)


# Custom QR code with colors
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
for data in list_of_data:
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{data.split()[0]}.png")

# Add logo to QR code (great for branding)
# Your logo overlay code here