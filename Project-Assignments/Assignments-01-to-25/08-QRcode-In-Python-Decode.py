
from pyzbar.pyzbar import decode # type: ignore
from PIL import Image

img = Image.open('qrcode.png')
result = decode(img)

print(result)