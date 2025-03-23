

import qrcode # type: ignore

data = "My Name Is Hamza Nasir!"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="white")

img.save("E:\Modern_Ai_Python\Python-Projects\Project-4-Assignments\Assignments-01-to-25\QRcode1.png")

