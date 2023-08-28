import qrcode
qr=qrcode.QRCode(
 version=1,
 box_size=10,
)
qr.add_data("https://www.microsoft.com/en-ca/")
img=qr.make_image()
img.save("jasmeh.jpg")
