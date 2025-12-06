import os
import qrcode

img=qrcode.make("https://www.google.com")

img.save('Qr.png','PNG')